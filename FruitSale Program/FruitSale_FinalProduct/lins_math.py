def add(list):
    total = 0
    for item in list:
        if item != None:
            total += int(item)
    return total

def average_list(list1, list2, list3):
    average = (list1 + list2 + list3)//3
    return average
