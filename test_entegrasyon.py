from src.utils.file_handler import select_and_copy_pdf
from src.database.db_manager import init_db, add_document, get_documents

if __name__ == "__main__":
    # 1. Veritabanını hazırla (Tablolar yoksa oluşturulur)
    init_db()
    
    print("--- Entegrasyon Testi Başlıyor ---")
    
    # 2. Dosyayı seç ve kopyala
    kaydedilen_yol, dosya_adi = select_and_copy_pdf()
    
    if kaydedilen_yol:
        # 3. Veritabanına kaydet
        # (Arkadaşının add_document fonksiyonundaki parametre sırasına göre düzenle)
        # Örnek: ad, yol, kategori, sayfa_sayisi
        add_document(dosya_adi, kaydedilen_yol, "Genel", 0)
        
        print(f"✅ Başarılı: {dosya_adi} hem klasöre hem veritabanına eklendi!")
        
        # 4. Veritabanından geri oku (Gerçekten orada mı?)
        veriler = get_documents()
        print(f"📋 Güncel Veritabanı Listesi: {veriler}")
    else:
        print("❌ İşlem iptal edildi, dosya seçilmedi.")