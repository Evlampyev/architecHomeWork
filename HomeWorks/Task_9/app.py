from collections import namedtuple
from book import Book
from book_case import BookCase
from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)
Message = namedtuple('Message', 'number')
messages = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books', methods=['GET'])
def get_tasks():
    """Получить список всех книг"""
    bks = books.get_books()  # получение списка всех книг из BookCase
    # context = (json.dumps(book.dump()) for book in bks)
    context = books.__str__()
    return render_template('back.html', context=context)


@app.route("/book", methods=['GET'])
def add_task():
    """Добавить книгу"""
    return render_template('add_book.html')


@app.route("/addBook", methods=['POST'])
def addBook():
    title = request.form["Title1"]
    author = request.form["Author"]
    year = request.form["Year"]
    pages = request.form["Pages"]
    book = Book(title, author, year, pages)
    books.__add__(book)
    return render_template("index.html")


@app.route('/book/<int:book_id>', methods=['GET'])
def get_task(book_id):
    for book in books.get_books():
        if book.id == int(book_id):
            itog = book

    context = itog.__str__()
    return render_template('back.html', context=context)


@app.route('/add_number', methods=['POST'])
def add_message():
    x = request.form['calc']

    return get_task(x)


@app.route("/forward/", methods=['POST'])
def move_forward():
    # Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=forward_message);


if __name__ == '__main__':
    books = BookCase()
    book1 = Book("Who are you", "Evlampyev A.V.", 1986, 111)
    book2 = Book("1984", "Petrov S.S.", 1900, 999)

    books.__add__(book2)
    books.__add__(book1)
    # print(books)

    app.run(debug=True)
