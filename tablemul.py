from flask  import *

app=Flask(__name__)

@app.route("/mul/<int:num>")

def tabel(num):
    return render_template('table.html',n=num)





if __name__=="__main__":
    app.run(debug=True)