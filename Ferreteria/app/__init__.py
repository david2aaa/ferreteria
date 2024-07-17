from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)


    from app.routes import cliente_routes, provedor_routes, categoria_routes, producto_routes, factura_routes
    app.register_blueprint(cliente_routes.bp)
    app.register_blueprint(provedor_routes.bp)
    app.register_blueprint(categoria_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(factura_routes.bp)
    return app