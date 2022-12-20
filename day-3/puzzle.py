
letters = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

letter2Priority = {}
i = 1
for x in letters:
    letter2Priority[x] = i
    i = i + 1

# Part One
with open('input-data.txt', 'r') as file:
    sum = 0
    for line in file:
        leftpart = []
        rightpart = []
        half = len(line.strip()) / 2
        i = 1
        for x in line.strip():
            if i <= half:
                leftpart.append(x)
            else:
                rightpart.append(x)
            i = i + 1
        sum = sum + letter2Priority[set(leftpart).intersection(rightpart).pop()]
    print(sum)

# Part Two
with open('input-data.txt', 'r') as file:
    sum = 0
    index_groups = {}
    index = 1
    i = 1
    for line in file:
        if i <=3:
            i = i + 1
            group = index_groups.get(index)
            if group is not None:
                group.append(line.strip())
            else:
                group = [line.strip()]
                index_groups[index] = group
        else:
            i = 1
            index = index + 1

    for k, v in index_groups.items():
        for x in v:
            pass
