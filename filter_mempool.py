import subprocess
import tempfile
from datetime import datetime
import os
from tx_pool import TxPool
from shutil import copyfile
from time import sleep

MEMPOOL_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'important_mempool')

def is_important_mempool(mempool_path):
    txpool = TxPool(txs=mempool_path)

    more_than_one_tx_sender, _ = txpool.count_txs_by_senders()
    if more_than_one_tx_sender > 0:
        return True
    return False

if __name__ == '__main__':
    if not os.path.exists(MEMPOOL_DIR):
        os.mkdir(MEMPOOL_DIR)

    temp_dir = tempfile.mkdtemp()

    number_of_snapshots = 0

    while(1):
        # Extacting the mempool to a temp dir
        now = datetime.now()
        file_name = now.strftime("%m_%d_%Y_%H_%M_%S") + '.json'
        file_path = os.path.join(temp_dir, file_name)
        cmd = ' '.join(['E:\\Technion\\crypto_project\\Ethereum\\Geth\\geth.exe', 'attach', 'http://localhost:8545/', '--exec', '"console.log(JSON.stringify(txpool.content.pending, null ,2))"', '>', '{}'.format(file_path)])
        subprocess.check_call(cmd, shell=True)

        # Deleted the last line of the file, it is None and needs to be deleted
        with open(file_path) as f1:
            lines = f1.readlines()
        with open(file_path, 'w') as f1:
            f1.writelines(lines[:-1])

        # Checking if the mempool snapshot is important and copying it if it is
        if is_important_mempool(file_path):

            copyfile(file_path, os.path.join(MEMPOOL_DIR, file_name))
        print(file_path)
        print(number_of_snapshots)
        number_of_snapshots += 1
        os.remove(file_path)
        sleep(60)    
