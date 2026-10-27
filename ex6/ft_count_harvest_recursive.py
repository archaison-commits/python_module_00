#!/usr/bin/env python3

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def days_recursion(n=1):
        if days - n < 0:
            print("Harvest time!")
        else:
            print(f"Day {n}")
            days_recursion(n+1)
    days_recursion()
