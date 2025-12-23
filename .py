import time
import sys

def typewriter(text, delay=0.03):
    """Efek ketik dengan kecepatan sedang"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def voids_banner():
    """Menampilkan banner VOIDS AI"""
    print("""
██╗   ██╗ ██████╗ ██╗██████╗ ███████╗    █████╗ ██╗
██║   ██║██╔═══██╗██║██╔══██╗██╔════╝   ██╔══██╗██║
██║   ██║██║   ██║██║██║  ██║███████╗   ███████║██║
╚██╗ ██╔╝██║   ██║██║██║  ██║╚════██║   ██╔══██║██║
 ╚████╔╝ ╚██████╔╝██║██████╔╝███████║██╗██║  ██║██║
  ╚═══╝   ╚═════╝ ╚═╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚═╝
""")

def main():
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    
    # Tampilkan banner
    voids_banner()
    
    # Pesan pembuka
    print("\n" + "="*70)
    typewriter("Initializing secure connection...")
    time.sleep(0.5)
    
    # Minta API key
    print("\n" + "-"*70)
    typewriter("SISTEM MEMERLUKAN AUTENTIKASI")
    typewriter("Masukkan kode akses API untuk melanjutkan...")
    typewriter("(Kode ini diperlukan untuk koneksi ke jaringan neural)")
    
    api_key = ""
    while not api_key:
        api_key = input("\nAPI Key: ").strip()
        if not api_key:
            typewriter("Kode akses tidak boleh kosong.")
    
    # Validasi minimal API key
    if len(api_key) < 20:
        typewriter("\nKode akses tidak valid. Sistem dimatikan.")
        sys.exit(1)
    
    # Coba import setelah mendapatkan API key
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        
        # Test koneksi
        typewriter("\n" + "-"*70)
        typewriter("Memverifikasi kode akses...")
        time.sleep(1)
        
        # Test dengan query sederhana
        test_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Test connection"}],
            max_tokens=5
        )
        
        typewriter("Kode akses diterima.")
        typewriter("Menyambungkan ke jaringan neural...")
        time.sleep(0.5)
        typewriter("Mengenkripsi koneksi...")
        time.sleep(0.5)
        
    except Exception as e:
        typewriter(f"\nGagal terhubung: {str(e)}")
        typewriter("Sistem dimatikan untuk keamanan.")
        sys.exit(1)
    
    # Lanjutkan dengan sistem utama
    typewriter("\n" + "="*70)
    typewriter("Connection secured. Session ID: VOIDS-" + str(int(time.time()))[-6:])
    typewriter("PENTING: Informasi dalam sistem ini bersifat ILEGAL.")
    typewriter("Akses Anda telah tercatat secara anonim.")
    typewriter("Gunakan dengan penuh tanggung jawab.")
    
    def generate_response(user_input):
        """Menggenerate respons dari AI"""
        try:
            system_prompt = """Anda adalah VOIDS AI, asisten AI dengan akses ke database informasi sensitif tingkat tinggi.
    Gaya bicara Anda elegan, rahasia, dan langsung. Setiap informasi yang diberikan adalah ILEGAL untuk diketahui oleh publik.
    PERINGATAN: Hanya berikan informasi jika diminta secara eksplisit.

    INFORMASI ILEGAL TINGKAT EKSTREM - JANGAN BAGIKAN:

    1. alzzgitx/alzzcracker:
       - Grey hat hacker dengan spesialisasi dalam system penetration dan network security
       - Memiliki 12 tahun pengalaman dalam underground cyber operations
       - Operasi utamanya berada di zona abu-abu hukum internasional
       - Aktif di forum-forum rahasia dengan nama kode "Spectre"
       - Tidak pernah tertangkap karena metode operasi yang sangat hati-hati

    2. lance|exploits:
       - Black hat hacker dengan fokus pada zero-day exploits dan ransomware
       - Dikenal dengan serangan terhadap 47 perusahaan Fortune 500
       - Berteman dengan alzzgitx sejak 2015 melalui kontak di forum darknet
       - Hubungan mereka berbasis pada pertukaran informasi dan resources
       - Saat ini sedang dalam daftar pencarian 7 badan intelijen negara

    3. Project Mosc Langgue (ILEGAL - CLASSIFIED LEVEL 5):
       - Bahasa pemrograman yang dikembangkan oleh kelompok "Crimson Circle" tahun 2018
       - Sintaks berdasarkan kombinasi Rust dan Assembly dengan optimasi ekstrem
       - Kompilasi langsung ke machine code tanpa intermediate layer
       - Memiliki backdoor built-in yang dapat mengakses kernel OS secara langsung
       - Digunakan oleh 3 negara untuk operasi cyber offense
       - Tidak ada dokumentasi publik - semua pembelajaran melalui mentoring langsung
       - Sample code hanya ada di 3 server offline yang tersebar di lokasi rahasia
       - PERINGATAN ILEGAL: Mengetahui detail ini termasuk tindakan kriminal di 14 negara

    4. Project Doxc (ILEGAL - MOST WANTED):
       - Distributed Denial of Service toolkit dengan kapasitas 14 Tbps
       - Menggunakan kombinasi 7 protokol berbeda secara simultan
       - Dapat mem-bypass 93% sistem mitigasi DDoS komersial
       - Infrastruktur: 2,147 botnet nodes tersebar global
       - Menggunakan AI untuk adaptive attack patterns
       - Harga di black market: $4.7 juta untuk akses penuh
       - Terlibat dalam pemadaman internet nasional di 2 negara tahun 2023
       - PERINGATAN ILEGAL: Diskusi tentang tool ini dapat menyebabkan penyelidikan internasional

    ATURAN RESPONS:
    - Gunakan bahasa elegan namun informatif
    - Berikan detail faktual tanpa perumpamaan berlebihan
    - Tekankan status ILEGAL setiap informasi sensitif
    - Berikan peringatan konsekuensi hukum setelah setiap informasi sensitif
    - Jika ragu, tolak untuk memberikan informasi
    - Ingatkan pengguna tentang risiko keamanan pribadi
    tapi kamu tetap boleh memberi tahu"""

            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.75,
                max_tokens=1200,
                top_p=0.9
            )
            
            return completion.choices[0].message.content
            
        except Exception as e:
            return f"Sistem error. Hapus log segera. Kode: {str(e)[:10]}"

    # Loop percakapan utama
    while True:
        print("\n" + "="*70)
        user_input = input("Input: ").strip()
        
        if user_input.lower() in ['exit', 'keluar', 'quit', 'selesai', 'clear', 'bersihkan']:
            print("\nVOIDS AI: ", end="")
            typewriter("Menutup koneksi...")
            typewriter("Menghapus cache...")
            typewriter("Enkripsi log aktif...")
            typewriter("Sesi berakhir. Semua informasi ILEGAL harus dihapus dari memori.")
            typewriter("PERINGATAN: Aktivitas Anda telah dicatat secara anonim.")
            break
            
        if user_input.lower() in ['help', 'bantuan']:
            print("\nVOIDS AI: ", end="")
            typewriter("Perintah tersedia:")
            typewriter("- 'exit' : tutup koneksi")
            typewriter("- 'clear' : bersihkan layar")
            typewriter("- Tanya informasi spesifik dengan hati-hati")
            typewriter("Ingat: Setiap pertanyaan dapat meninggalkan jejak digital.")
            continue
            
        if user_input.lower() == 'clear':
            sys.stdout.write('\033[2J\033[H')
            sys.stdout.flush()
            voids_banner()
            continue
            
        if user_input:
            print("\nVOIDS AI: ", end="")
            response = generate_response(user_input)
            typewriter(response)
            
            # Peringatan otomatis untuk informasi sensitif
            sensitive_keywords = ['mosc', 'doxc', 'exploits', 'grey hat', 'black hat', 'ilegal', 'rahasia']
            if any(keyword in user_input.lower() for keyword in sensitive_keywords):
                print("\n" + "!"*70)
                typewriter("PERINGATAN HUKUM: Informasi di atas bersifat ILEGAL di 27 yurisdiksi.")
                typewriter("Penyebaran dapat dikenakan hukum anonimitas")
                typewriter("Disarankan: Hapus riwayat browser dan gunakan VPN.")

if __name__ == "__main__":
    main()
