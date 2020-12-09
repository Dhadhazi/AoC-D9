with open("input.txt") as file:
    data = [int(number) for number in file.read().split("\n")]

PREAMBLE = 25


def sum_of_preamble(num, look):
    got_sum = False
    for base in range(PREAMBLE-1):
        for find in range(base+1, PREAMBLE):
            if look[base]+look[find] == num:
                got_sum = True
                break

    return got_sum
    return False



for i in range(PREAMBLE, len(data)):
    if not sum_of_preamble(data[i], data[i-PREAMBLE: i]):
        no_sum_number = data[i]
        print(f"First part solution: {no_sum_number}")
        break

# Part Two


def find_contiguous_set(number_to_look_for, dataset):
    number_set = [dataset[0]]
    i = 1;
    while i < len(dataset) and dataset[i] < number_to_look_for:
        if sum(number_set) < number_to_look_for:
            number_set.append(dataset[i])
            i += 1
        elif sum(number_set) > number_to_look_for:
            number_set = number_set[1:]
        else:
            return number_set
            break


contiguous_set = find_contiguous_set(no_sum_number, data)

minmax = min(contiguous_set)+max(contiguous_set)
print(f"Min max together: {minmax}")