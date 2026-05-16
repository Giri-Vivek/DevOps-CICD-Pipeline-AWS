from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>DevOps CI/CD Pipeline Project</h1>
    <h2>Deployment Successful...</h2>
    <p>Application deployed using Jenkins + Docker + AWS</p>
    <p>Time: {datetime.now()}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)