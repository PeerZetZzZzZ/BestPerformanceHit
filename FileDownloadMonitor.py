import os

import time

import schedule

from models import FileProvider
from utils import Utils


class FileDownloadMonitor:
    def download_files():
        file_providers = FileProvider.objects
        my_current_path = os.getcwd()
        for file_provider in file_providers:
             hostname = file_provider.hostname
             host_directory = my_current_path + "/" + hostname
             if not os.path.exists(host_directory):
                 os.makedirs(host_directory)
             download_time = Utils.downloadFile(file_provider.filepath, host_directory)
             print(download_time)
        print('udalo sie!')

    def start_downloading_loop():
        print("zainicjalizowalem")
        schedule.every(10).seconds.do(FileDownloadMonitor.download_files())
        while True:
            schedule.run_pending()
            time.sleep(1)