🦉 Smart Academic Assistant (SAA)
Smart Academic Assistant is a desktop application designed to optimize the academic study experience for students and researchers. 
It serves as a centralized hub for managing course materials, analyzing PDF documents, and enhancing learning through smart search and audio-player features.
🚀 Key Features
Integrated Library System: Organize your academic documents by courses (e.g., Linguistics, Computer Science).

Smart Search Engine: Quickly locate keywords and phrases within your study materials.

Audio Study Session: Listen to your documents with an integrated audio player for better retention.

Academic Dashboard: A user-friendly interface with a specialized "Welcome Screen" for seamless navigation.

Database Management: Securely store and manage your library with a robust SQLite backend.

Appearance Modes: Toggle between Dark and Light modes for comfortable long-term study sessions.
🛠️ Tech Stack
Language: Python 3.12.9

GUI Framework: CustomTkinter (Modern UI)

Database: SQLite3

PDF Processing: PyMuPDF (fitz)

Image Processing: Pillow (PIL)

📂 Project Structure
Smart_Academic_Assistant/
├── main.py              # Entry point of the application
├── src/
│   ├── ui/              # User Interface components (main_window.py, etc.)
│   ├── logic/           # Business logic and DB management (db_manager.py)
│   └── assets/          # Icons, logos, and images
└── database/            # Local SQLite database files

⚙️ Installation & Setup
1. Clone the repository:
   git clone https://github.com/yourusername/Smart_Academic_Assistant.git
2. Install dependencies:
   pip install customtkinter pymupdf pillow
3. Run the application:
   python main.py
   
👥 Development Team
Zeynep — Scrum Master & Project Lead
 Project Coordination: Managed team workflows, sprint cycles, and overall project delivery.
 UI/UX Architecture: Designed the structural framework of the application.
 Text-to-Speech (TTS) Integration: Implemented the auditory learning module to enhance accessibility.

Beyza — File System Engineer
 File Management: Developed functions for secure folder creation, file migration, and automated cleanup.
 Sync System: Built a synchronization protocol to maintain consistency between the local file system and the database.
 System Maintenance: Optimized storage usage by implementing tools to remove redundant files.

İsra — Database & Rendering Engineer
 Data Architecture: Established the SQLite-based system memory for storing document metadata and user progress.
 High-Quality Rendering: Developed the engine that converts PDF pages into optimized images for the UI.
 System Optimization: Enhanced keyword highlighting and ensured high-speed performance during data retrieval.

Oğuz — AI & Search Engine Specialist
 Smart Search: Developed the core text extraction and search engine using advanced PDF analysis.
 AI Integration: Implemented NLP (Natural Language Processing) to improve search accuracy through semantic understanding.
 Keyword Localization: Built the system that identifies the precise coordinate of words within documents.

İrem — Frontend Architect
 Core Layout Design: Designed the foundational visual structure and navigation of the application.
 Dynamic UI: Developed the main dashboard and responsive sidebar for a seamless user experience.
 Theme Engine: Implemented both Light and Dark modes to provide a comfortable study environment.
 
 🚧 Future Improvements
🤖 AI-powered summarization (LLM integration)
🎤 Voice-based search
☁️ Cloud synchronization
📝 Annotation & note-taking system
🌍 Multi-language support

📜 License
MIT License © 2026 The Development Team

This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with proper attribution.

⚠️ Disclaimer

This project was developed for academic purposes.
The software is provided "as is", without warranty of any kind. 

📖 API Documentation - Smart Academic Assistant

1. Database Module (src/logic/db_manager.py)
This module handles all persistent storage operations using SQLite3.

add_collection(name)
Description: Creates a new course category in the database.

Parameters: name (string) - The name of the course.

Returns: True if successful, False if the course already exists.

add_document(name, path, category, collection_id)
Description: Saves a PDF's metadata and links it to a specific course.

Parameters:

name: File name.

path: Local file system path.

collection_id: ID of the related course.

get_all_collections()
Description: Retrieves all created courses from the database.

Returns: A list of tuples containing (id, name, created_at).

2. UI Module (src/ui/main_window.py)
This module manages the graphical interface and user interactions.

handle_file_addition()
Description: Opens a file dialog for the user to select a PDF and triggers the database save sequence.

Trigger: Connected to the "Select PDF File" button.

load_files_by_course(collection_id)
Description: Fetches and displays all PDF documents associated with a specific course ID.

UI Impact: Clears and repopulates the scrollable_books frame.

search_keyword(keyword)
Description: Scans the currently open PDF for the specified text using PyMuPDF.

UI Impact: Highlights found text and updates the results label.

3. PDF Engine (src/logic/pdf_handler.py - if applicable)
extract_text(page_num): Extracts raw text from a specific page for search and audio processing.

render_page(page_num): Converts PDF pages into images for display in the UI.
