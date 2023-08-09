from argparse import ArgumentParser
from flask import Flask
from phone_lookup import phone_lookup_api


def parse_port():
    # Get the port number to listen to, by default we're using port 5000
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default=5000,
        type=int,
        help="listening port, default value of 5000",
    )
    args = parser.parse_args()
    port = args.port
    return port


def create_app():
    # Create the Flask app
    app = Flask(__name__)
    app.register_blueprint(phone_lookup_api, url_prefix="/v1")
    return app


def main():
    # Launch the flask app
    port = parse_port()
    app = create_app()
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
