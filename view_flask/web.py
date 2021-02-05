import sys
sys.path.append('.')

from flask import Flask, render_template, redirect, request
from controllers.category_controller import CategoryController
from models.category import Category

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def menu():
    return render_template('index.html')

category_controller = CategoryController()


@app.route('/create_category')
def new_category():
    return render_template('create_category.html', title='Nova Categoria')


@app.route('/categories', methods=['GET', 'POST'])
def list_category():
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        category = Category(name, desc)
        category_controller.create(category)
    categories = category_controller.read_all()
    return render_template('list_category.html', title='Categories', list=categories)


@app.route('/categories/<int:id>', methods=['GET', 'POST'])
def edit_category(id: int):
    if request.method == "POST":
        category_update = category_controller.read_by_id(id)
        name = request.form.get('name')
        desc = request.form.get('description')
        category_update.name = name
        category_update.description = desc
        category_controller.update(category_update)
        return redirect('/categories')
    category = category_controller.read_by_id(id)
    return render_template('edit_category.html', title='Category', object=category)


@app.route('/categories/<int:id>/delete', methods=['GET'])
def erase_category(id: int):
    obj = category_controller.read_by_id(id)
    category_controller.delete(obj)
    return redirect('/categories')


app.run(debug=True)