# 📈 Parqet Telegramer
Ein Telegram-Bot, der es ermöglicht, PDF-Dateien direkt an Parqet hochzuladen. Ideal für Nutzer, die ihre Depottransaktionen effizient und automatisiert verwalten möchten.

Bitte beachte, dass derzeit nur eine PDF-Datei pro Chat-Nachricht unterstützt wird.

# 🚀 Funktionen
* 📄 Empfängt PDF-Dateien über Telegram
* 🔒 Authentifiziert Nutzer basierend auf ihrer Telegram User ID
* 🌐 Automatischer Upload der empfangenen PDFs zu Parqet mittels Playwright
* 💬 Benachrichtigt den Nutzer über den Status des Uploads

# 🛠️ Voraussetzungen
* Python 3.8 oder höher
* Telegram Bot Token und User ID
* Parqet-Konto mit gültigen Zugangsdaten
* Installierte Systemabhängigkeiten für Playwright (siehe unten)

Weitere Infos folgen. Es ist bisher eher basic, funktioniert aber.

Software-Dependencies (ohne Gewähr):
* python > 3.8
* pip-packages: ython-telegram-bot, playwright, python-dotenv
* libnss3, libatk-bridge2.0-0, libxss1, libasound2, libxshmfence1, libgbm1
