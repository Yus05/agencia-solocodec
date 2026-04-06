import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Intentamos obtener la clave del entorno
    key = os.environ.get('SECRET_KEY')

    # Si no existe la clave, lanzamos un error claro
    if not key:
        raise ValueError("No se encontró la variable de entorno 'SECRET_KEY'.")

    app.config.from_mapping(
        SECRET_KEY=key,
        # Aquí puedes añadir más configuraciones luego
    )
    
    # Registro de Blueprints
    from . import pages
    app.register_blueprint(pages.bp)
    
    return app