from app import db 

class Compra(db.Model):
    __tablename__ = 'compra'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False )
    precio_total = db.Column(db.Float, nullable=False)
    proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id'))
    productos = db.relationship('Producto', secondary='compara_producto')
     