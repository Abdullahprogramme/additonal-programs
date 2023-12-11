# Advent of code problem number 1 starts here #
with open('C:\Personal Files\OneDrive - Habib University\Python\Extra\\numbers.txt', 'r') as f:
    fh = f.readlines()
    sum_num = 0
    lst = []
    for line in fh:
        for ch in line.strip():
            if ch.isnumeric(): lst.append(ch)
        sum_num += int(lst[0] + lst[-1])
        lst = []
print(sum_num)
f.close()
# Advent of code problem number 1 ends here #
