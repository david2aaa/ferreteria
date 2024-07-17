from flask import Blueprint, render_template, request, redirect, url_for
from app.models.categoria import Categoria
from app import db

bp = Blueprint('categoria', __name__)

@bp.route('/Student')
def index():
    data = Categoria.query.all()
    return render_template('clientes/index.html', data=data)

@bp.route('/Categoria/add', method=['GET','POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        
        newCategoria = Categoria(nombre=nombre)
        
        db.session.add(newCategoria)
        db.session.commit()
        
        return redirect(url_for('categoria.index'))
    
    return render_template('clientes/add.html')

@bp.route('/Cliente/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    categoria = Categoria.query.get_or_404(id)
    
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        
        db.session.commit()
        
        return redirect(url_for('categoria.index'))
    
    return render_template('categorias/edit.html', categoria=categoria)

@bp.route('/Cliente/delete/<int:id>')
def delete(id):
    categoria = Categoria.query.get_or_404(id)

    db.session.delete(categoria)
    db.session.commit()

    return redirect(url_for('categoria.index'))