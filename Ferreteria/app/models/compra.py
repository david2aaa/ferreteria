from app import db 

class Compra(db.Model):
    __tablename__ = 'compra'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'))

    # Relaciones
    proveedor = db.relationship('Proveedor', back_populates='compra')
    producto = db.relationship('CompraProducto', back_populates='compra')   