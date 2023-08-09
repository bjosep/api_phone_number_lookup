PHONE_NUMBERS_TEST = {
    "valid_phone_full": {
        "query": "phoneNumber=%2B12125690123",
        "response": {
            "areaCode": "212",
            "countryCode": "US",
            "localPhoneNumber": "5690123",
            "phoneNumber": "+12125690123",
        },
    },
    "valid_phone_and_country_number": {
        "query": "phoneNumber=2125690124&countryCode=US",
        "response": {
            "areaCode": "212",
            "countryCode": "US",
            "localPhoneNumber": "5690124",
            "phoneNumber": "2125690124",
        },
    },
    "invalid_country_number": {
        "query": "phoneNumber=12124690123&countryCode=USA",
        "response": {
            "countryCode": "USA",
            "error": {"phoneNumber": "invalid phone number"},
            "phoneNumber": "12124690123",
        },
    },
    "case_insensitive_country_number": {
        "query": "phoneNumber=12124690123&countryCode=Us",
        "response": {
            "areaCode": "212",
            "countryCode": "US",
            "localPhoneNumber": "4690123",
            "phoneNumber": "12124690123",
        },
    },
    "missing_country_number": {
        "query": "phoneNumber=6313118150",
        "response": {
            "error": {"countryCode": "required value is missing"},
            "phoneNumber": "6313118150",
        },
    },
    "valid_spaces": {
        "query": "phoneNumber=34%20915%20872200&countryCode=ES",
        "response": {
            "areaCode": "",
            "countryCode": "ES",
            "localPhoneNumber": "915872200",
            "phoneNumber": "34 915 872200",
        },
    },
    "invalid_spaces": {
        "query": "phoneNumber=351%2021%20094%20%202000",
        "response": {
            "error": {"phoneNumber": "invalid characters"},
            "phoneNumber": "351 21 094  2000",
        },
    },
}
