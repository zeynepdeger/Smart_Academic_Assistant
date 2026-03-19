import sqlite3
from datetime import datetime

DB_NAME = "SAA_Library.db"

# 1. Veritabanını ve Yeni Tablo Yapısını Hazırlar
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Koleksiyonlar (Klasörler) Tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS collections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        collection_name TEXT NOT NULL,
        created_at TEXT
    )
    """)

    # Belgeler Tablosu (Mevcut yapıya collection_id eklendi)
    # FOREIGN KEY ile koleksiyonlara bağladık.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        file_path TEXT,
        category TEXT,
        last_page INTEGER,
        collection_id INTEGER,
        FOREIGN KEY (collection_id) REFERENCES collections (id) ON DELETE SET NULL
    )
    """)

    conn.commit()
    conn.close()

# --- KOLEKSİSYON YÖNETİMİ ---

def add_collection(name):
    """Yeni bir ders grubu/koleksiyon oluşturur."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    date_now = datetime.now().strftime("%d-%m-%Y %H:%M")
    cursor.execute("INSERT INTO collections (collection_name, created_at) VALUES (?, ?)", (name, date_now))
    conn.commit()
    conn.close()

def get_files_in_collection(collection_id):
    """Belirli bir koleksiyonun (klasörün) içindeki tüm PDF'leri getirir."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documents WHERE collection_id = ?", (collection_id,))
    files = cursor.fetchall()
    conn.close()
    return files

# --- BELGE VE TAŞIMA İŞLEMLERİ ---

def add_document(file_name, file_path, category, collection_id=None, last_page=0):
    """Yeni kitap eklerken artık opsiyonel olarak koleksiyon_id de alabilir."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO documents (file_name, file_path, category, collection_id, last_page)
    VALUES (?, ?, ?, ?, ?)
    """, (file_name, file_path, category, collection_id, last_page))
    conn.commit()
    conn.close()

def move_document(doc_id, new_collection_id):
    """Bir PDF'i başka bir koleksiyona taşır (UPDATE sorgusu)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Kaptan'ın İpucu: WHERE şartını asla unutma!
    cursor.execute("UPDATE documents SET collection_id = ? WHERE id = ?", (new_collection_id, doc_id))
    conn.commit()
    conn.close()

# --- GELİŞMİŞ ARAMA (JOIN DESTEĞİ) ---

def search_documents(query_text):
    """Hem dosya adında hem de koleksiyon adında arama yapar."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    search = f"%{query_text}%"
    
    # JOIN kullanarak iki tabloyu birleştirip arama yapıyoruz
    sql = """
    SELECT d.file_name, c.collection_name, d.category 
    FROM documents d
    LEFT JOIN collections c ON d.collection_id = c.id
    WHERE d.file_name LIKE ? OR c.collection_name LIKE ? OR d.category LIKE ?
    """
    cursor.execute(sql, (search, search, search))
    results = cursor.fetchall()
    conn.close()
    return results

def get_documents():
    """Kütüphanedeki tüm belgeleri listeler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documents")
    documents = cursor.fetchall()
    conn.close()
    return documents