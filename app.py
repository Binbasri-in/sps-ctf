from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def challenge_one():
    return render_template('round1/challenge1.html')

@app.route('/HertzDominatePixel')
def challenge_two():
    return render_template('round1/challenge2.html')

@app.route('/lunch')
def lunch():
    return render_template('round1/lunch.html')

@app.route('/round2')
def round2():
    return render_template('round2/challenge1.html')

@app.route('/ctse')
def flag21():
    return render_template('round2/challenge2.html')

@app.route('/flag22')
def flag22():
    return render_template('round2/challenge3.html')

@app.route('/extra')
def round3():
    return render_template('extra/challenge1.html')

@app.route('/extra2')
def flag31():
    return render_template('extra/challenge2.html')


# for 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
