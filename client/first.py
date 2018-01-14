from bottle import route,run,static_file,get,post,request,template
#from nwhacks2018.client.client_manager import ClientHelper
#from nwhacks2018.client.runClient import *

from client_manager import ClientHelper
from runClient import *

import os

dir_path1 = os.path.dirname(os.path.realpath(__file__))

foo = ClientHelper()
@get('/static/<filename>')
def static(filename):
    
    return static_file(filename, root=dir_path1)
@post('/log1/<filename>')
def do_update(filename): #update info is sent here
    update = request.forms.get('update')
    foo.set_update_frequency(update)
    return static_file(filename, root=dir_path1)

@post('/log2/<filename>')
def do_duration(filename): #duration info is sent here
    duration = request.forms.get('duration')
    foo.set_duration(duration)
    return static_file(filename, root=dir_path1)

@post('/log3/<filename>')
def do_threshold(filename): #threshold info is sent here
    threshold = request.forms.get('threshold')
    foo.set_emergency_threshold(threshold)
    return static_file(filename, root=dir_path1)

@post('/log4/<filename>')
def do_go(filename): #go button
    #start()
    return static_file(filename, root=dir_path1)

@post('/log5/<filename>')
def stop(filename): #stop button
    foo.end_execution()
    return static_file(filename, root=dir_path1)



run('localhost',8080)
