from flask import Flask
app=Flask("__name__")

@app.route('/home/<name>')

def home(name):
    name=input("enter the name:")
    age=input("enter the age:")
    return "name is"+name+"age is"+age

if __name__=="__main__":
    app.run(debug=True)