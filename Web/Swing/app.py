"""
flag is NCC{K3ep_ruNNing-567780}
"""
### Python Imports
from flask import Flask, render_template, redirect, url_for, request, abort

### Setting up the Flask App, Login Manager, and Database
app = Flask(__name__, template_folder="templates")

### The Flask Apps Code
@app.route('/')
def four():
    return redirect('/K')

@app.route('/K')
def ex():
    return redirect('/3')

@app.route('/3')
def w():
    return redirect('/e')

@app.route('/e')
def a():
    return redirect('/p')

@app.route('/p')
def y():
    return redirect('/_')

@app.route('/_')
def five():
    return redirect('/r')

@app.route('/r')
def under():
    return redirect('/u')

@app.route('/u')
def K():
    return redirect('/NN')

@app.route('/NN')
def e():
    return redirect('/I')

@app.route('/I')
def three():
    return redirect('/n')

@app.route('/n')
def p():
    return redirect('/g')

@app.route('/g')
def dash():
    return redirect('/-')

@app.route('/-')
def m():
    return redirect('/5')

@app.route('/5')
def zero():
    return redirect('/6')

@app.route('/6')
def v():
    return redirect('/77')

@app.route('/77')
def one():
    return redirect('/8')

@app.route('/8')
def n():
    return redirect('/0')

@app.route('/0')
def g():
    return redirect('/}')

@app.route('/}')
def close():
    return redirect('/?')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
