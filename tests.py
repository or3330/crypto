import unittest
from tx_pool import TxPool

def convert_dict_to_mempool_format(desc):
    new_desc = dict()
    for i, tx_desc in enumerate(desc):
        new_desc[i] = {i: tx_desc}
    return new_desc


test1 = [
    {"from": "shahar",
     "gasPrice": "1",
     "nonce": "0"},
    {"from": "shahar",
     "gasPrice": "100",
     "nonce": "1"},
    {"from": "shahar",
     "gasPrice": "300",
     "nonce": "2"},
    {"from": "shahar",
     "gasPrice": "1",
     "nonce": "3"},
    {"from": "shahar",
     "gasPrice": "1",
     "nonce": "4"},
    {"from": "shahar",
     "gasPrice": "1",
     "nonce": "5"},
    {"from": "shahar",
     "gasPrice": "1",
     "nonce": "6"},
    {"from": "or",
     "gasPrice": "50",
     "nonce": "1"},
    {"from": "or",
     "gasPrice": "1",
     "nonce": "2"},
    {"from": "or",
     "gasPrice": "1",
     "nonce": "3"},
    {"from": "or",
     "gasPrice": "400",
     "nonce": "4"},
    {"from": "or",
     "gasPrice": "1",
     "nonce": "5"},
    {"from": "or",
     "gasPrice": "1",
     "nonce": "6"}
]

test2 = [{"from": "shahar",
          "gasPrice": "1",
          "nonce": "0"},
         {"from": "shahar",
          "gasPrice": "100",
          "nonce": "1"},
         {"from": "or",
          "gasPrice": "1",
          "nonce": "1"},
         {"from": "or",
          "gasPrice": "50",
          "nonce": "2"},
         {"from": "or",
          "gasPrice": "150",
          "nonce": "3"}
         ]

t1 = TxPool(convert_dict_to_mempool_format(test1))


class MyTestCase(unittest.TestCase):
    def test1(self):
        taken_txs, profit = t1.choose_txs(2, 2)
        self.assertEqual(101, profit, "Test1 failed!")
        print("debug1: taken_txs= ", taken_txs, " profit= ", profit)

    def test2(self):
        taken_txs, profit = t1.choose_txs(3, 2)
        print("debug2: taken_txs= ", taken_txs, " profit= ", profit)
        self.assertEqual(101, profit, "Test2 failed!")

    def test3(self):
        taken_txs, profit = t1.choose_txs(2, 3)
        print("debug3: taken_txs= ", taken_txs, " profit= ", profit)
        self.assertEqual(401, profit, "Test3 failed!")

    def test4(self):
        taken_txs, profit = t1.choose_txs(3, 3)
        print("debug4: taken_txs= ", taken_txs, " profit= ", profit)
        self.assertEqual(401, profit, "Test4 failed!")

    def test5(self):
        taken_txs, profit = t1.choose_txs(4, 4)
        print("debug5: taken_txs= ", taken_txs, " profit= ", profit)
        self.assertEqual(451, profit, "Test5 failed!")

    def test6(self):
        taken_txs, profit = t1.choose_txs(4, 10)
        print("debug6: taken_txs= ", taken_txs, " profit= ", profit)
        self.assertEqual(856, profit, "Test5 failed!")

    def test7(self):
        taken_txs, profit = t1.choose_txs(4, 15)
        print("debug7: taken_txs= ", taken_txs, " profit= ", profit)
        self.assertEqual(859, profit, "Test5 failed!")


if __name__ == '__main__':
    unittest.main()

