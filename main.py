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
        print(data[i])
        break
