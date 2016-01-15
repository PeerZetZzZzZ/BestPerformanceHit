import datetime

from bestperformancehit35 import db


class FileDownload(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    downloadtime = db.StringField(required=True)

    # def get_absolute_url(self):
    #     return url_for('filedownload', kwargs={"slug": self.slug})
    #
    # def __unicode__(self):
    #     return self.filename

    meta = {
        'allow_inheritance': True,
        'ordering': ['-created_at']
    }

class FileProvider(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    hostname = db.StringField(max_length=255, required=True, unique=True)
    filepath = db.StringField(required=True, unique=True)
    filesize = db.StringField(max_length=255, required=True)
    downloads = db.ListField(db.EmbeddedDocumentField(FileDownload))

    def add_new_file_provider(hostname, filepath, filesize):
        file_provider = FileProvider(hostname=hostname, filepath=filepath, filesize=str(filesize))
        file_provider.save()
        # FileProvider.objects(hostname="net23").delete()

    def remove_provider(hostname):
        FileProvider.objects(hostname=hostname).delete()

    def get_average_download_time(self):
        total_time = 0.0
        counter = 0
        for download in self.downloads:
            total_time += float(download.downloadtime)
            counter += 1
        if counter > 0:
            return round(total_time/counter, 4)
        return 0

    def get_downloads_counter(self):
        return len(self.downloads)

    meta = {
        'allow_inheritance': True,
        'ordering': ['-created_at']
    }

class SystemConfiguration(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    download_interval = db.IntField()

    def save_download_interval(download_interval):
        if SystemConfiguration.objects.count() == 1:
            if download_interval > 1 and download_interval <= 60:
             SystemConfiguration.objects(0).update_one(download_interval=download_interval)
        else:
            system_configuration_singleton = SystemConfiguration(download_interval=download_interval)
            system_configuration_singleton.save()

    def get_save_download_interval(*args):
         configurations = SystemConfiguration.objects.all()
         for configuration in configurations:
            return configuration.download_interval