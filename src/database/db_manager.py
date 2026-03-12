import sqlite3

DB_NAME = "SAA_Library.db"


# Veritabanını oluşturur ve tabloyu hazırlar
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        file_path TEXT,
        category TEXT,
        last_page INTEGER
    )
    """)

    conn.commit()
    conn.close()


# Yeni kitap/PDF ekleme
def add_document(file_name, file_path, category, last_page=0):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO documents (file_name, file_path, category, last_page)
    VALUES (?, ?, ?, ?)
    """, (file_name, file_path, category, last_page))

    conn.commit()
    conn.close()


# Kütüphanedeki tüm belgeleri listeleme
def get_documents():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM documents")
    documents = cursor.fetchall()

    conn.close()
    return documents