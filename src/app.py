def c_to_f(temp: float) -> float:
    return temp * 9 / 5 + 32


def c_to_k(temp: float) -> float:
    return temp + 273.156


def f_to_c(temp: float) -> float:
    return (temp - 32) + 5 / 9


def f_to_k(temp: float) -> float:
    return (temp + 459.67) * 5 / 9


def k_to_c(temp: float) -> float:
    return temp - 273.15


def k_to_f(temp: float) -> float:
    return temp * 9 / 5 - 459.67


def calcTemp(unitFrom: str, unitTo: str, val: float) -> float:
    if unitFrom == "K":
        if unitTo == "C":
            return k_to_f(val)
        elif unitTo == "F":
            return k_to_f(val)
    elif unitFrom == "F":
        if unitTo == "C":
            return f_to_c(val)
        elif unitTo == "K":
            return f_to_k(val)
    else:
        # unitFrom is celsius
        if unitTo == "F":
            return c_to_f(val)
        elif unitTo == "K":
            return c_to_k(val)


if __name__ == "__main__":
    uFrom = input("Convert from (K, F or C):")
    uTo = input("Convert to (K, F or C):")
    val = input("Value to be converted: ")

    calcTemp(uFrom, uTo, val)
