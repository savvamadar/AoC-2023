example_input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

lines = example_input.split('\n')

game_dictionary = {}

win_dictionary = {}

for line_index in range(len(lines)):
    game_dictionary[line_index] = []
    game_dictionary[line_index].append(lines[line_index].split(':')[1].split('|')[0].split()) # winning nums
    game_dictionary[line_index].append(lines[line_index].split(':')[1].split('|')[1].split()) # played nums
    win_dictionary[line_index] = 0
    for my_num in game_dictionary[line_index][1]:
        if my_num in game_dictionary[line_index][0]:
            if win_dictionary[line_index] == 0:
                win_dictionary[line_index] = 1
            else:
                win_dictionary[line_index] *= 2

print(sum(win_dictionary[k] for k in win_dictionary))
                    
    
    
