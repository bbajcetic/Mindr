from bottle import route,run,static_file,get,post,request,template

@get('/static/<filename>')
def static(filename):
    return static_file(filename, root="/home/branko/nwhacks2018")
@post('/log')
def do_login():
    update = request.forms.get('update')
    return template('Update returned {{info}}',info=update)

run(host='localhost',port=8080)
