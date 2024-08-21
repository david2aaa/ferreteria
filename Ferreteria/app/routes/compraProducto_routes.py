from flask import Blueprint, render_template, request, redirect, url_for
from app.models.compra_producto import CompraProducto
from app.models.producto import Producto
from app.models.compra import Compra
from app import db

bp = Blueprint('compraProducto', __name__)

@bp.route('/CompraProducto')
def index():
    data = CompraProducto.query.all()
    pdata = Producto.query.all()
    cdata = Compra.query.all()

    return render_template('comprasProductos/index.html', data=data, pdata=pdata, cdata=cdata)

@bp.route('/addCompraProducto', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        producto = request.form['productos']
        compra = request.form['compras']
        cantidad = request.form['cantidad']

        newCompraProducto = CompraProducto(producto_id=producto, compra_id=compra,cantidad=cantidad)

        db.session.add(newCompraProducto)
        db.session.commit()

        return redirect(url_for('compraProducto.index'))

    pdata = Producto.query.all()
    cdata = Compra.query.all()
    return render_template('comprasProductos/add.html', pdata=pdata, cdata=cdata)

@bp.route('/editCompraProducto/<int:id>', methods=['GET', 'POST'])
def edit(id):   
    compraProducto = CompraProducto.query.get_or_404(id)

    if request.method == 'POST':
        compraProducto.producto = request.form['producto_id']
        compraProducto.compra = request.form['compra_id']
        compraProducto.cantidad = request.form['cantidad']

        db.session.commit()

        return redirect(url_for('compraProducto.index'))
    
    pdata = Producto.query.all()
    cdata = Compra.query.all()

    return render_template('comprasProductos/edit.html', compraProducto=compraProducto, pdata=pdata, cdata=cdata)

@bp.route('/deleteCompraProducto/<int:id>')
def delete(id):
    compraProducto = CompraProducto.query.get_or_404(id)

    db.session.delete(compraProducto)
    db.session.commit()

    return redirect(url_for('compraProducto.index'))
