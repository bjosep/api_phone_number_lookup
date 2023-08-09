# Phone Number Lookup API

This repository contains a simple Flask-based API that allows users to perform phone number lookup and retrieve information about the phone number, such as the country code, area code, and local phone number.

## Installation and Usage

To install and run the submission, follow these steps:

1. Ensure you have Python 3 installed on your system
2. After extracting the zip file, navigate to the corresponding extracted directory
3. Create a virtual environment called `venv` by running `python3 -m venv venv`
4. Activate the previous virtual virtual environment by running `source venv/bin/activate` (On Unix or MacOS, using the bash shell)
5. Install the required dependencies by running `pip install -r requirements.txt`
6. Run the application by executing `python3 app.py`
   The Flask app will be accessible at `http://localhost:5000/`,
   if port 5000 is not available, you can pick a specific port by executing `python3 app.py -p port_number`
7. Our endpoint is at `http://localhost:5000/v1/phone-numbers`,<br />
   the following sample request `http://localhost:5000/v1/phone-numbers?phoneNumber=%2B12125690123` should return `{"areaCode":"212","countryCode":"US","localPhoneNumber":"5690123","phoneNumber":"+12125690123"}`
8. The existing unit tests can be run with `python3 -m unittest phone_lookup_tests.py`

## Folder Structure

1. **app.py**: Contains the main entry point of the Phone Number Lookup API. It configures and launches the Flask application to handle incoming HTTP requests.

2. **phonelookuptestdata.py**: Provides test data for the phone lookup API unit tests.

3. **phonelookuptests.py**: Contains unit tests for the phone lookup API to ensure its functionality and behavior are correct.

4. **phonelookup.py**: This file contains the implementation of the Phone Number Lookup API.

5. **utils.py**: Contains utility functions used by the phone lookup API for phone number validation and parsing.

6. **requirements.txt**: Lists the required Python packages and their versions for the application to run.

7. **README.md**: Contains the project's documentation, including installation instructions, technology stack, assumptions, and future improvements.

## Tech Stack

- Python: Chosen as the programming language due to its simplicity, readability, and a wide range of libraries available
- Flask: Used as the web framework due to its lightweight nature and simplicity for building RESTful APIs
- Phonenumbers Library: Used for phone number validation and parsing to ensure accurate and reliable handling of phone numbers. Building a regular expression for this task is complex and we might miss a lot of edge cases.
- argparse Module: Used to parse command-line argument for the port number
- pycountry: Used for country code validation

## Deployment (Optional)

To deploy the application to production, we can take advantage of GCP App Engine service which is fairly straightforward.
reference: `https://towardsdatascience.com/how-to-deploy-a-flask-api-8d54dd8d8b8a`

## Assumptions

- Country code is case insensitive which verifies ISO 3166-1 alpha-2 format, for example, `US` and `Us` both refers to the same country code
- We aim at validating phone number which means not only that the given combination of digits is possible but also
  it's in an assigned exchange

## Future Improvements

- Improve test coverage with additional test cases to cover various scenarios thoroughly
- Add more documentation, for example, functions docstring
- Add logging to track API usage and errors for better debugging and monitoring
