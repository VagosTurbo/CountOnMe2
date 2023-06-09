#!/usr/bin/env python3

import re 
import cProfile
import pstats
from pstats import SortKey
from mathlib import *

## @file Standart_deviation.py
# @author Kristian Grecnar
# @brief It calculates standart deviation of the sample which is located in a text file (data.txt)
# @date 24.4 2023
# @param numbers array of numbers from text file data.txt
# @return the value of standart deviation

input_numbers = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    input_numbers += line.strip() + " "

numbers = re.split('\s+', input_numbers.strip())

numbers = [float(number) for number in numbers]

## @brief Standart deviation function
# @param numbers array of numbers from text file data.txt
# @return value of standart deviation
def STD_Deviation(numbers):

############################# mean ff numbers

    lenght_of_numbers_list = len(numbers)

    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers = float(add(sum_of_numbers, num))

    mean_of_numbers =  float(div(sum_of_numbers, lenght_of_numbers_list))

############################# standart deviation
##### sum (xi- x_priemer)pwr 2
    sum_num_sub_mean = 0
    for x in numbers: 
        sum_num_sub_mean = float(add(sum_num_sub_mean, float(pwr(float(sub(x, float(mean_of_numbers))), 2))))

    N_sub_1 = float(sub(lenght_of_numbers_list, 1))    

    Standart_deviation = float(nthroot(float(div(sum_num_sub_mean, N_sub_1)), 2))

    return Standart_deviation 

STD_Deviation(numbers)

std_dev=STD_Deviation(numbers)
print(std_dev)

cProfile.run('STD_Deviation(numbers)', filename='Profilefile.txt')

with open ("output_time.txt", "w" ) as f:
    p = pstats.Stats("Profilefile.txt", stream=f)
    p.sort_stats("time").print_stats()

with open ("output_calls.txt", "w" ) as f:
    p = pstats.Stats("Profilefile.txt", stream=f)
    p.sort_stats("calls").print_stats()
    
## End of file Standart_deviation.py ##