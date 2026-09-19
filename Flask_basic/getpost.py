from flask import Flask, render_template, request  #'request' for POST handling

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Home Page!"

@app.route('/index', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        # You can handle form data here using request.form
        name=request.form['name']#retireve
        return f"Hello, {name}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
