# int -> booelan
# Given integer n, returns True or False based on reachability of goal
def bears(n):
    if n < 42:
        return False
    if n == 42:
        return True
    if n % 2 == 0:
        if bears(n - n // 2):
            return True
    if n % 3 == 0 or n % 4 == 0:
        n_str = str(n)
        first_dig = int(n_str[-1])
        second_dig = int(n_str[-2])
        if first_dig * second_dig != 0:
            if bears(n - (first_dig * second_dig)):
                return True
    if n % 5 == 0:
        if bears(n - 42):
            return True
    return False
