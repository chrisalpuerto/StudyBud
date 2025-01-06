# main flask file
# chris alpuerto

from flask import Flask, request,render_template,app

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        location = request.form['location']
        acompany = request.form['acompany']


    return render_template('index.html')
@app.route('/results', methods=['GET', 'POST'])
def results():
    print()

    return render_template('results.html')
if __name__ == '__main__':
    app.run(debug=True)