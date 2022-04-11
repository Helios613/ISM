from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def index():
    if(request.method=='POST'):
        url = request.form.get('url')
        constraint = request.form.get('constraint')
        return render_template('index.html', url=url, constraint=constraint)
    return render_template('index.html')

app.run(debug=True)

