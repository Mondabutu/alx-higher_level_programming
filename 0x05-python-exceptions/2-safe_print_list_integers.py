#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k_num = 0
    for i in range(k_num, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            k_num += 1
        except (ValueError, TypeError):
            pass
    print()
    return k_num
