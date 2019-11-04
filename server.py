from flask import Flask, request, render_template
from teapot import ESPTeapot
# import requests

app = Flask(__name__)
Teapot_address = 'http://192.168.1.'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        command = request.form['index']
        result = ''
        if command == 'start':
            temperature = request.form['temp']
            result = teapot.start(temperature)
        elif command == 'check':
            result = teapot.get_status()
        elif command == 'stop':
            result = teapot.stop()
        print(result)
    return render_template('index.html', data={'status': teapot.status, 'temp': teapot.temp})


@app.route('/api/teapot_is_ready')
def teapot_is_ready():
    if request.method == 'GET':
        status = request.args.get('status')
        if status == '1':
            teapot.status = 'Ready'
    return 'OK'


if __name__ == '__main__':
    teapot = ESPTeapot(url=Teapot_address)
    app.run()
