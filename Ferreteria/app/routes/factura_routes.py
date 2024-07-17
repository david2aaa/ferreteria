from flask import Blueprint, render_template, request, redirect, url_for
from app.models.factura import Factura
from app.models.cliente import Cliente
from app import db

bp = Blueprint('factura', __name__)

@bp.route('/Factura')
def index():
    data = Factura.query.all()
    return render_template('/facturas/index.html', data=data)

@bp.route('/Factura/add', method=['GET','POST'])
def add():
    if request.method == 'POST':
        fecha = request.form['fecha']
        precio_total = request.form['precio_total']
        cliente = request.form['cliente']
        
        newFactura = Factura(fecha=fecha, precio_total=precio_total, cliente=cliente)
        
        db.session.add(newFactura)
        db.session.commit()
        
        return redirect(url_for('factura.index'))
    data = Cliente.query.all()
    return render_template('facturas/add.html', data=data)

@bp.route('/Factura/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    factura = Factura.query.get_or_404(id)
    
    if request.method == 'POST':
        factura.fecha = request.form['fecha']
        factura.precio_total = request.form['precio_total']