from VefForritunVerkefni2.bottle import route, run, static_file, request
poks=["<h1 class='bottomtext'>Velkominn!</h1><br><h2 class='bottomtext2'>Ýttu á pokémon til að fá flavor textann.<h2>","<h1 class='bottomtext'>Bulbasaur</h1><br><h2 class='bottomtext2'>A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokemon.</h2>", "<h1 class='bottomtext'>Ditto</h1><br><h2 class='bottomtext2'>It can reconstitute its entire cellular structure to change into what it sees, but it returns to normal when it relaxes.</h2>","<h1 class='bottomtext'>Growlithe</h1><br><h2 class='bottomtext2'>Extremely loyal to its Trainer, it will bark at those who approach the Trainer unexpectedly and run them out of town.<h2>","<h1 class='bottomtext'>Metapod</h1><br><h2 class='bottomtext2'>A steel-hard shell protects its tender body. It quietly endures hardships while awaiting evolution.<h2>","<h1 class='bottomtext'>Mew</h1><br><h2 class='bottomtext2'>Because it can use all kinds of moves, many scientists believe Mew to be the ancestor of Pokemon.<h2>","<h1 class='bottomtext'>Pikachu</h1><br><h2 class='bottomtext2'>It lives in forests with others. It stores electricity in the pouches on its cheeks.<h2>","<h1 class='bottomtext'>Snorlax</h1><br><h2 class='bottomtext2'>When its belly is full, it becomes too lethargic to even lift a finger, so it is safe to bounce on its belly.<h2>","<h1 class='bottomtext'>Squirtle</h1><br><h2 class='bottomtext2'>It shelters itself in its shell then strikes back with spouts of water at every opportunity.<h2>","<h1 class='bottomtext'>Zapdos</h1><br><h2 class='bottomtext2'>This legendary bird Pokemon is said to appear when the sky turns dark and lightning showers down.<h2>","<h1 class='bottomtext'>Porygon</h1><br><h2 class='bottomtext2'>A man-made Pokemon created using advanced scientific means. It can move freely in cyberspace.<h2>"]
@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")
@route('/index')
def site():
    pok = 0 if not request.query.pok else int(request.query.pok)
    return '''
        <!DOCTYPE HTML>
        <HTML>
        <head>
            <link href="./static/pokemon.css" type="text/css" rel="stylesheet">
        </head>
        <Body>
        <div class="background-image"></div>
        <div class="content">
        <h1>Pokémon</h1>
        <div><center>
            <a href="/index?pok=1"><img src="./static/Bulbasaur.png" height="250" width="250"></a>
            <a href="/index?pok=2"><img src="./static/ditto.png" height="250" width="250"></a>
            <a href="/index?pok=3"><img src="./static/growlithe.png" height="250" width="250"></a>
            <a href="/index?pok=4"><img src="./static/metapod.png" height="250" width="250"></a>
            <a href="/index?pok=5"><img src="./static/mew.png" height="250" width="250"></a>
        </center></div>
        <div><center>
            <a href="/index?pok=6"><img src="./static/pikachu.png" height="250" width="250"></a>
            <a href="/index?pok=7"><img src="./static/snorlax.png" height="250" width="250"></a>
            <a href="/index?pok=8"><img src="./static/squirtle.png" height="250" width="250"></a>
            <a href="/index?pok=9"><img src="./static/Zapdos.png" height="250" width="250"></a>
            <a href="/index?pok=10"><img src="./static/porygon.png" height="250" width="250"></a>
        </center></div>'''+poks[pok]+'''</div>
        </Body>
    </HTML>
    '''

run(host='localhost', port=8080, debug=True)