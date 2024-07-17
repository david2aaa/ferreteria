from app import db 

class FacturaProducto(db.Model):
    __tablename__ = 'factura_producto'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.String(250), nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    facturas = db.Column(db.Integer, db.ForeignKey('factura.id'), primary_key = True)
    productos = db.Column(db.Integer, db.ForeingKey('producto.id'), primary_key = True)
    