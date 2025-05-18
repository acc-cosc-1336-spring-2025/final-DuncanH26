import question_d

def main():

    while True:

        multiplication_table = question_d.create_multiplication_table()
        question_d.display_multiplication_table(multiplication_table)


        option = input('Do you wish to continue (y/n): ')
        
        if option == 'n':
            break

main()

