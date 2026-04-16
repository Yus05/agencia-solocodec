from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect

from solocodecweb.forms import ContactForm
from solocodecweb import mail

bp = Blueprint('pages', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


# Vistas Servicios-------------------------------
@bp.route('/servicios')
def servicios():
    return render_template('servicios.html')

@bp.route('/servicios/diseno-&-desarrollo-web')
def servicio_diseno():
    return render_template('diseno-&-desarrollo-web.html')

@bp.route('/servicios/desarrollo-aplicaciones-web')
def servicio_desarrollo():
    return render_template('desarrollo-aplicaciones-web.html')

@bp.route('/servicios/automatizaciones-ia')
def servicio_automatizaciones():
    return render_template('automatizaciones-ia.html')

@bp.route('/servicios/mantenimiento-&-soporte')
def servicio_mantenimiento():
    return render_template('mantenimiento-&-soporte.html')
# Fin Vistas Servicios----------------------------


# Vistas Proyectos----------------------------------
@bp.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@bp.route('/proyectos/agencia-diseno-web')
def proyecto_agencia():
    return render_template('agencia-diseno-web.html')

@bp.route('/proyectos/agencia-web-por-subscripcion')
def proyecto_subscripcion():
    return render_template('agencia-web-por-subscripcion.html')

@bp.route('/proyectos/api-medi-schedule')
def proyecto_api():
    return render_template('api-medi-schedule.html')

@bp.route('/proyectos/crm-freelancers')
def proyecto_crm():
    return render_template('crm-freelancers.html')
# Fin Vistas Proyectos-------------------------------


# Vista Contacto-------------------------------------
@bp.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    
    if form.validate_on_submit():
        # 1. Extraer los datos del formulario ya validados
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message_body = form.message.data
        
        #2. Crear el objeto del mensaje
        msg = Message(subject=f"NUEVO MENSAJE SOLOCODEC: {subject}",
                      sender=current_app.config['MAIL_USERNAME'],
                      recipients=['ysomaza@gmail.com'])
        
        # 3. Cuerpo del correo
        msg.body = f""" 
        Has recibido un nuevo mensaje de contacto:
        
        Nombre: {name}
        Correo de contacto: {email}
        Asunto: {subject}
        
        Mensaje:
        {message_body}
        """
        
        # 4. Enviar el correo
        try:
            mail.send(msg)
            flash('¡Gracias por contactarnos! Tu mensaje ha sido enviado con éxito.', 'success')
        except Exception as e:
            flash(f'Ocurrió un error al enviar el mensaje: {str(e)}', 'danger')
            
        return redirect(url_for('pages.contacto'))
    
    
    return render_template('contacto.html', form=form)
# Fin Vista Contacto


# Vistas Legales---------------------
@bp.route('/politica-de-privacidad')
def politica_privacidad():
    return render_template('politica-de-privacidad.html')

@bp.route('/aviso-legal')
def aviso_legal():
    return render_template('aviso-legal.html')

@bp.route('/error-404')
def error_404():
    return render_template('error-404.html')
# Fin Vistas Legales----------------

