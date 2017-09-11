from VefForritunVerkefni2.bottle import route, run, static_file
@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")
@route('/<steve>')
def steve(steve):
    if steve=='steve':
        return """
        <!DOCTYPE HTML>
        <HTML>
            <head>
                <link href="./static/index.css" type="text/css" rel="stylesheet">
            </head>
            <Body>
                <div class="valmynd">
                    <a href="steve"><h2>SteveJobs</h2></a>
                    <a href="pics"><h2>Pictures</h2></a>
                    <a href="bio"><h2>Biography</h2></a>
                </div>
                <h1>Steve Jobs</h1>
                <center><img src="./static/billg.jpg" height="500" width="420"></center>
                <p>Þetta er hann Steve Jobs. Hann er algjör Steve</p>
            </Body>
        </HTML> 
        """
    elif steve=='bio':
        return """
        <!DOCTYPE HTML>
        <HTML>
            <head>
                <link href="./static/index.css" type="text/css" rel="stylesheet">
            </head>
            <Body>
                <div class="valmynd">
                    <a href="steve"><h2>SteveJobs</h2></a>
                    <a href="pics"><h2>Pictures</h2></a>
                    <a href="bio"><h2>Biography</h2></a>
                </div>
                <h1>Biography</h1>
                <center><img src="./static/billtheg.jpg" height="500" width="420"></center>
                <p>Þetta er mest-selda bók allra tíma, hún er með 11/10 á IBDb(Internet Book Database)</p>
            </Body>
        </HTML>
        """
    elif steve == 'pics':
        return """
        <!DOCTYPE HTML>
        <HTML>
            <head>
                <link href="./static/index.css" type="text/css" rel="stylesheet">
            </head>
            <Body>
                <div class="valmynd">
                    <a href="steve"><h2>SteveJobs</h2></a>
                    <a href="pics"><h2>Pictures</h2></a>
                    <a href="bio"><h2>Biography</h2></a>
                </div>
                <h1>Pictures</h1>
                <center><img src="./static/billyG.png" height="500" width="420"></center>
                <p>Þetta er falleg mynd af honum Steve Jobs. Þessi mynd var tekinn þegar hann fann upp myndavélina.</p>
            </Body>
        </HTML>
        """
    else:
        return("ERROR 404 - PAGE NOT FOUND!")

run(host='localhost', port=8080, debug=True)