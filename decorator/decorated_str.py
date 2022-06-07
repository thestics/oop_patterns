def suffix_with_char(char):
    assert isinstance(char, str)

    def decorator(f):
        def wrapper(s):
            return f(s) + char

        return wrapper

    return decorator


def prefix_with_char(char):
    assert isinstance(char, str)

    def decorator(f):
        def wrapper(s):
            return char + f(s)

        return wrapper

    return decorator


@suffix_with_char("\n")
@suffix_with_char("!")
@suffix_with_char("World")
@suffix_with_char(" ")
@suffix_with_char(",")
@prefix_with_char("Hello")
def print_str(s):
    return s


s = print_str("")
print(s)
