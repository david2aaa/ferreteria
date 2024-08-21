from flask import Blueprint, render_template, request, redirect, url_for
from app.models.producto import Producto
from app.models.categoria import Categoria
from app import db

bp = Blueprint('producto', __name__)

@bp.route('/Producto')
def index():
    query = request.args.get('query')
    if query:
        data = Producto.query.filter(Producto.nombre.ilike(f'%{query}%')).all()
    else:
        data = Producto.query.all()
    return render_template('productos/index.html', data=data)

@bp.route('/Producto/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria = request.form['categoria']
        
        newProducto = Producto(nombre=nombre, precio=precio, stock=stock, categoria_id=categoria)
        
        db.session.add(newProducto)
        db.session.commit()
        
        return redirect(url_for('producto.index'))
    data = Categoria.query.all()
    return render_template('productos/add.html', data=data)

@bp.route('/Producto/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = float(request.form['precio'])
        producto.stock = request.form['stock']
        producto.categoria_id = request.form['categoria']
        
        db.session.commit()

        return redirect(url_for('producto.index'))

    return render_template('productos/edit.html', producto=producto)

@bp.route('/Producto/delete/<int:id>')
def delete(id):
    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('producto.index'))
