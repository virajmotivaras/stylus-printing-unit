from flask import Flask, jsonify, request,send_file

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def hello():
    # return string can indicate the location of the unit
    return "Alive:Mumbai:Unit1
    "



if __name__ == '__main__':
    app.run(debug=True, port=9000)