import os
import threading
import time
from string import Formatter
from threading import Thread

import schedule
from utils import Utils

class FileDownloadMonitor(Thread):

    def run(self):
        schedule.every(30).seconds.do(download_files)
        while True:
            schedule.run_pending()
            time.sleep(1)

def download_files():
    from views import FileProvider
    file_providers = FileProvider.objects
    my_current_path = os.getcwd()
    for file_provider in file_providers:
        single_measurement = SingleMeasurement(file_provider, my_current_path)
        single_measurement.run()

class SingleMeasurement(Thread):
    file_provider = None
    my_current_path = None

    def __init__(self, file_provider, my_current_path):
        self.my_current_path = my_current_path
        self.file_provider = file_provider

    def run(self):
        from views import FileProvider
        from models import FileDownload
        hostname = self.file_provider.hostname
        print("Measuring time for hostname {}".format(hostname))
        host_directory = self.my_current_path + "/downloaded_files/" + hostname
        if not os.path.exists(host_directory):
            os.makedirs(host_directory)
        download_time = Utils.downloadFile(self.file_provider.filepath, host_directory)
        file_download = FileDownload(downloadtime=str(download_time))
        FileProvider.objects(hostname=hostname).update_one(push__downloads=file_download)
        print("Time for hostname {} measured with value {}".format(hostname, file_download))