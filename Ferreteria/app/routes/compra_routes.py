from flask import Blueprint, render_template, request, redirect, url_for
from app.models.compra import Compra
from app.models.proveedor import Proveedor
from app.models.producto import Producto
from app import db

bp = Blueprint('compra', __name__)

@bp.route('/compra')
def index():
    data = Compra.query.all()
    return render_template('compras/index.html', data=data)

@bp.route('/compra/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fecha = request.form['fecha']
        precio_total = request.form['precio_total']
        proveedor_id = request.form['proveedor']  # Obtener ID del proveedor
        
        print(f"Fecha: {fecha}, Precio Total: {precio_total}, Proveedor ID: {proveedor_id}")


        newCompra = Compra(fecha=fecha, precio_total=precio_total, proveedor_id=proveedor_id)
        
        db.session.add(newCompra)
        db.session.commit()
        
        return redirect(url_for('compra.index'))
    
    data = Proveedor.query.all()
    datap = Producto.query.all()
    return render_template('compras/add.html', data=data, datap=datap)


@bp.route('/compra/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    compra = Compra.query.get_or_404(id)
    
    if request.method == 'POST':
        compra.fecha = request.form['fecha']
        compra.precio_total = request.form['precio_total']
        compra.proveedor_id = request.form['proveedor']
        
        db.session.commit()
        
        return redirect(url_for('compra.index'))
    
    datap = Proveedor.query.all()
    return render_template('compras/edit.html', compra=compra, datap=datap)

@bp.route('/compra/delete/<int:id>')
def delete(id):
    compra = Compra.query.get_or_404(id)

    db.session.delete(compra)
    db.session.commit()

    return redirect(url_for('compra.index'))
