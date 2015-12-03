import os

import requests
import time

class Utils:
    def downloadFile(url, directory) :
      localFilename = url.split('/')[-1]
      r = requests.get(url, stream=True)

      start = time.clock()
      f = open(directory + '/' + localFilename, 'wb')
      for chunk in r.iter_content(chunk_size = 512 * 1024) :
            if chunk :
                  f.write(chunk)
                  f.flush()
                  os.fsync(f.fileno())
      f.close()
      return (time.clock() - start)

    def fileSize(url):
        response = requests.head(url)
        print("mam content length")
        print(response.headers.get('content-lenght'))