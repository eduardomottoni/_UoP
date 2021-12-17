def sort_list(list_to_sort):
    return list_to_sort.sort()

def add_increment_list(given_list): #list argument refer to the real object
    if len(given_list) != 0:
        n=0
        while (n < len(given_list)):
            for a in given_list:
                a += 1
                given_list[n] = a
                break
            n += 1
        print(given_list)
    else:
        print('list has no elements')
    
add_increment_list([])
add_increment_list([1,2]) #parameter when passed this way are the real objects
add_increment_list([3,4,5]) #inside function, this objects receive names like 'given_list', 'list_to_sort'
add_increment_list([3,2,1])
add_increment_list([1,1,1,1])
add_increment_list([1,2,3,4,5,6,7])
