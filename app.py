from flask import Flask, request, render_template

from books.books import books_bp
app = Flask(__name__)
app.register_blueprint(books_bp, url_prefix='/book')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
