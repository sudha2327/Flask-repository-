from flask import *

app=Flask(__name__)

@app.route('/cookie')

def main():
    res=make_response("<h1>Hii .. is it u????</h1>")
    res.set_cookie('floo','booo')
    return res

if __name__=="__main__":
    app.run(debug=True)