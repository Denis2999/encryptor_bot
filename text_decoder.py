def crypto(text="Sometext"):
    list_text = list(text.upper())
    number_text = ""
    coordinates = []
    for i in list_text:
        for index_list, char_list in enumerate(alphabet):
            joined_str = ''.join(char_list)
            if i in joined_str:
                index_str = joined_str.index(i)
                coordinates.append(index_list)
                coordinates.append(index_str)
                # print(index_list, index_str, end=" ", sep="")
            else:
                number_text = i + i
    return coordinates


alphabet = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z', ',', '.', '!', '?', ' '],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['+', '-', '*', '/', '=', '>', ';', ':', '(', ')'],
    ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И'],
    ['Й', 'К', 'Ч', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С'],
    ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
    ['Э', 'Ю', 'Я', 'Ї', 'Є', 'І', 'Ґ', 'Ą', 'Ć', 'Ę'],
    ['Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż', '%', '@', '#', '№'],

]

coord = crypto('''
НЧЕПWBŹГĆ
''')

# print("coord ", coord)

coord_1 = [coord.pop(0) for i in range(int(len(coord) / 2))]
# print("coord_1", coord_1)
coord_2 = coord
# print("coord_2", coord_2)

for i in range(len(coord_1)):
    coord_2.insert(i * 2, coord_1[i])
# print(coord_2)

half_coord_1 = coord_2[::2]
half_coord_2 = coord_2[1::2]

for i, j in zip(half_coord_1, half_coord_2):
    print(alphabet[i][j], end="")
