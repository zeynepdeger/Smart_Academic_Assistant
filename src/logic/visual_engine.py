import fitz  # pymupdf
from PIL import Image
import io

# Cache (önbellek)
page_cache = {}


# 📌 PDF sayfasını resme çevirme
def render_page(pdf_path, page_number, zoom=2):
    key = (pdf_path, page_number, zoom)

    # cache kontrolü
    if key in page_cache:
        return page_cache[key]

    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number)

    # çözünürlük artırma
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)

    img = Image.open(io.BytesIO(pix.tobytes("png")))

    doc.close()

    # cache'e kaydet
    page_cache[key] = img

    return img


# 📌 Sarı highlight (fosforlu kalem)
def highlight_text(pdf_path, page_number, rects):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number)

    for rect in rects:
        highlight = page.add_highlight_annot(rect)
        highlight.update()

    doc.saveIncr()
    doc.close()


# 📌 Altı kırmızı çizili (underline)
def underline_text(pdf_path, page_number, rects):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number)

    for rect in rects:
        underline = page.add_underline_annot(rect)
        underline.set_colors(stroke=(1, 0, 0))  # kırmızı
        underline.update()

    doc.saveIncr()
    doc.close()


# 📌 Koordinat dönüştürme (PDF → Image)
def convert_coords(rect, zoom):
    return fitz.Rect(
        rect.x0 * zoom,
        rect.y0 * zoom,
        rect.x1 * zoom,
        rect.y1 * zoom
    )