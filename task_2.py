def insert_sort(data):
    for i in range(1, len(data)):
        current = data[i]
        ind = i - 1
        while ind >= 0 and current < data[ind]:
            data[ind + 1] = data[ind]
            ind = ind - 1
        data[ind + 1] = current
    return data


def bloch_sort(data):
    znach = max(data) / len(data)
    new_data = []
    for i in range(len(data)):
        new_data.append([])

    for j in range(len(data)):
        box_index = int(data[j] / znach)
        new_data[box_index - 1].append(data[j])

    itog = []
    for q in new_data:
        itog += insert_sort(q)
    return itog


def heapsort(data):
    def build_max_heap(data):
        parent = (len(data) - 1 - 1) // 2
        while parent >= 0:
            max_heapify(data, parent, len(data))
            parent -= 1

    def max_heapify(data, index, size):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < size and data[left] > data[index]:
            largest = left
        else:
            largest = index
        if right < size and data[right] > data[largest]:
            largest = right
        if largest != index:
            data[largest], data[index] = data[index], data[largest]
            max_heapify(data, largest, size)

    build_max_heap(data)
    for i in range(len(data) - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        max_heapify(data, 0, i)
    return data


data = [5, 4, 3, 2, 1]
print("Исходный список:", data)
print("Блочная сортировка:", bloch_sort(data))
print("Пирамидальная сортировка:", heapsort(data))
