import unittest
from main2 import get_days_of_power

class TestTotalDays(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000), 10, "Should be 10")
        self.assertEqual(get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000), 141, "Should be 10")
        self.assertEqual(get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000), 17, "Should be 10")
        self.assertEqual(get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000), 5, "Should be 10")
        self.assertEqual(get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000), 1, "Should be 10")


if __name__ == '__main__':
    unittest.main()