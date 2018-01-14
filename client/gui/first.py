from bottle import route,run,static_file,get,post,request,template
from nwhacks2018.client.client_manager import ClientHelper
import os

dir_path1 = os.path.dirname(os.path.realpath(__file__))

foo = ClientHelper()
@get('/static/<filename>')
def static(filename):
    gfilename = filename
    return static_file(filename, root=dir_path1)
@post('/log1/<filename>')
def do_update(filename): #update info is sent here
    update = request.forms.get('update')
    foo.set_update_frequency(update)
    return static_file(filename, root= dir_path1)

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

run(host='localhost',port=8080)
