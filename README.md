Быстрый старт

#1. Клонирование репозитория
bash
git clone https://github.com/Surene0/social-network.git
cd social-network

#2. Создание виртуального окружения
Windows:
bash
python -m venv venv  
venv\Scripts\activate
Linux/Mac:
bash
python3 -m venv venv
source venv/bin/activate

#3. Установка зависимостей
bash
pip install -r requirements.txt

#4. Настройка переменных окружения
bash
Копируем файл с примерами настроек
cp .env.example .env
Отредактируйте файл .env, указав свои значения:
env
SECRET_KEY=ваш-уникальный-секретный-ключ-сгенерируйте-через-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3  # или настройте PostgreSQL
⚠️ Важно: Для генерации SECRET_KEY можно выполнить:
bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

#5. Применение миграций базы данных
bash
python manage.py makemigrations
python manage.py migrate

#6. Создание суперпользователя (опционально)
bash
python manage.py createsuperuser

#7. Запуск сервера разработки
bash
python manage.py runserver
Приложение будет доступно по адресу: http://127.0.0.1:8000
Админ-панель: http://127.0.0.1:8000/admin
