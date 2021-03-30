from settings import Settings


class Tx:
    def __init__(self, tx_id: int, tx_desc: dict):
        """
        :param tx_id:
        :param tx_desc:
        """
        self.tx_id = tx_id
        self.nonce = int(tx_desc[Settings.NONCE], 16)
        self.from_address = tx_desc[Settings.FROM]
        self.gas_price = int(tx_desc[Settings.GAS_PRICE], 16)
        self.gas = int(tx_desc.get(Settings.GAS, 0), 16)
        self.desc = tx_desc

    @property
    def profit(self):
        return self.gas * self.gas_price

    def __str__(self):
        return str(self.desc)

    def __repr__(self):
        return str(self.desc)
