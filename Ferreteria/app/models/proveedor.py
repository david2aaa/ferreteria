from app import db

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    direccion = db.Column(db.Sring(250), nullable=False)
    telefono = db.Column(db.Srting(250), nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    

    