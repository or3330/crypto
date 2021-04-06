from tx_pool import TxPool
import matplotlib.pyplot as plt
import os


for filename in os.listdir('./mempool/'):
    file_path = os.path.dirname(os.path.realpath(__file__))
    full_filename = 'mempool/'+ filename
    json_path = os.path.join(file_path, full_filename)
    txpool = TxPool(json_path)

    more_than_one_tx_sender, total_senders = txpool.count_txs_by_senders()
    print ("for json: ", filename)
    print("there are ", more_than_one_tx_sender , " senders with more than one tx, out of total ", total_senders, " senders")

#taken_txs1, profit1 = txpool.choose_txs(1, 10)
#taken_txs2, profit2 = txpool.choose_txs(2, 10)
#taken_txs3, profit3 = txpool.choose_txs(3, 10)
#taken_txs4, profit4 = txpool.choose_txs(4, 10)

#print(len(taken_txs1))
#print(taken_txs2)
#print(taken_txs3)
#print(taken_txs4)


#x_coordinates = [1, 2, 3, 4]
#y_coordinates = [profit1, profit2, profit3, profit4]
#plt.scatter(x_coordinates, y_coordinates)
#plt.show()
