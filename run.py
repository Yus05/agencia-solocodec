# import os
from dotenv import load_dotenv
from solocodecweb import create_app

# 1. Cargamos las variables de entorno (.env en local, Variables de Vercel en la nube)
load_dotenv()

# 2. CREAMOS LA APP AQUÍ (Fuera del if)
# Esto es lo que Vercel buscará para arrancar tu sitio
app = create_app()

if __name__ == '__main__':
    # Esto solo se ejecuta cuando tú escribes 'python run.py' en tu PC
    app.run(debug=True)