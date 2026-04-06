# 🌤️ PyWeather - Aplikacja Pogodowa

Kompaktowa aplikacja pogodowa napisana w języku Python z wykorzystaniem framweorku Flask. Aplikacja na żywo pobiera aktualne dane meteo z zewnętrznego serwera OpenWeatherMap API oraz trwale zapisuje historię wyszukiwań użytkownika w profesjonalnej relacyjnej bazie danych PostgreSQL.

Wizualna część projektu (Frontend) została całkowicie ręcznie napisana z wykorzystaniem najnowszych trendów "Glassmorphism" w czystym języku CSS i HTML.

## ✨ Główne funkcje
- Wyszukiwanie żywej temperatury i odczuwalności dla podanego miasta
- Dynamiczne ładowanie ikon pogodowych prosto z serwerów API
- Odporność na błędy (Wyłapywanie wyjątków literówek i nieistniejących miast z błędem 404)
- **Historia zapytań:** Połączenie z bazą PostgreSQL przez moduł SQLAlchemy. Pamięta 3 ostatnie, poprawnie wyszukane przez użytkowników miasta i renderuje je dynamicznie pod spodem loginu.

## 🛠️ Wykorzystane technologie:
- **Backend:** Python + Flask
- **Baza Danych:** PostgreSQL + gotowy ORM Flask-SQLAlchemy
- **API:** REST API (OpenWeatherMap) z wykorzystaniem biblioteki `requests`
- **Frontend:** HTML, Jinja2, CSS3 (Stylizacja Glassmorphism)

## 🚀 Jak uruchomić to u siebie? (Dla rekruterów / innych programistów)
1. Pobierz lub sklonuj ten kod do siebie na komputer.
2. Otwórz projekt w edytorze kodu i stwórz swoje środowisko: `python -m venv venv`
3. Aktywuj je: `.\venv\Scripts\activate` (na komputerach Windows)
4. Zainstaluj wszystkie niezbędne paczki jednym kliknięciem:
`pip install -r requirements.txt`
5. Pamiętaj o ustawieniu własnej bazy PostgreSQL (domyślna nazwa wg `app.py` to "Pogoda").
6. Utwórz absolutnie nowy plik o nazwie `.env` w głównym folderze projektu i wprowadź w nim wygenerowany dla Ciebie przez internet klucz do pogody w formacie:
`API_KEY=TutajTwojPrywatnyKlucz`
7. Wystartuj serwer wykrzykując `flask run` albo `python app.py`. Gotowe!
