import paradox


def main():
    print(paradox.birthday(10000))
    monty_hall_result = paradox.monty_hall(10000)
    print(f"{monty_hall_result[0]}, {monty_hall_result[1]}")


main()
