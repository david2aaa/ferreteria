from app import db 

class Factura(db.Model):
    __tablename__ = 'factura'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    # Relaciones
    cliente = db.relationship('Cliente', back_populates='factura')
    producto = db.relationship('FacturaProducto', back_populates='factura')