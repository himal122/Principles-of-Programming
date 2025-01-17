def read_mark():

    mark = int(input("Enter your POP In-class tests mark: "))

    if mark < 0 or mark > 500:
        raise ValueError("Invalid mark")

    return mark


try:
    val = read_mark()
    print(f"Your mark is {val}")

except ValueError as e:
    print(e)
    