import question_a
from question_a import Stock


def main():


    stock_dictionary = {

        'AAPL': question_a.Stock('AAPL', 'Apple Inc'),
        'CAT':  question_a.Stock('CAT', 'Caterpillar'),
        'EK':   question_a.Stock('EK', 'Eastman Kodak'),
        'GOOG': question_a.Stock('GOOG', 'Google'),
        'MSFT': question_a.Stock('MSFT', 'Microsoft')



    }
       
    


    while True:

        print('1-Display stock purchase history')
        print('2-Exit')

        option = input('Enter an option: ')

        if option == '1':
           Stock.stock_purchase_history(stock_dictionary)
        
        elif option == '2':
            print('Program Exiting...')
            break

main()
