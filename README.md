# Blog

Создать и активировать виртуальное окружение:
```
  python3 -m venv venv
  source venv/bin/activate 
```
Обновить pip до последней версии:
```
  python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
  pip install -r requirements.txt
```
Выполнить миграции:
```
  python3 manage.py migrate
  ```
Запустить проект:
```
  python3 manage.py runserver
```
