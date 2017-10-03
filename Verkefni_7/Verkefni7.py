from bottle import route, run, request, response, template

def check_login(a, b):
    if a.lower() == 'david' and b.lower() == 'password':
        return True
    else:
        return False

@route('/')
def login():
    return template('form.tpl')
username = request.forms.get('user')
password = request.forms.get('pass')
@route('/login', method="POST")
def do_login():
    username = request.forms.get('user')
    password = request.forms.get('pass')
    if check_login(username,password):
        response.set_cookie("account", username, secret='password')
        return "<p>Welcome! You are now logged in.</p><a href='/logout'><input type='submit' value='logout'></a>"
    else:
        return "<p>Login failed.</p>"+template('form.tpl')

@route('/logout')
def logout():
    response.set_cookie("account", "", expires=0)
    return '<p>You have been logged out</p>'
run(host='localhost', port=8080, debug=True)