from mathlib import *

input_numbers = input()

numbers = input_numbers.split(" " or "\n" or "\t")

if len(numbers) < 2:
    print("nizky pocet cisiel")
    exit()

numbers = [float(number) for number in numbers]

############################# mean if numbers


lenght_of_numbers_list = len(numbers)

sum_of_numbers = 0
for num in numbers:
        sum_of_numbers = add(sum_of_numbers, num)

mean_of_numbers =  div(sum_of_numbers, lenght_of_numbers_list)
print ("mean of numbers is", mean_of_numbers)

############################# standart deviation

sum_num_sub_mean = 0
for num in numbers:
       sum_num_sub_mean = add(sum_num_sub_mean, pwr(sub(num, mean_of_numbers), 2))
       

Standart_deviation = sqrt(div(sum_num_sub_mean, sub(lenght_of_numbers_list, 1)))

print ("Standart deviation of the numbers is ", Standart_deviation)