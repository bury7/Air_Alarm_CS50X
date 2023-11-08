import json
from flask import Flask, render_template
from static.python.parser_telegram import Telegram, InvalidIDException, InvalidHashException


app = Flask(__name__)


"""Main route"""
@app.route('/')
def index():
    return render_template("index.html")


"""API for air alarms"""
@app.route('/api')
async def api():
    t = Telegram()
    await t.get()
    info = t.alarms
    return json.dumps(info)


if __name__ == "__main__":
    app.run(debug=True)