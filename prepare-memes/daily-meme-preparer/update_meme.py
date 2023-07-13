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

def update_meme(count):
    url = 'http://3.83.27.88:8000/upload'
    payload = open(os.path.join(get_output_directory(), f'{count._count}.png'), 'rb')
    file = {'uploaded_file': payload}
    x = requests.post(url, verify=False, files=file)
    print(x.status_code)
    count.increment()


count = Count()
schedule.every(10).seconds.do(update_meme, count)

while True:
    schedule.run_pending()
