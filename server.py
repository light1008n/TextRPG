from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def game():
    return send_from_directory('static', 'index.html')

@app.route('/partials/<page>')
def partials(page):
    return send_from_directory('partials', f'{page}.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
