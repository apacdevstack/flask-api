"""Flask API Application Entrypoint file"""

import os
from apiapp import create_app

# application is exported so that WSGI servers like gunicorn can
# access it
application = create_app()

# Following block allows running using python interpreter during
# developement 
if __name__ == "__main__":
    HOST = os.environ.get("APP_HOST", "127.0.0.1")
    PORT = os.environ.get("APP_PORT", 8080)
    application.run(host=HOST, port=PORT)
