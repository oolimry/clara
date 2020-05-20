def food(number):
    result = 0
    for i in range(1, number):
        result += i
    if result == 0:
        return "die"
    else:
        return result
