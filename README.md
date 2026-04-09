#Case 1: Prediksi Stok
-Variabel
Input: terjual, permintaan, harga, profit  
Output: stok  
-Membership Function  
Input: rendah, sedang, tinggi  
Output: sedang, banyak  
Menggunakan trimf & trapmf  
-Proses  
Input nilai → fuzzifikasi  
Evaluasi rule  
Defuzzifikasi → hasil stok  

#Case 2: Kepuasan Pelayanan  
Variabel  
Input: info, syarat, petugas, sarpras  
Output: kepuasan  
-Membership Function  
Input: tidak, cukup, memuaskan  
Output: tidak, kurang, cukup, memuaskan, sangat  
Menggunakan trapmf & trimf (sesuai grafik)  
-Rule  
Total 81 rule (3⁴ kombinasi)  
Diambil dari file CSV  
Dibuat otomatis dengan loop  
-Proses  
Program membaca CSV → generate rule  
Input nilai → fuzzifikasi  
Evaluasi semua rule  
Defuzzifikasi → nilai kepuasan  
