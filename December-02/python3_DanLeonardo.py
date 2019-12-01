# Checks if a given credit card number is valid or not
# Returns: True if valid, False if invalid
def valid_credit_card(num):
    num_list = [int(x) for x in str(num)]
    num_list.reverse()

    # Sum odd digits
    sum_odd = 0
    for i in range(0, len(num_list), 2):
        sum_odd += num_list[i]

    # Handle even digits
    sum_even = 0
    for i in range(1, len(num_list), 2):
        even_digit = num_list[i] * 2
        if even_digit > 9:
            even_digit = sum(int(x) for x in str(even_digit))
        sum_even += even_digit

    # Sum both sums and check if last digit is 0
    sum_total = sum_odd + sum_even
    sum_total = [int(x) for x in str(sum_total)]

    if sum_total[-1] == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    test_number = 49927398716

    if valid_credit_card(test_number):
        print('%d passes the test' % test_number)
    else:
        print('%d fails the test' % test_number)
