from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'support bot training interface'

@app.route('/bot')
def talk():
    return render_template('bot.html')

@app.route('/bot2')
def talk2():
    return render_template('bot2.html')


if __name__ == "__main__":
    app.run()
