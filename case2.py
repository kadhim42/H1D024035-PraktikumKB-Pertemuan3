import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

info = ctrl.Antecedent(np.arange(0, 101, 1), 'info')
syarat = ctrl.Antecedent(np.arange(0, 101, 1), 'syarat')
petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'sarpras')

kepuasan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan')

for var in [info, syarat, petugas, sarpras]:
    var['tidak'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['cukup'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['memuaskan'] = fuzz.trapmf(var.universe, [75, 90, 100, 100])

kepuasan['tidak'] = fuzz.trapmf(kepuasan.universe, [0, 0, 50, 75])
kepuasan['kurang'] = fuzz.trapmf(kepuasan.universe, [50, 75, 100, 125])
kepuasan['cukup'] = fuzz.trapmf(kepuasan.universe, [125, 150, 250, 275])
kepuasan['memuaskan'] = fuzz.trapmf(kepuasan.universe, [250, 275, 325, 350])
kepuasan['sangat'] = fuzz.trapmf(kepuasan.universe, [325, 350, 400, 400])

df = pd.read_csv('81_fuzzy_rules.csv')

# hapus kolom rule
if 'Rule' in df.columns:
    df = df.drop(columns=['Rule'])

mapping = {
    'Tidak Memuaskan': 'tidak',
    'Kurang Memuaskan': 'kurang',
    'Cukup Memuaskan': 'cukup',
    'Memuaskan': 'memuaskan',
    'Sangat Memuaskan': 'sangat'
}

rules = []

def clean(val):
    return val.strip()

for i, row in df.iterrows():
    r = ctrl.Rule(
        info[mapping[clean(row['Kejelasan Informasi'])]] &
        syarat[mapping[clean(row['Kejelasan Persyaratan'])]] &
        petugas[mapping[clean(row['Kemampuan Petugas'])]] &
        sarpras[mapping[clean(row['Ketersediaan Sarpras'])]],
        kepuasan[mapping[clean(row['Kepuasan Pelayanan'])]]
    )
    rules.append(r)

kepuasan_ctrl = ctrl.ControlSystem(rules)
simulasi = ctrl.ControlSystemSimulation(kepuasan_ctrl)

simulasi.input['info'] = 80
simulasi.input['syarat'] = 60
simulasi.input['petugas'] = 50
simulasi.input['sarpras'] = 90

simulasi.compute()

print("Nilai Kepuasan Pelayanan:", simulasi.output['kepuasan'])