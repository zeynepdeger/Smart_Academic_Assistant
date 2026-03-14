import os
import shutil
from tkinter import filedialog, Tk


def select_and_copy_pdf():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="PDF Dosyası Seç",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
        os.makedirs(data_folder, exist_ok=True)

        file_name = os.path.basename(file_path)
        destination = os.path.join(data_folder, file_name)

        shutil.copy2(file_path, destination)

        print(f"Dosya kütüphaneye başarıyla eklendi: {file_name}")
        return destination ,file_name
    else:
        print("Dosya seçilmedi.")
        return None, None


if __name__ == "__main__":
    select_and_copy_pdf()