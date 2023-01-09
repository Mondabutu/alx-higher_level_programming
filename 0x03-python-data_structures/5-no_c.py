#!/usr/bin/python3
def no_c(my_string):
    mynew_string = my_string.translate({ord(i): None for i in 'cC'})
    return mynew_string
