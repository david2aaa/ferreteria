from app import db

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    direccion = db.Column(db.String(250), nullable=False)
    telefono = db.Column(db.String(250), nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    
    compra = db.relationship("Compra", back_populates="proveedor")

    