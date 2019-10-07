from timeit import default_timer as timer
from copy import copy
start = timer()
counter = 0


class Ledder:

    def __init__(self, producer, max_length, max_weight, material):
        self.producer = producer
        self.max_length = int(max_length)
        self.material = material
        self.max_weight = int(max_weight)

    def __repr__(self):
        return str(self.__dict__)


def read(file):
    with open(file) as f:
        list_of_ledders = []
        for line in f:
            line = line.strip("\n").split(",")
            list_of_ledders.append(Ledder(line[0], line[1], line[2],line[3]))
    return list_of_ledders


# selection
def sort_by_max_height(list_of_ledders):
    print("Algorithm name: Selection Sort")
    global counter
    counter = 0
    swap_counter = 0
    for j in range(len(list_of_ledders)):
        min_weight = 0
        min_position = 0
        for i in range(j, len(list_of_ledders)):
            if min_weight == 0:
                min_position = i
                min_weight = list_of_ledders[i].max_weight
            elif list_of_ledders[i].max_weight > min_weight:
                min_weight = list_of_ledders[i].max_weight
                min_position = i
            counter += 1

        if min_position != 0 and min_weight != 0 and min_position != j:
            temp = list_of_ledders[j]
            list_of_ledders[j] = list_of_ledders[min_position]
            list_of_ledders[min_position] = temp
            swap_counter += 1

    print("Comparison was made %d times" % counter)
    print("Swap was made %d times" % swap_counter)
    for i in list_of_ledders:
        print(i)


# merge
def sort_by_max_mass(list_of_ledders):
    print("Merge Sort")
    global counter
    counter = 0

    def split(input_list):
        if len(input_list) <= 1:
            return input_list

        middle_point = len(input_list) // 2

        left_part = input_list[0:middle_point]
        right_part = input_list[middle_point:]
        return merge(split(left_part), split(right_part))

    def merge(left_part, right_part):


        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index].max_length <= right_part[right_index].max_length:
                result.append(left_part[left_index])
                left_index += 1
            else:
                result.append(right_part[right_index])
                right_index += 1
            global counter
            counter += 1
        result = result + left_part[left_index:] + right_part[right_index:]
        return result

    list_of_ledders = split(list_of_ledders)
    print("Comparison was made %d times" % counter)
    for i in list_of_ledders:
        print(i)


list_of_ledders = read("file.txt")



sort_by_max_height(copy(list_of_ledders))
sort_by_max_mass(copy(list_of_ledders))
end = timer()
print("Time of completion: " + str(end - start) +
      " seconds" + "\n")
