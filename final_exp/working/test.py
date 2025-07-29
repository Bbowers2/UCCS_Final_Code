import math

def has_close_elements(my_list, threshold):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if abs(my_list[i] - my_list[j]) < threshold:
                return True
    return False
