%    if steve=='steve': tala = 1
%    elif steve=='bio': tala = 3
%    elif steve == 'pics': tala = 2
%   end
        <!DOCTYPE HTML>
        <HTML>
            <head>
                <link href="{{info["css"]}}" type="text/css" rel="stylesheet">
            </head>
            <Body>
                <div class="valmynd">
                    <a href="steve"><h2>SteveJobs</h2></a>
                    <a href="pics"><h2>Pictures</h2></a>
                    <a href="bio"><h2>Biography</h2></a>
                </div>
                <h1>{{info["headertext"+str(tala)]}}</h1>
                <div class="center"><img src="{{info["pic"+str(tala)]}}" height="500" width="420"></div>
                <p>{{info["footertext"+str(tala)]}}</p>
            </Body>
        </HTML>
