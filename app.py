from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def challenge_one():
    return render_template('challenge1.html')

@app.route('/secretkey')
def challenge_two():
    return render_template('challenge2.html')

# for 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
