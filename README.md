Пошаговая установка
1. Клонирование репозитория
bash
git clone https://github.com/Surene0/social-network.git
cd social-network
2. Создание виртуального окружения
bash
# Для Windows
python -m venv venv
venv\Scripts\activate

# Для Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Установка зависимостей

bash
pip install -r requirements.txt
4. Настройка переменных окружения

bash
# Копируем пример файла настроек
cp .env.example .env

# Редактируем файл .env (укажите свои значения)
# SECRET_KEY=ваш-уникальный-секретный-ключ
# DEBUG=True
# ALLOWED_HOSTS=localhost,127.0.0.1
5. Применение миграций базы данных

bash
python manage.py makemigrations
python manage.py migrate
6. Создание суперпользователя

bash
python manage.py createsuperuser
# Используйте email вместо username
7. Сбор статических файлов

bash
python manage.py collectstatic --noinput
8. Запуск сервера разработки

bash
python manage.py runserver
9. Открытие в браузере
Перейдите по адресу: http://127.0.0.1:8000

Админ-панель: http://127.0.0.1:8000/admin