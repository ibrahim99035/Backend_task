from turtle import title
from flask import Flask, render_template, url_for, request, redirect
from sqlalchemy import null
from App import app, db
from App.models import Book
from App.book import Add_Book
from App.search import PatientSearch
from App.update import Update_Book

import os
import secrets
from PIL import Image

def Save_Pic(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/covers', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

#routes
@app.route('/')
@app.route('/home', methods=('GET', 'POST'))
def index():
    no_books = True
    if Book.query.count() > 0:
        no_books = False

    #pagination
    page = request.args.get('page', 1, type=int)
    books = Book.query.order_by(Book.date_posted.desc()).paginate(page=page, per_page=5)

    searchForm = PatientSearch()
    done = False
    message = ''
    if searchForm.validate_on_submit:
        for book in books.items:
            done = True
            if book.title == searchForm.search.data:
                return redirect(url_for('book', book_id=book.id))
            else:
                message = 'No book found'

    return render_template('index.html', title = 'Home', no_books = no_books, books = books, form = searchForm, done = done, message = message)


@app.route('/new', methods=('GET', 'POST'))
def new():
    addBook = Add_Book()
    if addBook.validate_on_submit():
        record = Book(title=addBook.title.data, num_of_page=addBook.pages.data, author=addBook.author.data, cover=addBook.cover.data)
        if addBook.cover.data:
            pic_file = Save_Pic(addBook.cover.data)
            record.cover = pic_file
        
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addBook.html', title = 'Add a new book', form = addBook)

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book(book_id):
    book = Book.query.get_or_404(book_id)
    updateForm = Update_Book()
    if updateForm.validate_on_submit():
        book.title = updateForm.title.data
        book.author = updateForm.author.data
        book.num_of_page = updateForm.pages.data
        if updateForm.cover.data:
            pic_file = Save_Pic(updateForm.cover.data)
            book.cover = pic_file
        db.session.commit()
        return redirect(url_for('book', book_id=book.id))
        
    return render_template('book.html', title = book.title, book = book, form = updateForm)

@app.route('/book/<int:book_id>/delete', methods=['GET', 'POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/demo')
def demo():
    return render_template('demo.html', title = 'App Demo')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/plan')
def plan():
    return render_template('plan.html', title = 'Project Plan')

@app.route('/contacts')
def contact():
    return render_template('contacts.html', title = 'My Info')