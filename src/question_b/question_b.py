#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):

    position = []
    index = 0

    while True:
       
        index = dna_string1.find(dna_string2, index)
        if index == -1:
            break
        position.append(index + 1) 
        index += 1
        
    
    return position 