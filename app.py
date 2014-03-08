#coding: utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",)


@app.route('/reg.html')
def reg():
    error = ''
    result = ''
    if request.method == 'GET':
        email = request.args.get("mail", "").strip()
        jelszo = request.args.get("pass", "").strip()
        vnev = request.args.get("vnev", "").strip()
        knev = request.args.get("knev", "").strip()

    if len(email) > 0 or len(jelszo) > 0 or len(vnev) > 0 or len(knev) > 0:
        if len(email) == 0:
            return render_template('reg.html', error=u', az email mező nem lehet üres!')
        elif len(jelszo) == 0:
            return render_template('reg.html', error=u', a jelszó mező nem lehet üres!')
        elif len(vnev) == 0:
            return render_template('reg.html', error=u', a vezetéknév mező nem lehet üres!')
        elif len(knev) == 0:
            return render_template('reg.html', error=u', a keresztnév mező nem lehet üres!')
        else:
            result = u'Siker'

            if result == u'Siker':
		        return render_template('reg.html', success=True)
            elif result == u'Hiba':
		        return render_template('reg.html', error=u', már regisztráltál!')
            else:
                pass
    else:
        return render_template("reg.html",)
    print email+jelszo+vnev+knev


if __name__ == '__main__':
    app.run(debug=True)