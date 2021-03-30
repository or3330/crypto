import heapq
import collections

# constants
max_gas_in_block = 10000000
avg_gas_in_tx = 21000
#avg_tx_in_block = 3 #max_gas_in_block/avg_gas_in_tx
profit_i = 0
num_tx_i = 1
from_i = 2

class TxPool:
    def __init__(self, txs):
        self.tx_dict = collections.defaultdict(list)
        self.txs = txs
        self.__create_tx_lists_by_sender()

    def __create_tx_lists_by_sender(self):
        for tx in self.txs:
            self.tx_dict[tx["from"]].append(tx)
        for key in self.tx_dict:
            self.tx_dict[key] = sorted(self.tx_dict[key], key=lambda k: k['nonce'])

    def __add_to_heap(self, tx_list, look_ahead, h, pointer):
        sum = 0
        look_ahead_window = max(min(look_ahead, len(tx_list)-pointer), 0)
        for i in range(0, look_ahead_window):
            sum += int(tx_list[i+pointer]["gasPrice"])
            h.append([-sum / (i + 1), i + 1, tx_list[i]["from"]])

    def __remove_tx_from_list(self, tuple_tx):
        self.tx_dict[tuple_tx[from_i]] = self.tx_dict[tuple_tx[from_i]][tuple_tx[num_tx_i]:]

    def choose_txs(self, look_ahead, avg_tx_in_block):
        taken_txs = []
        look_ahead = min(look_ahead, avg_tx_in_block)
        sender_list_pointer_dict = collections.defaultdict(int)
        profit = 0
        num_taken_tx = 0

        while num_taken_tx < avg_tx_in_block:
            h = []
            for key in self.tx_dict:  # Add all the firsts from each sender to heap  # can improve performance here
                self.__add_to_heap(self.tx_dict[key], look_ahead, h, sender_list_pointer_dict[key])
            heapq.heapify(h)
            if len(h) == 0:
                return taken_txs, profit
            new_tx = heapq.heappop(h)
            while num_taken_tx+ new_tx[num_tx_i] > avg_tx_in_block:
                if len(h) == 0:
                    return taken_txs, profit
                new_tx = heapq.heappop(h)
            profit += -(new_tx[profit_i] * new_tx[num_tx_i])
            num_taken_tx += new_tx[num_tx_i]
            look_ahead = min(avg_tx_in_block - num_taken_tx, look_ahead)
            taken_txs.append(self.tx_dict[new_tx[from_i]][:new_tx[num_tx_i]])
            sender_list_pointer_dict[new_tx[from_i]] += new_tx[num_tx_i]
            #print(h) ## debug

        return taken_txs, profit