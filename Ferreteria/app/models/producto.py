from app import db

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.String(250), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    # Relaciones
    categoria = db.relationship('Categoria', back_populates='producto')
    factura = db.relationship('FacturaProducto', back_populates='producto')
    compra = db.relationship('CompraProducto', back_populates='producto')
