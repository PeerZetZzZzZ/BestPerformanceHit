import datetime

from bestperformancehit import db


class FileDownload(db.Document):
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
    hostname = db.StringField(max_length=255, required=True)
    filepath = db.StringField(required=True)
    filesize = db.StringField(max_length=255, required=True)
    downloads = db.ListField(db.EmbeddedDocumentField('FileDownload'))

    # def get_absolute_url(self):
    #     return url_for('filedownload', kwargs={"slug": self.slug})
    #
    # def __unicode__(self):
    #     return self.filename

    meta = {
        'allow_inheritance': True,
        'ordering': ['-created_at']
    }