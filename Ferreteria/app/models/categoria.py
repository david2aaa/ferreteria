from app import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)

    # Relaciones
    producto = db.relationship('Producto', back_populates='categoria')
