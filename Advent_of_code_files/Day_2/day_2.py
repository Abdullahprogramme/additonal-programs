# Advent of code problem number 2 starts here #
with open('C:\Personal Files\OneDrive - Habib University\Python\Extra\elfs.txt', 'r') as f:
    fh = f.readlines()
    game_sum = 0
    for line in fh: # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        flag = True
        game_number = line[5]
        lst = line[8:].split(";") # >= 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        for items in lst: # 1 blue, 2 green
            item_list = items.strip().split(',')
            for colour in item_list: # 1 blue  # 2 green
                if 'blue' in colour:
                    if int(colour.strip()[:2]) >= 14: flag = False
                if 'red' in colour:
                    if int(colour.strip()[:2]) >= 12: flag = False
                if 'green' in colour:
                    if int(colour.strip()[:2]) >= 13: flag = False
        if flag is False: flag = True
        else: game_sum += int(game_number)
print(game_sum)
f.close()
# Advent of code problem number 2 ends here #
