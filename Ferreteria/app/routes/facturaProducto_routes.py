from flask import Blueprint, render_template, request, redirect, url_for
from app.models.factura_producto import FacturaProducto
from app.models.producto import Producto
from app.models.factura import Factura
from app import db

bp = Blueprint('facturaProducto', __name__)

@bp.route('/FacturaProducto')
def index():
    data = FacturaProducto.query.all()
    pdata = Producto.query.all()
    fdata = Factura.query.all()

    return render_template('facturasProductos/index.html', data=data, pdata=pdata, fdata=fdata)

@bp.route('/addFacturaProducto', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        producto = request.form['producto']
        factura = request.form['factura']
        precio_unitario = request.form['precio_unitario']
        cantidad = request.form['cantidad']

        newFacturaProducto = FacturaProducto(producto_id=producto, factura_id=factura, precio_unitario=precio_unitario, cantidad=cantidad)

        db.session.add(newFacturaProducto)
        db.session.commit()

        return redirect(url_for('facturaProducto.index'))

    pdata = Producto.query.all()
    fdata = Factura.query.all()
    return render_template('facturasProductos/add.html', pdata=pdata, fdata=fdata)

@bp.route('/editFacturaProducto/<int:id>', methods=['GET', 'POST'])
def edit(id):
    facturaProducto = FacturaProducto.query.get_or_404(id)

    if request.method == 'POST':
        facturaProducto.producto_id = request.form['producto']
        facturaProducto.factura_id = request.form['factura']
        facturaProducto.precio_unitario = request.form['precio_unitario']
        facturaProducto.cantidad = request.form['cantidad']

        db.session.commit()

        return redirect(url_for('facturaProducto.index'))
    
    productos = Producto.query.all()
    facturas = Factura.query.all()

    return render_template('facturasProductos/edit.html', facturaProducto=facturaProducto, productos=productos, facturas=facturas)

@bp.route('/deleteFacturaProducto/<int:id>')
def delete(id):
    facturaProducto = FacturaProducto.query.get_or_404(id)

    db.session.delete(facturaProducto)
    db.session.commit()

    return redirect(url_for('facturaProducto.index'))
