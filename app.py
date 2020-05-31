from flask import Flask
from blue import blue

app = Flask(__name__)
app.register_blueprint(blue)