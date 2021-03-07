#! python3
# printTable.py display list of list in well organized table

'''
    Fucntion Take any list and display it in clean table format
    by adding right padding width to item
'''
def printTableFormat(listItem, paddingWidth):
    print('Table'.rjust(8))
    for row in range(len(listItem[0])):
        for col in range(len(listItem)):
            print(tableData[col][row].rjust(paddingWidth[col]), end=' ')


        print()

'''
    Function to find longest string in inner list
'''

def longestString(listItem):
    colWidths = []

    for items in listItem:
        max = 0
        # Loop through inner list to find longest item
        for item in items:
            if len(item) > max:
                max = len(item)
        colWidths.append(max)
    return colWidths

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['name', 'ali', 'majed', 'omer']
            ]



colWidths = longestString(tableData)
printTableFormat(tableData, colWidths)
