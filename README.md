<b>Запуск проекта</b>

1. git clone https://github.com/Endorfin86/django.git
2. cd django
3. python -m venv venv
4. venv\Scripts\activate
5. pip install -r requirements.txt
6. cd Menu
7. python manage.py migrate
8. python manage.py createsuperuser
9. python manage.py runserver

<b>Создание меню</b>
1. Создать меню в админпанели
2. Создать разделы и подразделы меню в админпанели
3. Разместить код формата {% draw_menu 'name_menu (Имя)' select %} в шаблонах home.html и page.html
