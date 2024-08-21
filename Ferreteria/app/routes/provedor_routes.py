from flask import Blueprint, render_template, request, redirect, url_for
from app.models.proveedor import Proveedor
from app import db

bp = Blueprint('proveedor', __name__)

@bp.route('/proveedor')
def index():
    data = Proveedor.query.all()
    return render_template('proveedor/index.html', data=data)

@bp.route('/proveedor/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['correo']
        
        newProveedor = Proveedor(nombre=nombre, direccion=direccion, telefono=telefono, correo=correo)
        
        db.session.add(newProveedor)
        db.session.commit()
        
        return redirect(url_for('proveedor.index'))
    
    return render_template('proveedor/add.html')

@bp.route('/proveedor/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.direccion = request.form['direccion']
        proveedor.telefono = request.form['telefono']
        proveedor.correo = request.form['correo']
        
        db.session.commit()

        return redirect(url_for('proveedor.index'))

    return render_template('proveedor/edit.html', proveedor=proveedor)

@bp.route('/proveedor/delete/<int:id>')
def delete(id):
    proveedor = Proveedor.query.get_or_404(id)

    db.session.delete(proveedor)
    db.session.commit()

    return redirect(url_for('proveedor.index'))
