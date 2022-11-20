class Bar:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.bar_tab = 0
    
    def add_money_to_bar_tab(self, drink):
        self.bar_tab += drink