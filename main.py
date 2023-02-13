from datetime import datetime

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


@app.get("/validate")
def validate():
    return "hi"


class Command(Resource):
    def post(self):
        return {
            "event_id": "foo",
            "created_at": datetime.now().isoformat(),
            "type": "PriceWasCalculated",
            "payload": {
                "person_id": "Tom",
                "card_id": "123",
                "price_amount": 0,
                "price_currency": "EUR",
            },
        }


api.add_resource(Command, '/handle-command')

if __name__ == '__main__':
    app.run(debug=True)
