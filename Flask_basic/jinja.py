from flask import Flask, render_template, request  #'request' for POST handling

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Home Page!"

@app.route('/index', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        # You can handle form data here using request.form
        name=request.form['name']#retireve
        return f"Hello, {name}!"
    return render_template('form.html')
#varibale rules
@app.route('/success/<score>')
def success(score):
    # return "The marks obtained is: " score
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template('result.html',result=res)
@app.route('/successres/<score>')
def successers(score):
    
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
        #key_value pair
        exp={'score':score,'result':res}
    return render_template('result1.html',result=res)


if __name__ == '__main__':
    app.run(debug=True)
'''
To read data from backend in the html page:
1.{{variable_name}}  #double curly braces:expression to print output in html
2.{% statement %}  #for loop, if else
3.{# comment #}  #comment
'''
@app.route('/submit',method=['GET'<'POST"'])
def submit():
    if request .method=='POST':
        s=float(request.form['science'])
        m=float(request.form['maths'])
        e=float(request.form['english'])
        total=(s+m+e)/3
    else:
        return render_template('submit.html')
    return redirect(url_for('successers',result=total))
        
        