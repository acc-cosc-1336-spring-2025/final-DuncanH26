import question_c
from question_c import Stock

def main():
   
   stock_list = Stock.get_stock_list()
   


   while True:

        print('1-Display stock purchase history')
        print('2-Exit')

        option = input('Pick an option: ')

        if option == '1':
            Stock.display_stock_list(stock_list)
      
        elif option == '2':
            print('Program Exiting...')
            break

main()
     
