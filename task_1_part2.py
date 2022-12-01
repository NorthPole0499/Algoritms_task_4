import timeit
import task_1_part1

while True:
    print('\n1 - quick sort, 2 - comb sort, 0 - exit')
    x = int(input('Input the sort: '))
    if x == 1:
        data = task_1_part1.input_data()
        start_time = timeit.default_timer()
        sortdata = task_1_part1.quicksort(data)
        print('Quick sort:', sortdata)
        print('Time is', timeit.default_timer() - start_time)
    elif x == 2:
        data = task_1_part1.input_data()
        start_time = timeit.default_timer()
        sortdata = task_1_part1.combsort(data)
        print('Comb sort:', sortdata)
        print('Time is', timeit.default_timer() - start_time)
    elif x == 0:
        break
    else:
        print('Wrong input!')