# Returns the number of cookies a person could buy
# n:    money to spend
# p:    cost of one cookie
# c:    number of jars for a free cookie
def cookie_count(n, p, c):
    # Spend as much money as possible on cookies
    total_cookies = n // p
    n -= total_cookies * p
    print('Bought %d cookies for %d money' % (total_cookies, total_cookies*p))

    # Spend jars on free cookies until we don't have enough jars for another one
    num_jars = total_cookies
    while num_jars >= c:
        print('\tNum Jars: %d' % num_jars)
        free_cookies = num_jars // c
        print('\tGot %d free cookies for %d jars' % (free_cookies, num_jars // c * c))
        num_jars -= free_cookies * c - free_cookies
        print('\tRemaining Jars: %d' % num_jars)
        total_cookies += free_cookies
        print('')

    return total_cookies

if __name__ == '__main__':
    print(cookie_count(15, 3, 2))
    print(cookie_count(10, 2, 5))
    print(cookie_count(12, 4, 4))
