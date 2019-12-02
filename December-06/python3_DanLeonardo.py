def fibonacci(n, sequence=[]):
    if n < 1:
        return []

    for i in range(len(sequence),n):
        if i in [0, 1]:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])

    return sequence

def fibonacci_prime(n):
    if n < 1:
        return []

    sequence = []
    prime_sequence = []

    while len(prime_sequence) < n:
        if len(sequence) in [0, 1]:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])

        last_sequence = sequence[-1]
        if is_prime(last_sequence):
            prime_sequence.append(last_sequence)
            print('%d: %d is prime' % (len(sequence), last_sequence))

    return prime_sequence

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    for num1 in range(2, num//2):
        if (num % num1) == 0:
            return False

    return True

if __name__ == '__main__':
    fib9 = fibonacci_prime(100)
    print(fib9)
