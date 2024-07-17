from app import db 

class Factura(db.Model):
    __tablename__ = 'factura'
    id = db.Column(db.integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    cliente = db.Column(db.Integer, db.ForeingKey('cliente.id'))
    productos = db.relationship('Producto', secondary='factura_producto')
    
