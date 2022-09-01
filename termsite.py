from flask import Flask, render_template, request, redirect, session, url_for, abort
from turbo_flask import Turbo
from commands import Commands as c

app = Flask(__name__)
turbo = Turbo(app)

app.config.update(
    SECRET_KEY="os.environ['SECRET_KEY']",
    SESSION_COOKIE_SECURE=True,
    REMEMBER_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    REMEMBER_COOKIE_HTTPONLY=True
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if turbo.can_stream():
            command = request.form['command']
            if command.lower() == 'clear' or command.lower() == 'cls':
                return turbo.stream([
                    turbo.replace(content='<div id="clear"><div id="populate"></div></div>' , target='clear'),
                    turbo.replace(content='<p id="main_" style="display: inline-block; margin-top: 18px;">term@<span>site:$ ~</span></p>' , target='main_'),
                    turbo.replace(content='<form id="main-form" style="display: inline-block;width: calc(100% - 211px);" method="POST"> <input id="enter" style="margin: 0 0 0 -2px;width: 100%;" type="text" autofocus name="command" autocomplete="off"></form>' , target='main-form')
                    ])
            elif command.lower() == 'help':
                content = c.help(command)
            elif command.lower() == 'reload':
                return redirect(url_for('index'))
            elif command.lower() == 'github':
                content = c.github(command)
            elif command.lower() == 'about':
                content = c.about(command)
            elif command.lower() == 'whoami':
                content = c.whoami(command)
            elif command.lower() == '':
                content = c.empty()
            else:
                content = f'<p>term@<span>site:$ ~</span> <fore>{command}</fore></p><e><p>No such Command!</p><p style="margin-bottom: 17px" >Type \'help\' to see a list of available commands.</p></e>'
            return turbo.stream([
                turbo.append(content=content ,target='populate'),
                turbo.replace(content='<p id="main_" style="display: inline-block; margin-top: 0px;">term@<span>site:$ ~</span></p>' , target='main_'),
                turbo.replace(content='<form id="main-form" style="display: inline-block;width: calc(100% - 211px);" method="POST"> <input id="enter" style="margin: 0 0 0 -2px;width: 100%;" type="text" autofocus name="command" autocomplete="off"></form>' , target='main-form')
            ])


    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False , host="0.0.0.0")