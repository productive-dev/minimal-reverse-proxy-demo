import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_precipitation():

    temperature_c = int(request.args.get('temp'))

    if not temperature_c:
        temperature_c = 23

    precip_type = "rain"

    is_cold = temperature_c < 0
    is_warm = temperature_c > 25

    if is_cold:
        print('cold weather detected')
        precip_type = "snow"

    if is_warm:
        print('warm weather detected')
        precip_type = "storms"

    percent_chance = round(random.uniform(0, 1) * 100)

    return {
        'precip_chance': percent_chance,
        'type': precip_type
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')