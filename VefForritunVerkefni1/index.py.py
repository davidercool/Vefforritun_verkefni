from VefForritunVerkefni1.bottle import route, run

@route('/index')
def mainsida():
    return("<a href=\"/SteveJobs\">Steve Jobs</a><br><a href=\"/Biography\">Biography</a><br><a href=\"/Pictures\">Pictures</a>")

@route('/SteveJobs')
def stevenjobbes():
    return("Welcome to Steve Jobs's homepage! It is very cool and has much info")

@route('/Biography')
def stevenjobbes():
    return("Hello this my biography. I born I do some stuff and then I die goodbye.")

@route('/Pictures')
def stevenjobbes():
    return("Cool picture.")
run(host='localhost', port=8080, debug=True)