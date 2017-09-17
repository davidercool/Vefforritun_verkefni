from Vefforritun_verkefni.bottle import route, run, static_file, template
@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")
@route('/<news>')
def news(news):
    info = {'title0':'Steve Jobs saves the world!', 'punchline0':'People thought that the influential comedian who went to far with his jokes was gone, but he has actually been alive this entire time saving the world from all evil!', 'pic0':'./static/billyG.png', 'title1': 'Icelandic Government falls!', 'punchline1':'After lots of corruption the Icelandic government finally collapsed onto itself.', 'pic1':'./static/kongur.jpg', 'title2':'Lorem Ipsum is actually Greek for...', 'punchline2':'Researchers from Lannister University have been studying linguistics, and more specifically the meaning of the famous writings: \'Lorem ipsum\'.', 'pic2':'./static/LoremIpsum.jpeg', 'fulltext0':'People thought that the influential comedian who went to far with his jokes was gone, but he has actually been alive this entire time, saving the world from all evil!\n\n A bunch of mediums and ghost communicators reported strange activities around the grave of comedic mastermind Steve jobs. They contacted the police and since then tons of specialists have found weird things happening there. There is a strange magnetic field distorting the air and the new Iphone X TM (Buy now for only $999) was reportedly seen growing on nearby trees.\n\n We interviewed the Pope about the incident and he said \'Steve Jobs invented a way to become a demi-god after death and decided to use his powers to make the Earth immune to all evil for the rest of eternity.\'', 'fulltext1':'After lots of corruption the Icelandic government finally collapsed onto itself. Literally.\n The parliament building collapsed and is now being built. Government actions will go back to normal at the end of the week.', 'fulltext2':'Researchers from Lannister University have been studying linguistics, and more specifically the meaning of the famous writings: \'Lorem ipsum\'.\n\n They found traces of usage of the phrase in ancient Greek media outlets. The real meaning of the phrase is: Clickbait', 'link0':'art0', 'link1':'art1', 'link2':'art2'}
    if news == 'index':
        return template('newstemplate', tala=3, news=news, info=info, art=3)
    elif news == 'art0':
        return template('body2', art=0, news=news, info=info)
    elif news == 'art1':
        return template('body2', art=1, news=news, info=info)
    elif news == 'art2':
        return template('body2', art=2, news=news, info=info)
    else:
        return template('errortemplate')
run(host='localhost', port=8080, debug=True)
