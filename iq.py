from flask import Flask, render_template, url_for, request, redirect
import random

x = random.randint(50, 200)
app = Flask(__name__)
counter = 0
melon = 0
@app.route('/')
def home():
    global x
    x = random.randint(50, 200)
    global counter
    global melon
    counter = 0
    melon = 0
    return render_template('home.html')

@app.route('/q1/', methods=['POST', 'GET'])
def q1():
    global counter
    global melon
    if melon > 1:
        counter = 0
        melon = 0
        return redirect(url_for('home'))
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == '12':
            counter += 1
        return redirect(url_for('q2'))
    else:
        return render_template('q1.html')

@app.route('/q2/', methods=['POST', 'GET'])
def q2():
    global counter
    global melon
    if melon > 2:
        counter = 0
        melon = 0
        return redirect(url_for('home'))
    melon = 2
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == '45':
            counter += 1
        return redirect(url_for('q3'))
    else:
        return render_template('q2.html')

@app.route('/q3/', methods=['POST', 'GET'])
def q3():
    global counter
    global melon
    if melon > 3:
        counter = 0
        melon = 0
        return redirect(url_for('home'))
    melon = 3
    if request.method == 'POST':
        answer = request.form['answer']
        answer = answer.lower()
        if answer == 'no':
            counter += 1
        return redirect(url_for('q4'))
    else:
        return render_template('q3.html')

@app.route('/q4/', methods=['POST', 'GET'])
def q4():
    global counter
    global melon
    if melon > 4:
        counter = 0
        melon = 0
        return redirect(url_for('home'))
    melon = 4
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == '-3' or answer == '-2':
            counter += 1
        return redirect(url_for('q5'))
    else:
        return render_template('q4.html')

@app.route('/q5/', methods=['POST', 'GET'])
def q5():
    global counter
    global melon
    if melon > 5:
        counter = 0
        melon = 0
        return redirect(url_for('home'))
    melon = 5
    if request.method == 'POST':
        answer = request.form['answer']
        try:
            answer = float(answer)
        except:
            answer = answer

        if answer == 5.5:
            counter += 1
        return redirect(url_for('final'))
    else:
        return render_template('q5.html')

@app.route('/finalscore')
def final():
    if x <= 50:
        answer = 'you are stoopid and that will always be true and Mr Oviedo will always look down upon you.'
    elif x <= 100:
        answer = 'you are just below average but you are still stoopid.'
    elif x <= 150:
        answer = 'you are smart. Now that you\'ve found that out, go make some friends instead of boosting your ego with IQ tests.'
    elif x <= 200:
        answer = 'Holy macaroni you are officially G-d we must now pray to you, we shall make a temple in your honour.'
    global counter
    global melon
    melon = 6
    return render_template('end.html', counter=counter, x=x, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)