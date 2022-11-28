from flask import *

app=Flask(__name__)

@app.route('/login',methods=['POST'])

def log():
    uname=request.form['username'] ##request.args.get('username')
    pword=request.form['password'] ##request.args.get('password')

    if uname=='sudha' and pword=='1234':
        return 'Welcome %s'%uname
    else:
        return "hiii %s"%uname+"hellow %s" %pword 
    


if __name__=='__main__':
    app.run(debug=True)




