#Food Mart Sales
#July 24

def main():
    departments = ['Produce = 1', 'Dairy = 2', 'Frozen = 3']
    for line in departments:
        print(line)
    print('Quit = 0')
    choice = int(input('Please select for which department you\'d like to enter sales for: '))
    while choice != 1 and choice != 2 and choice != 3 and choice != 0:
        print('Please enter a valid input.')
        choice = int(input('Please select for which department you\'d like to enter sales for: '))

    if choice == 1:
        produce()
    elif choice == 2:
        dairy()
    elif choice == 3:
        frozen()
    elif choice == 0:
        quit
                 
def produce():
    print('\nSales for Produce Department')
    produce = ['Salads', 'Apples', 'Oranges']
    WEEKS = 4
    produceSales = [[0 for x in range(WEEKS)] for y in range(len(produce))]

    for c in range(len(produce)):
        for r in range(WEEKS):
            sales = float(input(f'\nUnits Sold of {produce[c]} Week {r + 1}: '))
            while sales < 0:
                print('Error! Units cannot be negative. Please try again.')
                sales = float(input(f'\nUnits Sold of {produce[c]} Week {r + 1}: '))
            if sales >= 0:
                produceSales[c][r] = sales

    item_total = [0 for x in range(len(produce))]
    for r in range(WEEKS):
        for c in range(len(produce)):
            item_total[c] += produceSales[c][r]
    print(f'\nTotal Units of Salads: {item_total[0]}')
    print(f'Total Units of Apples: {item_total[1]}')
    print(f'Total Units of Oranges: {item_total[2]}')

def dairy():
    print('\nSales for Dairy Department')
    dairy = ['Milk', 'Eggs']
    WEEKS = 4
    dairySales = [[0 for x in range(WEEKS)] for y in range(len(dairy))]

    for c in range(len(dairy)):
        for r in range(WEEKS):
            sales = float(input(f'\nUnits Sold of {dairy[c]} Week {r + 1}: '))
            while sales < 0:
                print('Error! Units cannot be negative. Please try again.')
                sales = float(input(f'\nUnits Sold of {dairy[c]} Week {r + 1}: '))
            if sales >= 0:
                dairySales[c][r] = sales

    item_total = [0 for x in range(len(dairy))]
    for r in range(WEEKS):
        for c in range(len(dairy)):
            item_total[c] += dairySales[c][r]
    print(f'\nTotal Units of Milk: {item_total[0]}')
    print(f'Total Units of Eggs: {item_total[1]}')

def frozen():
    print('\nSales for Frozen Department')
    frozen = ['Pizza', 'Ice Cream']
    WEEKS = 4
    frozenSales = [[0 for x in range(WEEKS)] for y in range(len(frozen))]

    for c in range(len(frozen)):
        for r in range(WEEKS):
            sales = float(input(f'\nUnits Sold of {frozen[c]} Week {r + 1}: '))
            while sales < 0:
                print('Error! Units cannot be negative. Please try again.')
                sales = float(input(f'\nUnits Sold of {frozen[c]} Week {r + 1}: '))
            if sales >= 0:
                frozenSales[c][r] = sales

    item_total = [0 for x in range(len(frozen))]
    for r in range(WEEKS):
        for c in range(len(frozen)):
            item_total[c] += frozenSales[c][r]
    print(f'\nTotal Units of Pizza: {item_total[0]}')
    print(f'Total Units of Ice Cream: {item_total[1]}')

if __name__ == '__main__':
    main()
