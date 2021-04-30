#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    # Multiply the members of each tuple
    products = []
    for i in my_list:
        products.append(i[0] * i[1])
    # Add individual results of mulitplication
    sum1 = sum(products)
    # Sum the second member of the tuples
    weight = sum(i[1] for i in my_list)
    # Divide sum of mult by sum of 2nd tuple member
    return sum1 / weight
