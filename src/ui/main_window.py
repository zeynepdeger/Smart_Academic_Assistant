import customtkinter as ctk
from tkinter import filedialog

# Proje Renk Paleti (Mavi Temalar)
THEMES = {
    "dark": {"bg": "#0B192C", "sidebar": "#1E3E62", "text": "white"},
    "light": {"bg": "#E3F2FD", "sidebar": "#BBDEFB", "text": "#0D47A1"}
}

class SmartAcademicAssistant(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.title("Smart Academic Assistant (SAA)")
        self.geometry("1100x700")
        ctk.set_appearance_mode("dark")

        # Grid Düzeni: Sol taraf Sidebar (Kitaplık), Sağ taraf Ana İçerik
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (DİJİTAL KİTAPLIK) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="SAA KİTAPLIK", 
                                      font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=30, padx=20)

        # Kitap Listesi (Dinamik Liste Alanı)
        self.book_list = ctk.CTkLabel(self.sidebar_frame, text="Kitaplarınız burada listelenecek...", 
                                      font=ctk.CTkFont(size=12), text_color="gray")
        self.book_list.pack(pady=20)

        # Mod Değiştirici Switch
        self.mode_switch = ctk.CTkSwitch(self.sidebar_frame, text="Bebe Mavisi (Işık)", 
                                         command=self.toggle_appearance_mode)
        self.mode_switch.pack(side="bottom", pady=20)

        # --- ANA EKRAN (VİTRİN) ---
        self.main_content = ctk.CTkFrame(self, fg_color="transparent")
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_content.grid_columnconfigure(0, weight=1)
        self.main_content.grid_rowconfigure(1, weight=1)

        # "Dosya Seç" Butonu ve Yazı
        self.upload_btn = ctk.CTkButton(self.main_content, text="📂 Dosya Seç", 
                                        width=300, height=100, font=ctk.CTkFont(size=24),
                                        hover_color="#1976D2", # Hover efekti
                                        command=self.on_file_selected)
        self.upload_btn.grid(row=1, column=0)

        self.info_label = ctk.CTkLabel(self.main_content, 
                                       text="Dosya seçin ve aradığınız sayfayı hemen bulun.",
                                       font=ctk.CTkFont(size=16))
        self.info_label.grid(row=2, column=0, pady=20)

        # Gizli Arama Alanı (Dosya seçilince aktif olur)
        self.search_area = ctk.CTkFrame(self.main_content, fg_color="transparent")
        self.search_entry = ctk.CTkEntry(self.search_area, placeholder_text="Anlam olarak ara...", width=400)
        self.add_btn = ctk.CTkButton(self.search_area, text="Kitaplığa Ekle", fg_color="#2E7D32")

    def on_file_selected(self):
        """Dosya seçildiği an çalışan dinamik yerleşim fonksiyonu"""
        path = filedialog.askopenfilename(filetypes=[("Belgeler", "*.pdf *.pptx")]) # PDF ve PPTX desteği [cite: 72]
        if path:
            # Butonu yukarı kaydır ve küçült
            self.upload_btn.grid(row=0, column=0, pady=(20, 10))
            self.upload_btn.configure(width=200, height=40, font=ctk.CTkFont(size=14))
            
            # Arama çubuğunu ve ekle butonunu göster
            self.search_area.grid(row=1, column=0, pady=40)
            self.search_entry.pack(side="left", padx=10)
            self.add_btn.pack(side="left", padx=10)
            self.info_label.configure(text=f"Yüklenen: {path.split('/')[-1]}")

    def toggle_appearance_mode(self):
        """Gece Mavisi ve Bebe Mavisi arası geçiş"""
        if self.mode_switch.get() == 1:
            ctk.set_appearance_mode("light")
            self.configure(fg_color=THEMES["light"]["bg"])
        else:
            ctk.set_appearance_mode("dark")
            self.configure(fg_color=THEMES["dark"]["bg"])

if __name__ == "__main__":
    app = SmartAcademicAssistant()
    app.mainloop()