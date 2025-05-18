class Stock:

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
    def stock_purchase_history(stock_dictionary):
        for symbol, stock in stock_dictionary.items():
            print (stock.get_symbol(), stock.get_company_name())

            

 
