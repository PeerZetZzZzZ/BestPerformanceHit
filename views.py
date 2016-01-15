import json

from flask import Blueprint, render_template, request, make_response, url_for
from flask.views import MethodView
# from utils import fileSize
from werkzeug.utils import redirect

from DistanceCounter import DistanceCounter
from FileDownloadMonitor import FileDownloadMonitor
from bestperformancehit35 import app
from models import FileProvider, SystemConfiguration

file_providers = Blueprint('file_providers', __name__, template_folder='templates')
from utils import Utils
class ListView(MethodView):

    def get(self):
        file_providers = FileProvider.objects.all()
        return render_template('providers.html', file_providers=file_providers)

@app.route('/addprovider')
def addprovider(name=None):
    return render_template('addprovider.html', name=name)

@app.route('/filedownloadinterval')
def filedownloadinterval(name=None):
    SystemConfiguration.save_download_interval(5)
    return render_template('file_download_interval.html', name=name)

@app.route('/filedownloadinterval', methods=['POST'])
def filedownloadinterval_change(name=None):
    received_data_as_json = json.loads(request.data.decode())
    file_download_interval = received_data_as_json['file_download_interval']
    print("Received file_download_interval change: " + file_download_interval)
    return make_response(render_template('file_download_interval.html'), 200)

@app.route('/addprovider', methods=['POST'])
def addprovider_func(name=None):
    hostname = str(request.form['hostname']).strip()
    filepath = str(request.form['filepath']).strip()
    if not len(filepath) is 0 and not len(hostname) is 0:
        file_size = Utils.fileSize(filepath)
        FileProvider.add_new_file_provider(hostname, filepath, file_size)
    return make_response(render_template('provider_added.html'), 200)

# Received data e.g. {'hostname':'hostname123'}
# Since hostname is unique in DB it's enough
@app.route('/removeprovider', methods=['POST'])
def removeprovider_func(name=None):
    received_data_as_json = json.loads(request.data.decode())
    hostname_to_remove = received_data_as_json['hostname']
    FileProvider.remove_provider(hostname_to_remove)
    print("Provider with hostname {} has been removed with all history!".format(hostname_to_remove))
    return redirect(url_for('addprovider'))

@app.route('/client')
def render_client(name=None):
    return make_response(render_template('performance_hit_client/client.html'), 200)

# Received data e.g. {'resources_list':['www.google.pl/file1.mp3']}
@app.route('/test', methods=['POST'])
def addprovider_func2(name=None):
    received_data = json.loads(request.data.decode())
    # geo_local = GeoLocal(list=list, host=host)
    print("mam zwrotke od geo local")

    file_providers = FileProvider.objects
    resources_list = received_data['resources_list']
    d = DistanceCounter()
    d.find_winner(resources_list)


    return make_response("{\"winner\":\"http://www.bestperformancehit.net23.net/1szum.mp3\"}", 200)

@app.before_first_request
def start_download_services():
    file_download_interval = SystemConfiguration.get_save_download_interval()
    print("Start download services with file download interval in minutes: ")
    print(file_download_interval)
    file_download_monitor = FileDownloadMonitor(file_download_interval)
    file_download_monitor.start()

# Register the urls
file_providers.add_url_rule('/', view_func=ListView.as_view('list'))
