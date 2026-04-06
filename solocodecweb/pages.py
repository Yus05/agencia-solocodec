from flask import Blueprint, render_template

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


@bp.route('/contacto')
def contacto():
    return render_template('contacto.html')


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

