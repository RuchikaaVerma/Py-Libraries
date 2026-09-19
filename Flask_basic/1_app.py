#Terminal : pip install flask

from flask import Flask

#intialize the flask app
app=Flask(__name__)#object of flask class
'''
It create an instance of the flask class,
which will be your WSGI(web server gateway interface) application.

route() decorator in Flask is used to bind a URL to a specific function.
unique and readable URL for each function, which is known as a route.
When a user accesses that URL, the associated function is executed, and its return value is sent back as the HTTP response.
'''

@app.route('/')#decorator('/'=rule parameter)
#it call this   function

def welcome():
    #point top of this fxn
    return "Welcome to Flask" #return value is response to the request
#parameter
if __name__=='__main__':#entry point
    app.run(debug=True)
    #(put host=form of string,port=integer,debug=True/False)
    '''debug=True:it will automatically reload the server when code changes'''