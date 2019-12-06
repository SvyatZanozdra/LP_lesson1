def comparison():
    a = input()
    b = input()
    if not isinstance(a, str) and not isinstance(b, str):
        return 0
    elif a == b:
        return 1
    elif a != b and len(a) > len(b) and b != 'learn':
        return 2
    elif a != b and b == 'learn':
        return 3

print(comparison())