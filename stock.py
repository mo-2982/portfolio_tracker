class Stock:
    def __init__(self, symbol, quantity, buy_price):
        self.symbol = symbol
        self.quantity = quantity
        self.buy_price = buy_price
        self.current_price = buy_price
        
    def invested(self):
        return self.buy_price * self.quantity
    
    def current_value(self):
        return self.current_price * self.quantity
    
    def profit(self):
        return self.current_value() - self.invested() 
    
    def profit_percent(self):
        return (self.profit() / self.invested()) * 100
    
    def update_price( self,new_price):
        self.current_price = new_price
    
    def __str__(self):
        return (
        f"{self.symbol}: {self.quantity} shares, "
        f"profit {self.profit():+,.0f} ({self.profit_percent():+.1f}%)"
    )

if __name__ == "__main__":
    s = Stock("Foolad", 1000, 4500)
    s.update_price(4950)
    print(s.invested())
    print(s.current_value())
    print(s.profit())
    print(s.profit_percent())
    print(s)
        