from VefForritunVerkefni1.bottle import route, run

@route('/hello')
def hi():
    return("Hello World!")

run(host='localhost', port=8080, debug=True)