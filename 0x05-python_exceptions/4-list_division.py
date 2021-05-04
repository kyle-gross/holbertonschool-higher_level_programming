#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            number = my_list_1[i] / my_list_2[i]
        except IndexError:
            number = 0
            print("out of range")
        except ZeroDivisionError:
            number = 0
            print("division by 0")
        except TypeError:
            number = 0
            print("wrong type")
        finally:
            new_list.append(number)
    return new_list
