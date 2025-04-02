#basics everything in single file



from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)


# route structure

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/abcd')
def abcd():
    return "Hello, ABCDDDDDD!"





@app.route('/welcome/<name>')
def welcome(name):
    return render_template('index.html', name=name)








@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        return f"Welcome, {username}!"
    return '''
        <form method="post">
            Name: <input type="text" name="username">
            <input type="submit">
        </form>
    '''

@app.route('/api/data')
def api_data():
    return jsonify({"message": "Hello, API!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
