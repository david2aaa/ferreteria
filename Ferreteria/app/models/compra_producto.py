from app import db 

class CompraProducto(db.Model):
    __tablename__ = 'compra_producto'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.String(250), nullable=False)
    precio_unitario =db.Column(db.Float, nullable=False)
    compras = db.Column(db.Integer, db.ForeingKey('compra.id'))
    productos = db.Column(db.Integer, db.ForeignKey('producto.id'))