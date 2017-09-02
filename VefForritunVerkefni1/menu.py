from VefForritunVerkefni1.bottle import route, run

@route('/<id:int>')
def callback(id:id):
    if id == 1:
        return("gunnar")
    elif id == 2:
        return("daniel")
    elif id == 3:
        return("þórarinn")
    else:
        return("ERROR 404 - PAGE NOT FOUND!")

run(host='localhost', port=8080, debug=True)