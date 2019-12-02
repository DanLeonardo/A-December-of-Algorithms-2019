if __name__ == '__main__':
    N = int(input('Enter N: '))

    tokens = []
    print('Enter (token no, id): ')
    for i in range(0, N):
        token = input()
        token = token.lstrip('(')
        token = token.rstrip(')')
        token = token.replace(' ', '')
        token = token.split(',')
        tokens.append(token)

    print('Enter k: ')
    bribe = input()

    for token in tokens:
        if token[1] is bribe:
            tokens.remove(token)
            tokens.insert(0, token)

    print('The order is: ')
    for token in tokens:
        print('(%s, %s)' % (token[0], token[1]))
