import fitz
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def turkce_kucuk_harf(metin):
    """
    Büyük/Küçük harf ve Türkçe karakter (İ-i, I-ı, Ş-ş) sorununu kökten çözer.
    Kelime köklerini (Örn: İntegral -> integral) yakalamamızı sağlar.
    """
    harfler = {'İ': 'i', 'I': 'ı', 'Ş': 'ş', 'Ğ': 'ğ', 'Ü': 'ü', 'Ö': 'ö', 'Ç': 'ç'}
    for buyuk, kucuk in harfler.items():
        metin = metin.replace(buyuk, kucuk)
    return metin.lower()

def smart_search_in_pdf(pdf_path, query, similarity_threshold=0.3):
    """
    Hem kelime köküne/harfe duyarlı hem de anlamsal (vektörel) arama yapar.
    Arayüz (UI) ekibi için Sayfa No, Koordinatlar ve Önizleme Metni paketleyip döndürür.
    """
    doc = fitz.open(pdf_path)
    results = []
    
    query_vector = model.encode(query, convert_to_tensor=True) 
    query_lower = turkce_kucuk_harf(query)                     

    for page_num in range(len(doc)):
        page = doc[page_num]
        actual_page = page_num + 1
        
        blocks = page.get_text("blocks")
        
        for b in blocks:
            x0, y0, x1, y1, text, block_no, block_type = b
            
            if block_type == 0:
                text_clean = text.strip()
                if not text_clean:
                    continue
                    
                text_lower = turkce_kucuk_harf(text_clean)
                
                is_exact_match = query_lower in text_lower
                
                block_vector = model.encode(text_clean, convert_to_tensor=True)
                similarity = util.cos_sim(query_vector, block_vector).item()
                is_semantic_match = similarity >= similarity_threshold
                
                if is_exact_match or is_semantic_match:
                    
                    preview = text_clean[:100].replace('\n', ' ') + "..."
                    
                    results.append({
                        "sayfa": actual_page,
                        "koordinatlar": {"x0": round(x0, 1), "y0": round(y0, 1), "x1": round(x1, 1), "y1": round(y1, 1)},
                        "onizleme": preview,
                        "benzerlik_skoru": round(similarity, 2),
                        "eslesme_turu": "Kök Eşleşmesi" if is_exact_match else "Anlamsal Eşleşme"
                    })
                    
    doc.close()
    
    if results:
        print(f"\n🎯 Arama: '{query}' -> Toplam {len(results)} paragrafta/cümlede bulundu.")
        for res in results:
            print(f"Sayfa {res['sayfa']} | Tür: {res['eslesme_turu']} (Skor: {res['benzerlik_skoru']})")
            print(f"Önizleme: {res['onizleme']}\n" + "-"*40)
    else:
        print(f"\nArama: '{query}' -> Anlamsal veya harf bazlı sonuç bulunamadı.")
        
    return results