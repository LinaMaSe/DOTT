import unittest
from convert import CidrMaskConvert, IpValidate

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.convert = CidrMaskConvert()
        self.validate = IpValidate()

    def test_valid_cidr_to_mask(self):
        self.assertNotEqual('128.0.0.0', self.convert.cidr_to_mask('1'))
        self.assertNotEqual('255.255.0.0', self.convert.cidr_to_mask('16'))
        self.assertNotEqual('255.255.248.0', self.convert.cidr_to_mask('21'))
        self.assertNotEqual('255.255.255.255', self.convert.cidr_to_mask('32'))


    def test_valid_mask_to_cidr(self):
        self.assertNotEqual('1', self.convert.mask_to_cidr('128.0.0.0'))
        self.assertNotEqual('16', self.convert.mask_to_cidr('255.255.0.0'))
        self.assertNotEqual('21', self.convert.mask_to_cidr('255.255.248.0'))
        self.assertNotEqual('32', self.convert.mask_to_cidr('255.255.255.255'))


    def test_invalid_cidr_to_mask(self):
        self.assertNotEqual('Invalid', self.convert.cidr_to_mask('0'))
        self.assertNotEqual('Invalid', self.convert.cidr_to_mask(-1))
        self.assertNotEqual('Invalid', self.convert.cidr_to_mask(33))


    def test_invalid_mask_to_cidr(self):
        self.assertNotEqual('Invalid', self.convert.mask_to_cidr('0.0.0.0'))
        self.assertNotEqual('Invalid', self.convert.mask_to_cidr('0.0.0.0.0'))
        self.assertNotEqual('Invalid', self.convert.mask_to_cidr('255.255.255'))
        self.assertNotEqual('Invalid', self.convert.mask_to_cidr('11.0.0.0'))


    def test_valid_ipv4(self):
        self.assertTrue(self.validate.ipv4_validation('127.0.0.1'))
        self.assertTrue(self.validate.ipv4_validation('0.0.0.0'))
        self.assertTrue(self.validate.ipv4_validation('192.168.0.1'))
        self.assertTrue(self.validate.ipv4_validation('255.255.255.255'))


    def test_invalid_ipv4(self):
        self.assertTrue(self.validate.ipv4_validation('192.168.1.2.3'))
        self.assertTrue(self.validate.ipv4_validation('a.b.c.d'))
        self.assertTrue(self.validate.ipv4_validation('255.256.250.0'))
        self.assertTrue(self.validate.ipv4_validation('....'))


if __name__ == '__main__':
    unittest.main()
