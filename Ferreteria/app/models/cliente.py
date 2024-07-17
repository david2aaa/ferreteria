from app import db 

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    apellido = db.Column(db.String(250), nullable=False)
    telefono = db.Column(db.String(250), nullable=False)
    direccion = db.Column(db.String(250), nullable=False) 