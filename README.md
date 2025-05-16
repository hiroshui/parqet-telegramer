This is NOT an official product of Parqet!

# 📈 Parqet Telegramer
Ein Telegram-Bot, der es ermöglicht, PDF-Dateien direkt an Parqet hochzuladen. Ideal für Nutzer, die ihre Depottransaktionen effizient und automatisiert verwalten möchten.

Bitte beachte, dass derzeit nur eine PDF-Datei pro Chat-Nachricht unterstützt wird.

# 🚀 Funktionen
* 📄 Empfängt PDF-Dateien über Telegram
* 🔒 Authentifiziert Nutzer basierend auf ihrer Telegram User ID
* 🌐 Automatischer Upload der empfangenen PDFs zu Parqet mittels Playwright
* 💬 Benachrichtigt den Nutzer über den Status des Uploads

# 🛠️ Voraussetzungen
* Linux bzw. Windows Subsystem for Linux (WSL)
* Python 3.8 oder höher
* Telegram Bot Token und User ID
* Parqet-Konto mit gültigen Zugangsdaten
* Installierte Systemabhängigkeiten für Playwright (siehe unten)

Weitere Infos folgen. Es ist bisher eher basic, funktioniert aber.

# Software-Dependencies (ohne Gewähr):
* python > 3.8
* pip-packages: ython-telegram-bot, playwright, python-dotenv
* libnss3, libatk-bridge2.0-0, libxss1, libasound2, libxshmfence1, libgbm1

# Installationsanleitung

0. Erzeuge einen Account bei Parqet und einen Bot via Telegram. (https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/, app.parqet.com)
1. Clone das repo via `git clone $REPO`
2. Erstelle eine .env-Datei im Projektverzeichnis mit folgendem Inhalt:
.env: 
```
TELEGRAM_TOKEN=dein_telegram_bot_token
TELEGRAM_USER_ID=deine_telegram_user_id
PARQET_ID=deine_portfolio_id_aus_parqet (https://app.parqet.com/p/PORTFOLIO)
```
3. Installiere alle Dependencies - eine richtige Anleitung dazu folgt ggf. noch. Sonst frag mich gerne.
4. Run it `python bot.py`
5. Du kannst deinem Bot nun PDF-Dateien schicken und schauen, ob es klappt.

Bitte beachte, die App ist noch nicht super stabil. Es läuft, aber viele Dinge könnten schneller gehen. War ein kleines Freitagsnachmittag-Projekt, in das ich ca 2h reingesteckt habe :)

Feel free!
