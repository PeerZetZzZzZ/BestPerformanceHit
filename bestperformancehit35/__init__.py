from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from FileDownloadMonitor import FileDownloadMonitor

app = Flask(__name__, static_url_path='')
app.config["MONGODB_SETTINGS"] = {'DB': "my_bestperformancehit"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

if __name__ == '__main__':
    app.run()

def register_blueprints(app):
    # Prevents circular imports
    from views import file_providers
    app.register_blueprint(file_providers)

register_blueprints(app)