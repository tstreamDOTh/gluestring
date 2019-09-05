import unittest
from gluestring.gluegun import Gluegun

offer_dictionary = {
    "offer_thirty": "30%",
    "offer_fourty": "40%",
    "default": "null"
}
test_offer_string = "Get {{offer_thirty}} off . Get {{offer_fourty}} if SUPER user. "


class TestUtils(unittest.TestCase):
    def test_gluegun(self):
        g1 = Gluegun(offer_dictionary)
        result_string = g1.glue_it(test_offer_string)
        self.assertEqual(
            result_string, 'Get 30% off . Get 40% if SUPER user. ')

    def test_gluegun_with_no_parameters_should_not_throw_error(self):
        # TODO: Add a default dictionary with a map with a DEFAULT key set as 'NA'
        g1 = Gluegun()
        result_string = g1.glue_it(test_offer_string)
        self.assertEqual(
            result_string, 'Get NA off . Get NA if SUPER user. ')

    def test_gluegun_with_no_default(self):
        # TODO: Add a default dictionary with a map with a DEFAULT key set as 'NA'
        # Hint - Merge the supplied dictionary with a default dictionary, if DEFAULT is present in the supplied dictionary then is should overrider the DEFAULT: NA in the default dictionary
        offer_dictionary_without_default = {
            "offer_thirty": "30%",
            "offer_fourty": "40%",
        }
        test_offer_string_with_unknown_keys = "Get {{offer_alien}} off . Get {{offer_alien2}} if SUPER user. "

        g1 = Gluegun(offer_dictionary_without_default)
        result_string = g1.glue_it(test_offer_string_with_unknown_keys)

        self.assertEqual(
            result_string, 'Get NA off . Get NA if SUPER user.')


if __name__ == '__main__':
    unittest.main()

# python -m unittest tests.unit_tests
