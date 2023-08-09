from app import create_app
from unittest import TestCase
from phone_lookup_tests_data import PHONE_NUMBERS_TEST


class TestPhoneLookUp(TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.phone_numbers_test = PHONE_NUMBERS_TEST
        self.base_url = "/v1/phone-numbers?"

    def do_test(self, query, expected_response):
        url = self.base_url + query
        actual_response = self.app.get(url).get_json()
        assert expected_response == actual_response

    def test_valid_phone_full(self):
        """
        Testing the api returns correct information when given valid full phone number
        """
        query, expected_response = (
            self.phone_numbers_test["valid_phone_full"]["query"],
            self.phone_numbers_test["valid_phone_full"]["response"],
        )
        self.do_test(query, expected_response)

    def test_valid_phone_and_country_number(self):
        """
        Testing the api returns correct information when given valid phone number and country code
        """
        query, expected_response = (
            self.phone_numbers_test["valid_phone_and_country_number"]["query"],
            self.phone_numbers_test["valid_phone_and_country_number"]["response"],
        )
        self.do_test(query, expected_response)

    def test_invalid_country_number(self):
        """
        Testing the api returns an error when given invalid country code
        """
        query, expected_response = (
            self.phone_numbers_test["invalid_country_number"]["query"],
            self.phone_numbers_test["invalid_country_number"]["response"],
        )
        self.do_test(query, expected_response)

    def test_case_insensitive_country_number(self):
        """
        Testing the api case insensitive with respect to country code
        """
        query, expected_response = (
            self.phone_numbers_test["case_insensitive_country_number"]["query"],
            self.phone_numbers_test["case_insensitive_country_number"]["response"],
        )
        self.do_test(query, expected_response)

    def test_missing_country_number(self):
        """
        Testing the api returns an error when country code is required but missing
        """
        query, expected_response = (
            self.phone_numbers_test["missing_country_number"]["query"],
            self.phone_numbers_test["missing_country_number"]["response"],
        )
        self.do_test(query, expected_response)

    def test_valid_spaces(self):
        """
        Testing the api processes correctly phone numbers with valid spaces
        """
        query, expected_response = (
            self.phone_numbers_test["valid_spaces"]["query"],
            self.phone_numbers_test["valid_spaces"]["response"],
        )
        self.do_test(query, expected_response)

    def test_invalid_spaces(self):
        """
        Testing the api processes returns an error when given an phone number with invalid spaces
        """
        query, expected_response = (
            self.phone_numbers_test["invalid_spaces"]["query"],
            self.phone_numbers_test["invalid_spaces"]["response"],
        )
        self.do_test(query, expected_response)
