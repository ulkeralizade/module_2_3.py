my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0

while True:
    if i >= len(my_list):
        break

    number = my_list[i]

    if number < 0:
        break

    if number == 0:
        i += 1
        continue

    print(number)
    i += 1
