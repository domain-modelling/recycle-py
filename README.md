# Recycle - python client

## Installation

Create a virtual environment and activate it
```bash
python3 -m venv _env
source _env/bin/activate
```

Install all requirements
```bash
pip install -r requirements.txt
```

## Running
`python ./main.py`

## Setting up ngrok
Make sure you have ngrok configured correctly. If unsure, please visit https://dashboard.ngrok.com/get-started/your-authtoken

`ngrok http 127.0.0.1:5000` should  setup the tunnel. Copy the generated url from the commandline.
You can also visit https://dashboard.ngrok.com/cloud-edge/endpoints to see the endpoints you are exposing.

