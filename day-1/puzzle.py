with open('input_data.txt', 'r') as file:
    elven_supplies = []
    current_elf_total = 0

    for line in file:
        if line not in ('\n', '\r\n'):
            current_elf_total += int(line)
        else:
            elven_supplies.append(current_elf_total)
            current_elf_total = 0

    elven_supplies.sort(reverse=True)
    max_elven_cal = elven_supplies[0]
    top_three_sum = 0

    for x in range(3):
        top_three_sum += elven_supplies[x]

    print('max_elven_cal =', max_elven_cal)
    print('top_three_sum =', top_three_sum)
