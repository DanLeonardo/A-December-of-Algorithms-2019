# A N'ish number is a natural number which is either a power of N, or the sum of unique powers on N
# Returns the num'th N'ish number in the sequence
def nish_number(num, base):
    if num < 1 or base < 0:
        return -1

    binary_array = create_binary_array(num)

    sum = 0
    for i, power in enumerate(binary_array):
        if power is 1:
            sum += pow(base, i)

    return sum

# Returns a list of powers of 2 that when summed together add up to num
# The list is reversed so the index is the power of 2
# e.g. num=7 returns a list [1, 1, 1, 0]
# 2^0 + 2^1 + 2^2 == 7
def create_binary_array(num):
    binary_array = []

    binary_array.append(num%2)
    if num > 1:
        binary_array.extend(create_binary_array(num//2))

    return binary_array

# Returns the "num" sevenish number
def sevenish_number(num):
    return nish_number(num, 7)

if __name__ == '__main__':
    for i in range(1, 11):
        print('%d: %d' % (i, sevenish_number(i)))
