# tutorial from youtube c.p. - fibonacci pt 1


# approach 1 using direct

def fibonacci(n):
    """

    :param int n:  the sequence member
    :return: n-th member of Fibonacci sequence
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

    load_ext line_profiler
    lprun -f fibonacci(5)
