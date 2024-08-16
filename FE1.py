#Food Mart Online
#July 24

def main():
    
    print('Welcome to Food Mart online!')
    print('\nProduce = 1\nDairy = 2\nFrozen Foods = 3\nCheckout = 4\nQuit = 5')
    choice = int(input('\nEnter the number of which department, to checkout, or quit: '))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        choice = int(input('Enter the number of which department, to checkout, or quit: '))
    total = 0
    
    if choice == 1:
        SALAD = 5
        APPLES = 4
        ORANGES = 3
        produce_total = 0
        
        print('\nProduce Department:')
        print(f'Salad: ${SALAD}')
        print(f'Apples: ${APPLES}')
        print(f'Oranges: ${ORANGES}')

        again = 'y'

        while again.lower() == 'y':
            produce_choice = int(input('Enter 1 for a salad, 2 for apples, 3 for oranges: '))
            again = input('Would you like to buy more produce? Enter y for yes, n for no, : ')
            if produce_choice == 1:
                produce_total += SALAD
            elif produce_choice == 2:
                produce_total += APPLES
            elif produce_choice == 3:
                produce_total += ORANGES
        if again.lower() == 'n':
            total += produce_total
            print('Back to main menu.')
            
        print('\nProduce = 1\nDairy = 2\nFrozen Foods = 3\nCheckout = 4\nQuit = 5')
        choice = int(input('\nEnter the number of which department, to checkout, or quit: '))
        while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
            choice = int(input('Enter the number of which department, to checkout, or quit: '))

    if choice == 2:
        MILK = 5
        EGGS = 4
        dairy_total = 0
        
        print('\nDairy Department:')
        print(f'Milk: ${MILK}')
        print(f'Eggs: ${EGGS}')

        again = 'y'

        while again.lower() == 'y':
            dairy_choice = int(input('Enter 1 for milk, 2 for eggs: '))
            again = input('Would you like to buy more from dairy? Enter y for yes, n for no, : ')
            if dairy_choice == 1:
                dairy_total += MILK
            elif dairy_choice == 2:
                dairy_total += EGGS
        if again.lower() == 'n':
            total += dairy_total
            print('Back to main menu.')
            
        print('\nProduce = 1\nDairy = 2\nFrozen Foods = 3\nCheckout = 4\nQuit = 5')
        choice = int(input('\nEnter the number of which department, to checkout, or quit: '))
        while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
            choice = int(input('Enter the number of which department, to checkout, or quit: '))

    if choice == 3:
        PIZZA = 7
        ICE_CREAM = 6
        frozen_total = 0
        
        print('\nFrozen Department:')
        print(f'Pizza: ${PIZZA}')
        print(f'Ice Cream: ${ICE_CREAM}')

        again = 'y'

        while again.lower() == 'y':
            frozen_choice = int(input('Enter 1 for pizza, 2 for ice cream: '))
            again = input('Would you like to buy more frozen? Enter y for yes, n for no, : ')
            if frozen_choice == 1:
                frozen_total += PIZZA
            elif frozen_choice == 2:
                frozen_total += ICE_CREAM
        if again.lower() == 'n':
            total += frozen_total
            print('Back to main menu.')

        print('\nProduce = 1\nDairy = 2\nFrozen Foods = 3\nCheckout = 4\nQuit = 5')
        choice = int(input('\nEnter the number of which department, to checkout, or quit: '))
        while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
            choice = int(input('Enter the number of which department, to checkout, or quit: '))

    if choice == 4 and total > 0:
        print(f'Your subtotal is ${total:,.2f}.')
        fee = input('Would you like pickup or delivery? ')
        if fee.lower() == 'delivery':
            distance = float(input('Enter how many miles from the store: '))
            FEE = 1.5
            CHARGE = FEE * distance
            print(f'\nDelivery fee: ${CHARGE:,.2F}')
            total += CHARGE
        
        print(f'Your total is ${total:,.2f}')
        print('\nThank you for shopping at Food Mart!')
    elif choice == 4 and total == 0:
        print('Hope to see you soon!')
            

    if choice == 5:
        print('Hope to see you soon!')
        total = 0

if __name__ == '__main__':
    main()
