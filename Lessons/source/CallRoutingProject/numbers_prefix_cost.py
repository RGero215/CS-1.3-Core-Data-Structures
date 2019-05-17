import re

def number_list(file_name):
    """Function takes a file and return a word list no puntuations"""                      
    file_object = open(file_name, "r", encoding="utf-8-sig")
    no_punctuation_file = file_object.read()
    #.3 Use regular expresion to remove puntuation
    no_punctuation_file = re.sub(r'[+]','',no_punctuation_file)
    #.4 Storage an array of words without puntuations
    number_list = no_punctuation_file.split()
    # print(number_list)
    return number_list

def prefix_cost_dict(file_name):
    prefix = ''
    cost = ''
    result_list = []                       
    file_object = open(file_name, "r", encoding="utf-8-sig")
    no_plus_file = file_object.read()
    no_plus_file = re.sub(r"[+-,]", " ", no_plus_file)
    list_prefix_cost = no_plus_file.split()
    for index, item in enumerate(list_prefix_cost):
        if index %2 == 0:
            prefix = item
        else:
            cost = item
            result_list.append((prefix, cost))
            
    
    # print(result_list)
    return result_list

    


if __name__ == "__main__":
    # print(number_list('phone-numbers-1000.txt'))
    print(prefix_cost_dict('route-costs-35000.txt'))
    # print(ord('0'))
    # print(ord('1'))
    # print(ord('2'))
    # print(ord('3'))
    # index = 0
    # number_list = number_list('phone-numbers-1000.txt')
    # while index < len(number_list):
    #     print(number_list[index])
    #     for number in number_list[index]:
    #         print(number)
            
    #     break

    #     index += 1

    pass