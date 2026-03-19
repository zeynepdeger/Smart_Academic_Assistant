import customtkinter as ctk
from PIL import Image , ImageDraw
import os

# --- LOGO TABANLI RENK PALETİ ---
BG_COLOR = "#0A192F"          # Derin Lacivert (Logonun dış halkası)
SIDEBAR_COLOR = "#112240"     # Koyu Mavi (Logonun iç kısmı)
ACCENT_BLUE = "#38BDF8"       # Neon Buz Mavisi (Baykuşun parlayan kısımları)
TEXT_COLOR = "#E6F1FF"        # Ferah Beyaz/Mavi (Yazılar)

class SmartAcademicAssistant(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Başlığı ve Boyutu
        self.title("Smart Academic Assistant")
        self.geometry("1150x750")
        
        # Tema Ayarı (Açılışta karanlık mod ve logo renkleri)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color=BG_COLOR)

        # Grid (Izgara) Yapısı: Sol taraf menü, sağ taraf ana içerik
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (SOL PANEL) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color=SIDEBAR_COLOR)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_propagate(False) # Genişliği sabit tut

       
       # --- SIDEBAR İÇERİĞİ ---
       # 1. Logo ve Başlık Alanı
        self.logo_space = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.logo_space.pack(pady=(50, 20), padx=20, fill="x")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(current_dir, "logo.png")

        try:
            pil_image = Image.open(logo_path).convert("RGBA")
            target_size = (180, 180)
            pil_image = pil_image.resize(target_size, Image.Resampling.LANCZOS)
            
            mask = Image.new("L", target_size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + target_size, fill=255)
            
            round_pil_image = Image.new("RGBA", target_size, (0, 0, 0, 0))
            round_pil_image.paste(pil_image, (0, 0), mask=mask)
            
            logo_image = ctk.CTkImage(light_image=round_pil_image, dark_image=round_pil_image, size=target_size)
            self.logo_label = ctk.CTkLabel(self.logo_space, image=logo_image, text="")
            self.logo_label.pack()
            
        except Exception as e:
            print(f"Logo hatası: {e}")
            self.logo_label = ctk.CTkLabel(self.logo_space, text="S A A", font=ctk.CTkFont(size=32, weight="bold"), text_color=ACCENT_BLUE)
            self.logo_label.pack()

        self.subtitle_label = ctk.CTkLabel(self.logo_space, text="SMART ACADEMIC\nASSISTANT", 
                                          font=ctk.CTkFont(size=16, weight="bold", family="Segoe UI"),
                                          text_color=ACCENT_BLUE,
                                          )
        self.subtitle_label.pack(pady=(20, 0))
       
        # 2. Ayırıcı Çizgi
        self.separator = ctk.CTkFrame(self.sidebar_frame, height=2, fg_color=BG_COLOR)
        self.separator.pack(fill="x", padx=30, pady=(25,15))
        # 3. Kaydırılabilir Kitap Listesi Alanı
        # Burası dosyaların isimlerinin şık kutucuklar halinde görüneceği yer
        self.scrollable_books = ctk.CTkScrollableFrame(self.sidebar_frame, 
                                                       fg_color="transparent", 
                                                       label_text="",
                                                       scrollbar_button_color=BG_COLOR,
                                                       scrollbar_button_hover_color=ACCENT_BLUE)
        self.scrollable_books.pack(expand=True, fill="both", padx=10, pady=10)

        # Örnek Bir Kitap (Nasıl duracağını görmen için geçici)
        self.sample_book = ctk.CTkButton(self.scrollable_books, 
                                         text="📄 Örnek_Makale.pdf", 
                                         fg_color="transparent", 
                                         text_color=TEXT_COLOR,
                                         anchor="w", 
                                         hover_color=BG_COLOR,
                                         font=ctk.CTkFont(size=13))
        self.sample_book.pack(fill="x", pady=2)

        # 4. Hızlı Ekle Butonu (Sidebar'ın altına sabit)
        self.add_book_btn = ctk.CTkButton(self.sidebar_frame, 
                                          text="+ Kitaplığa Ekle", 
                                          fg_color=ACCENT_BLUE, 
                                          text_color=BG_COLOR,
                                          hover_color="#00BFFF",
                                          font=ctk.CTkFont(size=14, weight="bold"),
                                          corner_radius=8)
        self.add_book_btn.pack(pady=20, padx=20, fill="x")
# 4. Theme Switch (English names)
        self.mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode", 
                                      font=ctk.CTkFont(size=12, weight="bold"),
                                      text_color=ACCENT_BLUE)
        self.mode_label.pack(side="bottom", pady=(0, 5))

        self.theme_switch = ctk.CTkSwitch(self.sidebar_frame, text="Dark / Light", 
                                         command=self.toggle_theme,
                                         progress_color=ACCENT_BLUE)
        self.theme_switch.pack(side="bottom", pady=(0, 20))

    # --- UPDATED THEME TOGGLE (LOGONUN AÇIK MAVİSİ) ---
    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            # LIGHT MODE - Ice Blue Harmonized
            MAIN_BG_LIGHT = "#E1F5FE"
            SIDEBAR_BG_LIGHT = "#B3E5FC"
            BORDER_LIGHT = "#81D4FA" # Çerçeve rengi (biraz daha belirgin mavi)
            
            ctk.set_appearance_mode("light")
            self.configure(fg_color=MAIN_BG_LIGHT)
            self.sidebar_frame.configure(fg_color=SIDEBAR_BG_LIGHT, border_color=BORDER_LIGHT)
            
            self.subtitle_label.configure(text_color="#0D47A1") 
            self.mode_label.configure(text_color="#0D47A1")
            self.library_label.configure(text_color="#01579B")
            
        else:
            # DARK MODE
            ctk.set_appearance_mode("dark")
            self.configure(fg_color="#0A192F")
            self.sidebar_frame.configure(fg_color="#112240", border_color="#1E293B")
            self.subtitle_label.configure(text_color="#38BDF8")
            self.mode_label.configure(text_color="#38BDF8")
            self.library_label.configure(text_color="gray")
if __name__ == "__main__":
    app = SmartAcademicAssistant()
    app.mainloop()