from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key= 'Strawberry'

@app.route('/')
def index():
    return render_template("dojo_sur.html")


@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def success():
    return render_template('results.html')
    
if __name__=="__main__":
    app.run(debug=True)