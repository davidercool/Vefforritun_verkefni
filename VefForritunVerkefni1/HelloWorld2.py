from VefForritunVerkefni1.bottle import route, run

@route('/HelloWorld')
def hello():
    with open('Helloworld.txt', 'r') as f:
        return f.read()

run(host='localhost', port=8080, debug=True)