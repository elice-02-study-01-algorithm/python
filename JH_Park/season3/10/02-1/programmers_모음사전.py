from itertools import product

def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    list_to_dict = {}
    
    for i in range(5):
        for w in list(product(alphabet, repeat=(i+1))):
            dictionary.append(''.join(list(w)))

    dictionary.sort()
    
    for i in range(len(dictionary)):
        list_to_dict[dictionary[i]] = i + 1
    print(list_to_dict)
    
    return list_to_dict[word]