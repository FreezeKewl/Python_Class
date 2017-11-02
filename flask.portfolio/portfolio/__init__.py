
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Claude'
    filename = 'img'
    return render_template('index.html', name = name, filename = filename)
    return render_template('about.html')
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return render_template('about.html')
        return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact')

if __name__ == "__main__":
    app.run(debug=True)
