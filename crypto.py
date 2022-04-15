class Crypto:

    def __init__(self, name: str, symbol: str, price: int, percent_change_24h: int,
                 percent_change_7d: int, market_cap: int, volume_24h: int,
                 circulating_supply: int):
        self.name = name
        self.symbol = symbol
        self.price = round(price, 2)
        self.percent_change_24h = round(percent_change_24h, 2)
        self.percent_change_7d = round(percent_change_7d, 2)
        self.market_cap = market_cap
        self.volume_24h = volume_24h
        self.circulating_supply = circulating_supply

    def __str__(self):
        return f"{self.symbol}, {self.name}, {self.price}$ "\
               f"{self.percent_change_24h}%, {self.percent_change_7d}% "\
                f"{self.market_cap}, {self.volume_24h}, {self.circulating_supply}"





#todo klasy z metodami przyjmujaca lisye na podstawie symbolu wywoluje dane cene ruchy itd
