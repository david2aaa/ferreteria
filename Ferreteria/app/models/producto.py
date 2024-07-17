from app import db 

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.String(250), nullable=False)
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    facturas = db.relationship('Factura', secondary='factura_producto')
    compras = db.relationship('Compra', secundary='compra_producto')