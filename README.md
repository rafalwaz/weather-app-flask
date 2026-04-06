# Aplikacja Pogodowa (Python + Flask)

Prosty projekt typu Full-Stack, w którym połączyłem zewnętrzne API pogodowe z własną bazą danych.

## Działanie

Aplikacja pozwala użytkownikowi wpisać nazwę miasta, a następnie pobiera aktualne dane pogodowe z API OpenWeatherMap. Wyświetlana jest m.in. temperatura oraz ikony pogody.

Dodatkowo aplikacja zapisuje historię wyszukiwań w bazie danych PostgreSQL. Przy każdym zapytaniu zapisywany jest wynik, a na stronie wyświetlane są 3 ostatnie wyszukania.

Do obsługi bazy danych wykorzystałem SQLAlchemy jako ORM.

Warstwa frontowa została zbudowana przy użyciu Jinja2 oraz czystego HTML i CSS (bez gotowych szablonów). Styl oparty jest na efekcie Glassmorphism.

## Użyte technologie

- **Backend**: Python (Flask)
- **Baza danych**: PostgreSQL + SQLAlchemy (ORM)
- **API**: OpenWeatherMap + biblioteka `requests`
- **Frontend**: HTML, CSS, Jinja2
- **Konfiguracja**: python-dotenv (.env)
