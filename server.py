from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def home_play():
    return render_template('play_home.html')
    
@app.route('/play/<int:num>')
def play_times(num):
    return render_template('play_times.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def play_color(num, color):
    return render_template('play_color.html', num=num, color=color)


if __name__ == ("__main__"):
    app.run(debug=True)