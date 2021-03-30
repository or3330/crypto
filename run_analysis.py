from tx_pool import TxPool
import matplotlib.pyplot as plt
import os

# for mempool in mempools:
file_path = os.path.dirname(os.path.realpath(__file__))
json_path = os.path.join(file_path, 'mempool/test.json')
txpool = TxPool(json_path)

taken_txs1, profit1 = txpool.choose_txs(1, 20)
taken_txs2, profit2 = txpool.choose_txs(2, 20)
taken_txs3, profit3 = txpool.choose_txs(3, 20)
taken_txs4, profit4 = txpool.choose_txs(4, 20)

print(len(taken_txs1))
print(taken_txs2)
print(taken_txs3)
print(taken_txs4)


x_coordinates = [1, 2, 3, 4]
y_coordinates = [profit1, profit2, profit3, profit4]
plt.scatter(x_coordinates, y_coordinates)
plt.show()