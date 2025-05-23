#!/usr/bin/python3

def list_division(my_l_1, my_l_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result = my_l_1[i] / my_l_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
