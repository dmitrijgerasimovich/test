from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Персональная страница</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }
        h1 { color: #333; }
        p { font-size: 18px; }
    </style>
</head>
<body>
    <h1>Добро пожаловать на мою персональную страницу!</h1>
    <p>Меня зовут {{ name }}.</p>
    <p>Это простое веб-приложение на Python с использованием Flask.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, name="Ваше имя")

if __name__ == '__main__':
    app.run(debug=True)
