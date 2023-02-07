import subprocess
import time
import requests
import os
import shutil
from psutil import Process
from http import HTTPStatus
from features.steps.shoppinglist_proxy import request_get


def kill(proc_pid):
    process = Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

def wait_until_server_available():
    re_entry = 1
    code = 400
    while(code != HTTPStatus.OK.value and re_entry < 10):
        time.sleep(1)
        try:
            response = request_get('')
            code = response.status_code 
        except Exception:
            print("fail")
        
        print("re_entry =" + str(re_entry))
        re_entry+=1

def run_server():
    process = subprocess.Popen(
        ['python', 'manage.py', 'runserver'],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wait_until_server_available()
    return process

def remove_folder(folder):
     if(os.path.exists(folder)):
            shutil.rmtree(folder)

