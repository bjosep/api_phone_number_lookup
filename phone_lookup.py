from flask import request, jsonify, Blueprint
from urllib.parse import unquote
from utils import (
    validate_and_parse_phone_number,
    is_phone_number_characters_valid,
    is_country_code_missing,
    is_valid_country_code,
    get_phone_number_info,
)

phone_lookup_api = Blueprint("v1", __name__)


@phone_lookup_api.route("/phone-numbers", methods=["GET"])
def phone_numbers_endpoint():
    # Get the request parameters
    encoded_phone_number = request.args.get("phoneNumber")
    country_code = request.args.get("countryCode", None)

    # Decode the URL-encoded phone number with unquote()
    phone_number = unquote(encoded_phone_number)

    # compact_phone_number stores the phone number without spaces
    compact_phone_number = phone_number.replace(" ", "")

    # Initialize the response variable
    response = {}
    response["phoneNumber"] = phone_number
    if country_code is not None:
        country_code = country_code.upper()
        response["countryCode"] = country_code

    # Validate that the country code follows ISO 3166-1 alpha-2 format
    if country_code is not None and not is_valid_country_code(country_code):
        response["error"] = {"countryCode": "invalid country code"}
        return jsonify(response), 400

    # Validate that the phone number contains only digits and spaces
    if not is_phone_number_characters_valid(phone_number):
        response["error"] = {"phoneNumber": "invalid characters"}
        return jsonify(response), 400

    if is_country_code_missing(compact_phone_number, country_code):
        response["error"] = {"countryCode": "required value is missing"}
        return jsonify(response), 400

    is_valid_phone_number, parsed_phone_number = validate_and_parse_phone_number(
        compact_phone_number, country_code
    )
    # Validate the phone number format using phonenumbers library
    if not is_valid_phone_number:
        response["error"] = {"phoneNumber": "invalid phone number"}
        return jsonify(response), 400

    # Process the phone number and retrieve information and add it to the reponse
    phone_info = get_phone_number_info(parsed_phone_number)
    response = {**phone_info, **response}

    return jsonify(response)
