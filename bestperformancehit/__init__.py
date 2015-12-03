from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_bestperformancehit"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
    print("siemka")
    app.run()

def register_blueprints(app):
    # Prevents circular imports
    from views import file_providers
    app.register_blueprint(file_providers)

register_blueprints(app)