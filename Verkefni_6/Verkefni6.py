from bottle import route, run, static_file, request
@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")
@route('/')
def steve():
    return  '''
<!DOCTYPE HTML>
<HTML>
    <head>
        <link href="./static/form.css" type="text/css" rel="stylesheet">
        <link href="./static/tablogo.com" rel="icon">
     </head>
    <Body>
        <title>sign up to my awesome website</title>
        <div class="dominosfont">
        <h1 class="dominosfont">Sign Up</h1>
        <form action="/form", method='POST'>
            Full name<br>
            <input type="text" name="name" required><br><br>
            Username<br>
            <input type="text" name="user" required><br><br>
            Password<br>
            <input type="password" name="passowrd" required><br><br>
            Address<br>
            <input type="text" name="home" required><br><br>
            Phone number<br>
            <input type="text" name="phone" pattern="[1-9]{7,300}" title="has to be at least 7 digits, no letters allowed" required><br><br>
            E-mail<br>
            <input type="email" name="email" type="email" required>
            <br><br>
        <a href="/form"><input type="submit"></a>
        <br><br><h4>* required</h4>
        </form>
        </div>
    </Body>
</HTML>
    '''

@route('/form', method='POST')
def domimoses():
    listi = []
    name = request.forms.get('name')
    username = request.forms.get('user')
    home = request.forms.get('home')
    phone = request.forms.get('phone')
    email = request.forms.get('email')
    listi.append(name)
    listi.append(username)
    listi.append(home)
    listi.append(phone)
    listi.append(email)
    return listi
run(host='localhost', port=8080, debug=True)
