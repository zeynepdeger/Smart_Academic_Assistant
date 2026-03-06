import fitz 

def extract_text(pdf_path):
    """PDF'i açıp tüm sayfaların metnini bir liste olarak döndürür."""
    text_list = []
    doc = fitz.open(pdf_path)
    
    for page in doc:
        text_list.append(page.get_text())
        
    doc.close()
    return text_list

def search_word_and_get_coordinates(pdf_path, keyword):
    """Kelimeyi arar, koordinatları saklar ve istenen çıktıyı verir."""
    doc = fitz.open(pdf_path)
    found_pages = []
    all_coordinates = [] 

    for page_num in range(len(doc)):
        page = doc[page_num]
        
        rects = page.search_for(keyword)
        
        if rects:
            actual_page = page_num + 1  
            found_pages.append(actual_page)
            
            for rect in rects:
                all_coordinates.append({
                    "sayfa": actual_page,
                    "x0": rect.x0, 
                    "y0": rect.y0, 
                    "x1": rect.x1, 
                    "y1": rect.y1
                })
                
    doc.close()

    # Çıktı formatını ayarlama
    if found_pages:
        if len(found_pages) == 1:
            pages_str = str(found_pages[0])
        else:
            pages_str = ", ".join(map(str, found_pages[:-1])) + " ve " + str(found_pages[-1])
            
        print(f"Arama: {keyword} -> Sonuç: {pages_str}. sayfalarda bulundu")
    else:
        print(f"Arama: {keyword} -> Sonuç: Belgede bulunamadı.")

    return all_coordinates