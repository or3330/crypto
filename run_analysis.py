from tx_pool import TxPool
import matplotlib.pyplot as plt

#for mempool in mempools:
txpool = TxPool("C:\\Users\\שחר\\PycharmProjects\\crypto\\mempool\\test.json")
taken_txs1, profit1 = txpool.choose_txs(1)
taken_txs2, profit2 = txpool.choose_txs(2)
taken_txs3, profit3 = txpool.choose_txs(3)
taken_txs4, profit4 = txpool.choose_txs(4)

x_coordinates = [1, 2, 3, 4]
y_coordinates = [profit1, profit2, profit3, profit4]
plt.scatter(x_coordinates, y_coordinates)
plt.show()