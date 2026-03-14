import sys
import os

# 1. Adım: Proje klasörlerini (src altındakileri) sisteme tanıtıyoruz
# Bu sayede "import ui" dediğinde bilgisayar src/ui klasörüne bakacağını anlar.
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def start_app():
    """Uygulamayı başlatan ana fonksiyon."""
    print("-----------------------------------------")
    print("🚀 SMART ACADEMIC ASSISTANT BAŞLATILIYOR...")
    print("-----------------------------------------")
    print("Kaptan: Sistem hazır, mürettebat bekleniyor!")
    
    # İleride 4. kişi arayüzü bitirdiğinde buraya şu satırı ekleyeceğiz:
    # from ui.main_window import MainWindow
    # app = MainWindow()
    # app.mainloop()

if __name__ == "__main__":
    start_app() 
    