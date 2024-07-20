from flask import Flask
from Server_VISIONA import visiona_bp

app = Flask(__name__)

# Registrar el blueprint de VISIONA
app.register_blueprint(visiona_bp)

if __name__ == '__main__':
    app.run(debug=True)