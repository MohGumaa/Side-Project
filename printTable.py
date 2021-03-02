#! python3
# printTable.py display list of list in well organized table

'''
    Fucntion Take any list and display it in clean table format
    by adding right padding width to item
'''
def printTableFormat(listItem, paddingWidth):
    print('Table'.rjust(paddingWidth))
    for row in range(len(listItem[0])):
        for col in range(len(listItem)):
            print(tableData[col][row].rjust(paddingWidth), end='')

        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']

            ]

printTableFormat(tableData, 8)
