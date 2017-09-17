%include('header.tpl')
        <div class="flexbox">
            <div class="margin"><img src="{{info['pic'+str(art)]}}" height="200" width="200"></div>
            <div class="minusmargin">
                <h1>{{info['title'+str(art)]}}</h1>
                <p>{{info['fulltext'+str(art)]}}</p>
            </div>
        </div>
%include('footer.tpl')