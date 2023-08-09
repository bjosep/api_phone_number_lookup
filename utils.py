import phonenumbers

from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
)
import pycountry


def validate_and_parse_phone_number(phone_number, country_code):
    parsed_number = None
    try:
        # Parse the phone number and check if it's valid
        parsed_number = phonenumbers.parse(phone_number, country_code)
        return phonenumbers.is_valid_number(parsed_number), parsed_number
    except phonenumbers.NumberParseException:
        return False, parsed_number


def is_phone_number_characters_valid(phone_number):
    # Remove trailing and leading spaces
    trimmed_phone_number = phone_number.strip()
    # Check if there are invalid spaces in the phone number
    if len(trimmed_phone_number.split()) > 3:
        return False
    # Check if the phone number contains only digits and spaces
    return all(
        char.isdigit() or char.isspace() or char == "+" for char in trimmed_phone_number
    )


def is_country_code_missing(phone_number, country_code):
    # Check if the country code is required and missing
    return not country_code and not phone_number.startswith("+")


def is_valid_country_code(country_code):
    # Check if the country code is a valid ISO 3166-1 alpha-2 code using pycountry library
    try:
        # Try to look up the country code in the pycountry database
        pycountry.countries.get(alpha_2=country_code)
        return True
    except LookupError:
        return False


def get_phone_number_info(parsed_phone_number):
    # parse information from phone number
    national_number = phonenumbers.national_significant_number(parsed_phone_number)
    length_area_code = phonenumbers.length_of_geographical_area_code(
        parsed_phone_number
    )
    country_code_string = region_code_for_country_code(parsed_phone_number.country_code)
    area_code = ""
    subscriber_number = ""

    if length_area_code > 0:
        subscriber_number = national_number[length_area_code:]
        area_code = national_number[:length_area_code]

    else:
        subscriber_number = national_number
        area_code = ""

    # Create the phone info dictionary and fill it with the information
    phone_info = {
        "countryCode": country_code_string,
        "areaCode": area_code,
        "localPhoneNumber": subscriber_number,
    }
    return phone_info
