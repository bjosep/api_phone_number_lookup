# api_phone_number_lookup

## Overview
The goal of this API is to provide information about phone numbers based on specific requirements. It exposes a REST/HTTP interface that allows users to query details about a phone number in E.164 format, including the country code, area code, and local phone number. Additionally, the API handles edge cases, for instance missing country code or unvalid phone number formatting.

## Frameworks
Flask, unittest, pycountry, phonenumbers

## Installation
follow the instructions on installation.md

## Requirements
### /v1/phone-numbers Endpoint
Create an endpoint that takes request parameters and returns information about a phone number.

Request Parameters<br>
*phoneNumber:* The phone number in E.164 format.

Format: [+][country code][area code][local phone number]<br>
Example: +12125690123 (valid), +52 631 3118150 (valid), 34 915 872200 (valid), 351 21 094 2000 (invalid)<br>
If phoneNumber is missing the country code, the user must provide countryCode parameter in ISO 3166-1 alpha-2 format.<br>

*countryCode:* The country code in ISO 3166-1 alpha-2 format.

Example: US (valid), MX (valid), ESP (invalid)

<br>
Request: /v1/phone-numbers?phoneNumber=%2B12125690123<br>
Response:
json
{
 "phoneNumber": "+12125690123",
 "countryCode": "US",
 "areaCode": "212",
 "localPhoneNumber": "5690123"
}
Note: + is URL-encoded as %2B, and [space] is URL-encoded as %20.
<br>
Request: /v1/phone-numbers?phoneNumber=631%20311%208150<br>
Response: Invalid phone number format
