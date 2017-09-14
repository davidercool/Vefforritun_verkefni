from bottle import route, run, static_file, template
@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")
@route('/<steve>')
def steve(steve, tala=1):
    info={'css1':'href="./static/index.css"'}
    return template('temporaryplate', steve=steve, tala=tala, info=info)
run(host='localhost', port=8080, debug=True)
