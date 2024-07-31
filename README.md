# Bulk-whatsapp
Perangkat Lunak open source untuk mengirim pesan berkala secara otomatis ke banyak nomor

# Installasi dan Penggunaan

## Installasi

Clone repository ini!.

```bash
git clone https://github.com/huda1603/Bulk-whatsapp.git
```

Change directory ke repository.

```bash
cd Bulk-whatsapp
```

Install Module.

```bash
pip install -r requirements.txt
```

## Penggunaan

Edit File **config-wa-sender.txt**

*Contoh:*
```bash
PathFileNumber = "C:\bulk-wa\nomor.txt"
Pesan = (
Halo, Huda

Gimana Kabarmu
Semoga Sehat Selalu
)
Jeda_Waktu = "16"
```

Jalankan program main.py dan tetap mengikuti alurnya.

```bash
python main.py
```
*Note: Sebelum menjalankan program pastikan kamu sudah membuka aplikasi whatsapp terlebih dahulu(bukan whatsapp web)*
