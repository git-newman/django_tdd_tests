from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    """тест на токсичность"""

    def test_bad_math(self):
        """неправильные математические расчеты"""
        self.assertNotEqual(1+4, 3)
