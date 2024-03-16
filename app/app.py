from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/teste', methods=['GET'])
def get_generic():
    return 'testado!'

@app.route('/with/<name>', methods=['GET'])
def medicine_names(name):
    return f'teste de {name}'

# app.run(host=os.getenv('app_host'), port=os.getenv('app_port'), debug=True)
