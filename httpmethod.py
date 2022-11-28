from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

app=Flask(__name__)
@app.route('/login',methods=['GET','POST'])

def do_the_login():
    return render_template('hii.html')

def show():
    return "here this one having the process of showing the details !!!!!!!!!!!!!"
def login():
    if request.method=='POST':
        return do_the_login()
    else:
        return show()





if __name__=='__main__':
    app.run()