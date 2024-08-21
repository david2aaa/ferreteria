from app import db 

class CompraProducto(db.Model):
    __tablename__ = 'compra_producto'
    id = db.Column(db.Integer, primary_key =True, autoincrement=True)
    compra_id = db.Column(db.Integer, db.ForeignKey('compra.id'), primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), primary_key=True)
    cantidad = db.Column(db.String(250), nullable=False)

    # Relaciones
    compra = db.relationship('Compra', back_populates='producto')
    producto = db.relationship('Producto', back_populates='compra')
