from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test-format')
def test_format():
    return render_template('test_format.html')

@app.route('/mock-test')
def mock_test():
    return render_template('mock_test.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you would typically save the data to a database
        flash('Thank you for joining us, {}! We have received your message.'.format(name))
        return redirect(url_for('join'))
    return render_template('join.html')

if __name__ == '__main__':
    app.run(debug=True)
