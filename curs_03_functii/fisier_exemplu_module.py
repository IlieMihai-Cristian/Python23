def modul_func(a, b=0, *args, **kwargs):
    total = 0
    initial = a + b
    for x in args:
        total += x
    for y in kwargs.values():
        total += y
    return initial + total

var_ex = 'orice'