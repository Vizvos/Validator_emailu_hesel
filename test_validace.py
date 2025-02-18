import unittest
from validace import *

class TestValidace(unittest.TestCase):
    def test_validni_email(self):
        self.assertTrue(validuj_email("test@example.com"))
        self.assertTrue(validuj_email("john.doe123@domain.co.uk"))

    def test_nevalidni_email(self):
        self.assertFalse(validuj_email("test@.com"))
        self.assertFalse(validuj_email("invalid-email"))
        self.assertFalse(validuj_email("test@domain,com"))

    def test_validni_heslo(self):
        self.assertTrue(validuj_heslo("Secure99Pass"))
        self.assertTrue(validuj_heslo("Secure99Pass"))

    def test_nevalidni_heslo(self):
        self.assertFalse(validuj_heslo("short"))
        self.assertFalse(validuj_heslo("nobignumbers"))
        self.assertFalse(validuj_heslo("12345678"))

    def test_validni_delka(self):
        self.assertTrue(validuj_delku("asasasass"))

    def test_validni_velke_pismeno(self):
        self.assertTrue(validuj_velke_pismeno("aaAasdaASs"))

if __name__ == '__main__':
    unittest.main()