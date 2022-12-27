from flask import Flask

from datetime import datetime

app = Flask(__name__)

@app.get("/validate")
def validate():
    return "hi"

@app.post("/handle-command")
def handle_command():
    return {
        "event_id": "foo",
        "created_at": datetime.now().isoformat(),
        "type": "PriceWasCalculated",
        "payload": {
            "person_id": "Tom",
            "price_amount": 0,
            "price_currency": "EUR",
        },
    }, 200
