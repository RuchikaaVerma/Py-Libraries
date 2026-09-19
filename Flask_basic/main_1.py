from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    #intergrate with html (this mehid is not optimal) so better approach to redirect we use a library render_template .
   # return "<html><body><h1>Welcome to Flask</h1></body></html>"
    return render_template('index.html')#error =template not found which is index.html is not integrated properly
''' it will lookup to the folder templates and find the html file'''

@app.route('/about')
def about():
    return render_template('about.html')
    #in web server terminal type(/file_name)
if __name__=='__main__':
    app.run(debug=True)
   