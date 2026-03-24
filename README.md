# Матеріали курсу Python Frameworks 2026

## Структура проєкту

```
python-frameworks-2026/
├── static/          # Статичні файли (CSS, зображення, JS)
├── templates/       # HTML-шаблони Jinja2
├── first.py         # Головний файл застосунку
├── .gitignore
└── README.md
```

---

## Вимоги

- Python 3.10+
- pip

---

## Встановлення

```bash
# Клонувати репозиторій
git clone https://github.com/svniko/python-frameworks-2026.git
cd python-frameworks-2026

# Створити та активувати віртуальне середовище
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Встановити залежності
pip install flask               # встановити Flask
```

---

## Запуск

```bash
flask --app first run --debug
```

Після запуску відкрийте браузер за адресою: [http://localhost:5000](http://localhost:5000)







