from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
load_dotenv()
import os

from db_scripts import DataBaseManager

app = Flask(__name__) # Створюємо веб–додаток Flask
app.secret_key = os.getenv('SECRET_KEY')
db = DataBaseManager("menu.db")

IMG_PATH = os.path.dirname(__file__) + os.sep + 'static' + os.sep + 'img' + os.sep


@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    items = db.get_all_items()
    return render_template('index.html', items=items) #Результат, що повертається у браузер

@app.context_processor
def get_categories():
    categories = db.get_all_categories()
    return dict(categories=categories)

@app.route("/items/<int:item_id>")
def item_page(item_id):
    item = db.get_item(item_id)
    return render_template("item_page.html", item = item)
    
@app.route("/categories/<int:category_id>")  # Вказуємо url-адресу для виклику функції
def category_page(category_id):
    items = db.get_category_items(category_id)
    return render_template("index.html", items=items)  # html-сторінка, що повертається у браузер

@app.route("/search") # Вказуємо url-адресу для виклику функції
def search():
    items = db.get_all_items()
    if request.method == 'GET':
        query = request.args.get('query')
        items = db.search_item(query)
    return render_template('index.html', items=items) #Результат, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу