from flask import Flask, request, jsonify

app = Flask(__name__)

# This is a sample Python script.
@app.get("/validate")
def validate():
    return "hi"

@app.post("/handle-command")
def handle_command():
    return {
        "event_id": "foo",
        "created_at": "new Date().toISOString()",
        "type": "PriceWasCalculated",
        "payload": {
            "person_id": "Tom",
            "price_amount": 0,
            "price_currency": "EUR",
        },
    }, 200
