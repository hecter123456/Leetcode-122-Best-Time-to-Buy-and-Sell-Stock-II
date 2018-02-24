import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = 0
        self.assertEqual(Solution().maxProfit(Input),Output)
    def testSample(self):
        Input = [1,2,3,4,5]
        Output = 4
        self.assertEqual(Solution().maxProfit(Input),Output)

class Solution():
    def maxProfit(self, prices):
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total

if __name__ == '__main__':
    unittest.main()
