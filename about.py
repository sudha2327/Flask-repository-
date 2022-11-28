from flask import Flask
import flask

app=Flask(__name__)



def about():
    return "this about blog!!!!"

app.add_url_rule("/about","about",about)

if __name__=="__main__":
    app.run(debug=True)

