import pymysql
conn = pymysql.connect(host='tsuts.tskoli.is', user='2201002860', passwd='mypassword', db='2201002860_vef2Verk11')

from bottle import route, run, request, response, template

def check_login(a, b):
    if a.lower() == 'david' and b.lower() == 'password':
        return True
    else:
        return False
@route('/')
def login():
    return template('login.tpl')
username = request.forms.get('user')
password = request.forms.get('pass')
@route('/login', method="POST")
def do_login():
    username = request.forms.get('user')
    password = request.forms.get('pass')
    if check_login(username,password):
        response.set_cookie("account", username, secret='password')
        return "<p>Welcome! You are now logged in.</p><a href='/logout'><input type='submit' value='logout'></a><a href='/database'><input type='submit' value='Database'></a>"
    else:
        return "<p>Login failed.</p>"+template('login.tpl')

@route('/database')
def velkominn():
    username = request.get_cookie("account", secret='password')
    if username:
        return template('choice.tpl')
    else:
        return "Þú ert ekki skráður inn."

@route('/search')
def velkominn():
    username = request.get_cookie("account", secret='password')
    if username:
        return "<center><h1>Search Bar</h1><input type='SearchBar' name='search' required><a href='/search/'><input type='submit' value='Search'></a></center>"
    else:
        return "Þú ert ekki skráður inn."

@route('/search/')
def velkominn():
    username = request.get_cookie("account", secret='password')
    if username:
        search = request.forms.get("search")
        result = conn.cursor()
        listi = result.execute("SELECT * FROM bilar where skraningarnumer = '{}';".format(search))
        result.close()
        return listi
        #return "<center><h1>ERROR 404 Nothing with this name is in our database</h1></center>"
    else:
        return "Þú ert ekki skráður inn."

@route('/edit')
def velkominn():
    username = request.get_cookie("account", secret='password')
    if username:
        return template('form.tpl')
    else:
        return "Þú ert ekki skráður inn."

@route('/add')
def velkominn():
    username = request.get_cookie("account", secret='password')
    if username:
        return template('choice.tpl')
    else:
        return "Þú ert ekki skráður inn."

@route('/logout')
def logout():
    response.set_cookie("account", "", expires=0)
    return '<p>You have been logged out</p>'
run(host='localhost', port=8080, debug=True)