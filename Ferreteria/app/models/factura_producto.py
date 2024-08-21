from app import db 

class FacturaProducto(db.Model):
    __tablename__ = 'factura_producto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    precio_unitario = db.Column(db.Float, nullable=False)
    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'), primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), primary_key=True)
    cantidad = db.Column(db.String(250), nullable=False)

    # Relaciones
    factura = db.relationship('Factura', back_populates='producto')
    producto = db.relationship('Producto', back_populates='factura')