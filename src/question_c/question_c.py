class Stock:
  
  def __init__(self, symbol, company_name):
    self.__symbol = symbol
    self.__company_name = company_name

  def get_symbol(self):
        return self.__symbol
    
  def get_company_name(self):
        return self.__company_name
    
  def get_stock_list():
       
       stock_list = []

       stock_list.append(Stock('AAPL', 'Apple Inc'))
       stock_list.append(Stock('CAT', 'Caterpillar'))
       stock_list.append(Stock('EK', 'Eastman Kodak'))
       stock_list.append(Stock('GOOG', 'Google'))
       stock_list.append(Stock('MSFT', 'Microsoft'))

       return stock_list
    
  def display_stock_list(stock_list):
       for stock in stock_list:
          
        print(f'Company:{stock.get_company_name()}, Symbol:{stock.get_symbol()}')
