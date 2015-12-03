from flask import Blueprint, render_template, request, make_response
from flask.views import MethodView
# from utils import fileSize

from bestperformancehit import app
from models import FileProvider
file_providers = Blueprint('file_providers', __name__, template_folder='templates')
from utils import Utils
class ListView(MethodView):

    def get(self):
        print("kon")
        file_providers = FileProvider.objects.all()
        print(len(file_providers))
        return render_template('providers.html', file_providers=file_providers)



@app.route('/addprovider')
def addprovider(name=None):
    print(Utils.downloadFile(FileProvider.objects(hostname="net23").get().filepath, 'downloaded_files'))
    return render_template('addprovider.html', name=name)

@app.route('/addprovider', methods=['POST'])
def addprovider_func(name=None):
    hostname = str(request.form['hostname']).strip()
    filepath = str(request.form['filepath']).strip()
    if not len(filepath) is 0 and not len(hostname) is 0:
        file_size = Utils.fileSize(filepath)
        FileProvider.add_new_file_provider(hostname, filepath, file_size)
    return make_response(render_template('provider_added.html'), 200)

# Register the urls
file_providers.add_url_rule('/', view_func=ListView.as_view('list'))
