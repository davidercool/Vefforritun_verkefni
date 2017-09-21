from bottle import route, run, static_file, request, post
@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")
@route('/')
def dominose():
    return '''
        <!DOCTYPE HTML>
        <HTML>
            <head>
                <link href="./static/form.css" type="text/css" rel="stylesheet">
                <link href="./static/tablogo.com" rel="icon">
             </head>
            <Body>
                <title>Dominose Pizas 5812346</title>
                <div class="dominosfont">
                <h1 class="dominosfont">Dominose Piza</h1>
                <form action="/form", method='POST'>
                    First name:<br>
                    <input type="text" name="name" required><br><br>
                    Heimilisfang:<br>
                    <input type="text" name="heimili" required><br><br>
                    Símanúmer:<br>
                    <input type="text" name="simi" pattern="[1-9]{7,300}" title="Þarf að vera minnst 7 tölustafir" required><br><br>
                    E-mail:<br>
                    <input type="email" name="email" type="email">
                    <br><br>
                    <h2>Veldu stærð:</h2>
                    <input type="radio" name="Size" value="1500" checked> Small - 1500kr<br>
                    <input type="radio" name="Size" value="2000"> Medium - 2000kr<br>
                    <input type="radio" name="Size" value="4000"> Large - 4000kr (BESTA VALUE)</input><br><br>
                    <h2>Veldu Álegg: 200 kr stykkið</h2>
                    <input type="checkbox" name="alegg" value="200">Pepperoni<br>
                    <input type="checkbox" name="alegg1" value="200">Skinka<br>
                    <input type="checkbox" name="alegg2" value="200">Hakk<br><br><br>
                <a href="/form"><input type="submit"></a>
                </form>
                </div>
            </Body>
        </HTML>
        '''

@route('/form', method='POST')
def domimoses():
    listi = []
    alegg = request.forms.get('alegg')
    alegg1 = request.forms.get('alegg')
    alegg2 = request.forms.get('alegg')
    numer = request.forms.get('simi')
    heimili = request.forms.get('heimili')
    nafn = request.forms.get('name')
    email = request.forms.get('email')
    listi.append(int(alegg1))
    listi.append(int(alegg2))
    listi.append(int(alegg))
    listi = filter(None, listi)
    aleggverd = sum(listi)
    sizeprice=request.forms.get('Size')
    summa=int(sizeprice)+int(aleggverd)
    virdisauki=summa*1.25
    return 'Heildarverð pöntuninnar er: '+str(summa)+'<br><br>Eftir virðisaukaskatt er verðið: '+str(virdisauki)+'<br><br>Staðfesting á pöntun hefur verið sent á Símanumerið: '+numer+' og emailið: '+email+'<br><br>pöntuninn verður kominn á heimilisfangið '+heimili+' eftir 15 mín!'
run(host='localhost', port=8080, debug=True)