import time



# print(sum([number for number in range(10)]))
# print(sum(number for number in range(10)))


list_start_time = time.time()
print(sum([number for number in range(10000)]))
list_processing_time = time.time() - list_start_time

gen_start_time = time.time()
print(sum(number for number in range(10000)))
gen_processing_time = time.time() - gen_start_time

print(f'Processing with list is {list_processing_time}')
print(f'Processing with gen is {gen_start_time}')