# YouTube_video_data

## Описание:

Проект для друга. Телеграмм бот, который собирают информацию о видео по ссылке на YouTube.

## Основные установки:

### Скачать проект:
```
git clone https://github.com/R3on322/YouTube_video_data.git
```
### Создать виртуальное окружение:
```
python -m venv venv
```
### Установить модули из приложения:

requierements.txt - все неоходимые зависимости там.
```
pip install -r requirements.txt
```

### Запуск проекта:
- В папке services указать свой полный путь до файла yandexdriver.exe, из этого проекта.
(Например: C:\\...\\YouTube_video_data\\services\\yandexdriver.exe)
- Создать файл docker-compose.yaml на основе docker_compose.example.yaml
- Создать файл .env на основе .env.example
- Запустить БД через docker_compose(docker-compose up -d в терминале)
- Запуск приложения через bot.py

### Обновить pip до последней версии:
```
python -m pip install --upgrade pip
```

### Используется:

- Python 3.10
- Aiogram 3.0+
- PostgreSQL
- Asyncpg
- SQLAlchemy

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

![Jokes Card](https://readme-jokes.vercel.app/api)
