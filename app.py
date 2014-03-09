#coding: utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1


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

@app.route('/about.html')
def about():
    sumSessionCounter()
    return render_template('about.html')

@app.route('/form')
def form():
  sumSessionCounter()
  # if a name has been sent, store it on a session variable
  if request.args.get('yourname'):
    session['name'] = request.args.get('yourname')
    # And then redirect the user to the main page
    return redirect(url_for('about'))
  else:
    # If no name has been sent, show the form
    return render_template('form.html', session=session)



@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('about'))
if __name__ == '__main__':
    app.run(debug=True)