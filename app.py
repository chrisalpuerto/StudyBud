# main flask file
# chris alpuerto

from flask import Flask, request,render_template,app

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        print("hi")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)