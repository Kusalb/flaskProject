from flask import Flask, jsonify
import time
import asyncio
from flask_sock import Sock

from all_vuln_one_var import run_program
app = Flask(__name__)
sock = Sock(app)
# sock.init_app(app=)

@app.route('/')
async def hello():  # put application's code here
    await run_program()
    return jsonify({'about': "Hello world"})

@sock.route('/')
def vulnurability_detection(ws):
    while True:
        data = ws.receive()
        print(data)
        data = data.split(" ")
        if data[0]=="start":
            rs = run_program(data[1])
            ws.send(rs)




if __name__ == '__main__':
    app.run()
