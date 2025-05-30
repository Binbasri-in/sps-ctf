from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/start', methods=['GET', 'POST'])
def challenge_oneq():
    return render_template('day2/challenge1.html')

@app.route('/', methods=['GET', 'POST'])
def challenge_one():
    return render_template('day2/last-challenge.html')  # activate after lunch

@app.route('/challenge1', methods=['GET', 'POST'])
def challenge_onew():
    return render_template('round1/challenge1.html')


@app.route('/Datacenter')
def datacenter():
    return render_template('day2/Datacenter.html')

@app.route('/data-qr')
def dataqr():
    return render_template('day2/challenge2.html')

@app.route('/true')
def sink():
    return render_template('day2/Sink.html')

@app.route('/sink-qr')
def sinkqr():
    return render_template('day2/challenge3.html')

@app.route('/sink-qr-wrong')
def sinkqrwrong():
    return render_template('day2/Wrong.html')

@app.route('/decode@cts')
def decode():
    return render_template('day2/last-challenge.html')

@app.route('/HertzDominatePixel')
def challenge_two():
    return render_template('round1/challenge2.html')

@app.route('/lunch')
def lunch():
    return render_template('round1/lunch.html')

@app.route('/logic-lock')
def round2():
    return render_template('round2/challenge1.html')

@app.route('/ctse')
def flag21():
    return render_template('round2/challenge2.html')

@app.route('/gate')
def flag22():
    return render_template('round2/challenge3.html')

@app.route('/jawed')
def flag23():
    return render_template('round2/final.html')


@app.route('/extra')
def round3():
    return render_template('eyantra.html')

@app.route('/extra2')
def flag31():
    return render_template('extra/challenge2.html')


# for 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
