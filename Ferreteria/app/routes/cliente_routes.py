from flask import Blueprint, render_template, request, redirect, url_for
from app.models.cliente import Cliente
from app import db

bp = Blueprint('cliente', __name__)

@bp.route('/cliente')
def index():
    data = Cliente.query.all()
    return render_template('clientes/index.html', data=data)

@bp.route('/Cliente/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        newCliente = Cliente(nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono)
        
        db.session.add(newCliente)
        db.session.commit()
        
        return redirect(url_for('cliente.index'))
    
    return render_template('clientes/add.html')

@bp.route('/Cliente/edit/<int:id>>', methods=['GET', 'POST'])
def edit(id):
    cliente = Cliente.query.get_or_404(id)
    
    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.apellido = request.form['apellido']
        cliente.direccion = request.form['direccion']
        cliente.telefono = request.form['telefono']
        
        db.session.commit()

        return redirect(url_for('cliente.index'))

    return render_template('clientes/edit.html', cliente=cliente)

@bp.route('/Cliente/delete/<int:id>')
def delete(id):
    cliente = Cliente.query.get_or_404(id)
    
    db.session.delete(cliente)
    db.session.commit()
    
    return redirect(url_for('cliente.index'))
