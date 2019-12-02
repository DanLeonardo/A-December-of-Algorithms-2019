def squared(x):
    return x * x

def times2(x):
    return x * 2

def check_one_to_one(input, fx):
    set1, set2 = input
    map = {}

    for val in set1:
        result = fx(val)

        if result in map:
            return False
        elif result not in set2:
            return False
        else:
            map[result] = val

    return True

if __name__ == '__main__':
    set1 = [1,-1,2,3,4]
    set2 = [2,-2,4,6,8]

    if check_one_to_one((set1, set2), times2):
        print('It is one-one.')
    else:
        print('It is not one-one.')
