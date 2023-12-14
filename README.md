# hello_world

A simple python package which can be pip installed and used with an API key. Uses Supabase as database, Stripe for payment, and Heroku for hosting.

## Installation

You can install the package via pip:

```bash
pip install hello_world
```

## Usage

First, you need to initialize the package with your API key:

```python
from hello_world import HelloWorld

hw = HelloWorld("your_api_key")
```

Then, you can use the `hello_world` method:

```python
message = hw.hello_world()
print(message)  # prints: "Hello, World!"
```

Please note that the `hello_world` method can only be called if you have made a payment.

## Payment

To make a payment, you can use the `make_payment` method from the `Payment` class:

```python
from hello_world import Payment

payment = Payment("your_api_key")
payment.make_payment("your_stripe_token", 100)  # make a payment of 100 USD
```

## Hosting

The package is hosted on Heroku. You can access the API at: `https://your-heroku-app-name.herokuapp.com/hello_world`

## Requirements

- Python 3.6+
- FastAPI
- Stripe
- Supabase
- Heroku

## Development

To contribute to this project, you can clone the repository:

```bash
git clone https://github.com/yourusername/hello_world
cd hello_world
```

Then, install the dependencies:

```bash
pip install -r requirements.txt
```

You can run the FastAPI server with:

```bash
uvicorn main:app --reload
```

## License

This project is licensed under the terms of the MIT license.
