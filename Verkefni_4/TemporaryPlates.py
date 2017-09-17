from Vefforritun_verkefni.bottle import route, run, static_file, template
@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")
@route('/<steve>')
def steve(steve, tala=1):
    info={'css':'./static/index.css', 'centerclass':'class="center"', 'headertext1':'Steve Jobs', 'headertext2':'Pictures', 'headertext3':'Biography', 'footertext1':'Þetta er hann Steve Jobs. Hann er algjör Steve', 'footertext3':'Þetta er mest-selda bók allra tíma, hún er með 11/10 á IBDb(Internet Book Database)', 'footertext2':'Þetta er falleg mynd af honum Steve Jobs. Þessi mynd var tekinn þegar hann fann upp myndavélina.', 'pic1':'./static/billyG.png', 'pic2':'./static/bill-g.jpg', 'pic3':'./static/billtheg.jpg'}
    return template('temporaryplate', steve=steve, tala=tala, info=info)
run(host='localhost', port=8080, debug=True)
