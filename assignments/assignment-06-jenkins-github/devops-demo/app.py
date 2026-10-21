import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'message': 'DevOps CI/CD Demo Application running successfully!',
        'ci_tool': 'Jenkins Automation Server',
        'author': 'Rutuja Deepak Jagtap',
        'roll_no': '123B1B146',
        'college': 'PCCOE Pune',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({
        'health': 'healthy',
        'code': 200,
        'uptime': 'operational'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
