from bottle import route, run, static_file
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
                <link href="./static/Untitled-4.css" type="text/css" rel="stylesheet">
            </head>
            <Body>
                <h1>Steve Jobs</h1>
                <img src="./static/billg.jpg">
            </Body>
        </HTML>
        """
    elif steve=='bio':
        return """
        <!DOCTYPE HTML>
        <HTML>
            <head>
                <link href="./static/Untitled-4.css" type="text/css" rel="stylesheet">
            </head>
            <Body>
                <h1>Steve Jobs</h1>
                <img src="./static/billg.jpg">
            </Body>
        </HTML>
        """
    elif steve == 'pics':
        return """
        <!DOCTYPE HTML>
        <HTML>
            <head>
                <link href="./static/Untitled-4.css" type="text/css" rel="stylesheet">
            </head>
            <Body>
                <h1>Steve Jobs</h1>
                <img src="./static/billg.jpg">
            </Body>
        </HTML>
        """
    else:
        return("ERROR 404 - PAGE NOT FOUND!")

run(host='localhost', port=8080, debug=True)
