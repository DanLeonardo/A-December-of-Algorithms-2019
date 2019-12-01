import random
import time

# Checks if a given list is sorted
def check_if_sorted(list):
    if len(list) <= 1:
        return True

    last_value = list[0]
    for i in range(1, len(list)):
        if last_value > list[i]:
            return False
        else:
            last_value = list[i]

    return True

# Removes half of the values in the given list rounding down
def snap(list):
    if len(list) <= 1:
        return

    # The number of elements to remove per snap
    num_to_remove = len(list) // 2

    # Remove a random element in the list
    random.seed(time.time())
    while num_to_remove > 0:
        index = random.randint(0, len(list)-1)
        list.pop(index)

        num_to_remove -= 1

# Performs Thanos Sort on a given list
# If the list is not sorted half of its values are snapped (removed)
# Thanos Sort runs until the list is sorted
def thanos_sort(list):
    while not check_if_sorted(list):
        snap(list)

    return list

if __name__ == '__main__':
    test_list = [1, 2, 5, 3, 4, 5]

    print('Thanos Sort: %s' % test_list)
    thanos_sort(test_list)
    print('Sorted: %s' % test_list)
