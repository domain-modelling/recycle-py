# Recycle - python client

## Installation
`python3 -m pip install -r requirements.txt`

## Running
`FLASK_APP=main.py flask run`

This will start a flask app listening on 127.0.0.1 on port 5000. If you want to use a different host and port, use this:
`FLASK_APP=main.py flask run --host=0.0.0.0 -p 8000`

If you want the server to restart after save, use the debug flag:
`FLASK_APP=main.py flask --debug run --host=0.0.0.0 -p 8000`

## Setting up ngrok
Make sure you have ngrok configured correctly. If unsure, please visit https://dashboard.ngrok.com/get-started/your-authtoken

`ngrok http 5000` should  setup the tunnel. Copy the generated url from the commandline.
You can also visit https://dashboard.ngrok.com/cloud-edge/endpoints to see the endpoints you are exposing.

