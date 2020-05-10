import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_temperature():
    temperature_c = random.randint(-10, 33)
    return { 'temperature_c': temperature_c }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')