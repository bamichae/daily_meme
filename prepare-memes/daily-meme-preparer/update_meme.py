import os
import pathlib
import threading

import requests as requests
import schedule
import time


class Count(object):
    def __init__(self):
        self._count = 0

    def increment(self):
        count = self._count
        self._count += 1
        return str(count)

def get_this_directory():
    return pathlib.Path(__file__).parent.resolve()


def get_output_directory():
    this_directory = get_this_directory()
    return os.path.join(this_directory, 'output')

def update_meme(count, url):
    url = f'{url}/upload'
    payload = open(os.path.join(get_output_directory(), f'{count._count}.png'), 'rb')
    file = {'uploaded_file': payload}
    x = requests.post(url, verify=False, files=file)
    print(x.status_code)
    count.increment()


count = Count()
url = '127.0.0.1:8000'
schedule.every(10).seconds.do(update_meme, count, url)

while True:
    schedule.run_pending()
