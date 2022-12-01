def str_to_float(data):
    for i in range(len(data)):
        data[i] = float(data[i])
    return data

def input_data():
    strdata = input('Input the list: ')
    data = strdata.split()
    data = str_to_float(data)
    return data

def quicksort(data):
    if len(data) <= 1:
        return data
    else:
        supel = data[len(data) // 2]
        l_data = []
        r_data = []
        e_data = []
        for i in range(len(data)):
            if data[i] < supel:
                l_data.append(data[i])
            elif data[i] > supel:
                r_data.append(data[i])
            else:
                e_data.append(data[i])
        return quicksort(l_data) + e_data + quicksort(r_data)

def combsort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(len(data) - i):
            if data[j] > data[j + i]:
                data[j], data[j + i] = data[j + i], data[j]
    return data