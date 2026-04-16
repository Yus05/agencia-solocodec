import os
from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect


mail = Mail()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    
    # Intentamos obtener la clave del entorno
    key = os.environ.get('SECRET_KEY')

    # Si no existe la clave, lanzamos un error claro
    if not key:
        raise ValueError("No se encontró la variable de entorno 'SECRET_KEY'.")

    app.config.from_mapping(
        SECRET_KEY=key,
        
        # Configuracion de Flask-Mail (Cargada desde variables de entorno)
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
        MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    )
    
    mail.init_app(app)
    csrf.init_app(app)
    
    # Registro de Blueprints
    from . import pages
    app.register_blueprint(pages.bp)
    
    return app