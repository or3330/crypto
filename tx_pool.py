import heapq
import collections
from tx import Tx
import json

# constants
max_gas_in_block = 10000000
avg_gas_in_tx = 21000
# avg_tx_in_block = 3 #max_gas_in_block/avg_gas_in_tx
profit_i = 0
num_tx_i = 1
from_i = 2


class TxPool:
    def __init__(self, txs):
        """
        :param txs: either dict or path to json file
        """
        self.tx_dict = collections.defaultdict(list)
        self.txs = self.__parse_mempool(txs)
        self.__create_tx_lists_by_sender()

    @staticmethod
    def __parse_mempool(mempool):
        """
        Parses the json or dict file to list of Txs

        :param mempool:
        :return:
        """
        txs = list()

        if isinstance(mempool, str):
            with open(mempool) as fp:
                mempool = json.load(fp)

        for tx_id, tx_desc in mempool.items():
            tx_desc = list(tx_desc.values())[0]
            txs.append(Tx(tx_id, tx_desc))

        return txs

    def __create_tx_lists_by_sender(self):
        for tx in self.txs:
            self.tx_dict[tx.from_address].append(tx)
        for key in self.tx_dict:
            self.tx_dict[key] = sorted(self.tx_dict[key], key=lambda k: k.nonce)

    @staticmethod
    def __add_to_heap(tx_list, look_ahead, h, pointer):
        sum = 0
        look_ahead_window = max(min(look_ahead, len(tx_list)-pointer), 0)
        for i in range(0, look_ahead_window):
            sum += int(tx_list[i+pointer].gas_price)
            h.append([-sum / (i + 1), i + 1, tx_list[i].from_address])

    def __remove_tx_from_list(self, tuple_tx):
        self.tx_dict[tuple_tx[from_i]] = self.tx_dict[tuple_tx[from_i]][tuple_tx[num_tx_i]:]

    def choose_txs(self, look_ahead, avg_tx_in_block):
        """
        TODO: add documentation
        :param look_ahead:
        :param avg_tx_in_block:
        :return:
        """
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
            while num_taken_tx + new_tx[num_tx_i] > avg_tx_in_block:
                if len(h) == 0:
                    return taken_txs, profit
                new_tx = heapq.heappop(h)
            profit += -(new_tx[profit_i] * new_tx[num_tx_i])
            num_taken_tx += new_tx[num_tx_i]
            look_ahead = min(avg_tx_in_block - num_taken_tx, look_ahead)
            taken_txs.append(self.tx_dict[new_tx[from_i]][:new_tx[num_tx_i]])
            sender_list_pointer_dict[new_tx[from_i]] += new_tx[num_tx_i]
            # print(h) ## debug

        return taken_txs, profit
