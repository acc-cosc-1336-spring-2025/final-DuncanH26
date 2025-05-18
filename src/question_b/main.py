import question_b

def main():

    while True:
        string = input('Enter a DNA string with a length between 9 and 16: ')
        if 9 <= len(string) <= 16:
            break
        else: 
            print('Invalid DNA string')

    while True:
        substring = input('Enter a substring with only 4 characters: ')
        if len(substring) == 4:
            break
        else:
            print('Invalid DNA substring')

    consensus = question_b.get_most_likely_ancestor_consensus(string, substring)
            
    if consensus:
                print(f'The substring {substring} had positions inside the string {string} at {consensus}')
                

main()

    