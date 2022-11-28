from flask import *
from werkzeug.exceptions import RequestTimeout

app=Flask(__name__)
app.secret_key="abc"

@app.route('/')

def homr():
    res=make_response("<h3>hey man <a href='/get'> get</a> link</h3>")
    session['response']="Session1"
    return res

@app.route('/get')

def sees():
    if 'response' in session:
        s=session['response']

        return render_template('getses.html',n=s)



if __name__=="__main__":
    app.run(debug=True)