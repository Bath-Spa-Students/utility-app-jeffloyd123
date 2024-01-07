items = {
    "\nMenu\n" :{ "drinks\n"
                 
        "A1": {"item":"redbull " ,"price":11 ,"stock":6},
        "A2": {"item":"vodka" ,"price":24, "stock":14},
        "A3": {"item":"hot chocolate","price": 5,"stock": 9},
        "A4": {"item":"coconut water" , "price":7,"stock": 5},
        "A5": {"item":"smoothie" ,"price":9,"stock": 10},
    "-----------------------------------------------------\n"
        "snacks\n" 
        "B1": {"item":"pies " , "price":7 , "stock":4},
        "B2": {"item":"beef jerky" , "price":8 , "stock":12},
        "B3": {"item":"brownies" , "price":5 , "stock":8},
        "B4": {"item":"banana chips" , "price":4 , "stock":6},
        "B5": {"item":"salted peanuts" , "price":3 , "stock":19},

    "-----------------------------------------------------\n"
        "pastries\n"
        "C1": {"item":"croissant " , "price":3 , "stock":8},
        "C2": {"item":"cinnamon roll" , "price":5 , "stock":6},
        "C3": {"item":"macaron" , "price":2 , "stock":10},
        "C4": {"item":"apple pie" , "price":4 , "stock":13},
        "C5": {"item":"eclair" , "price":2 , "stock":7},
         
    "-----------------------------------------------------\n"
        
        "chewing gum\n"
        "D1": {"item":"Mentos" , "price":3 , "stock":9},
        "D2": {"item":"extra " , "price":2 , "stock":13},
        "D3": {"item":"Trident " , "price":4 , "stock":16},
        "D4": {"item":"wrigleys " , "price":1 , "stock":10},
        "D5": {"item":"Batook " , "price":2 , "stock":16},
    },
}

print("\nWelcome to vending machine !!!") # Welcome message

import time
time.sleep(2) #Function to add transitions between text.

#print list of the items
def print_menu(item):
    for listed, listed_items in item.items():
        print(listed + ":")
        for code, item in listed_items.items():
            print(f'{code}: {item["item"]} ({item["price"]:.2f} dhs)')
        print()

#Function to recieve valid code from user
def get_code(item):
    while True:
        code= input("input code: ")
        #To check the given code is valid or not
        for listed, listed_items in item.items():
             if code in listed_items:
                 return code
        print("Invalid code. Please try again.")

#Function to get right amount from the user 
def get_money(item, code):
    for listed, listed_items in item.items():
        if code in listed_items:
            item= listed_items[code]
            break
    else: 
        print(f'Invaild Code "{code}".')
        return 

    while True: 
        money=float(input("Enter money:"))
        if money > item["price"] or money==item["price"]:
            return money
            dispense_item(item , code , money)  
        print(
            f'Not enough money , Please insert {item["price"]- money :.2f}dhs more.'
        )

#Function to dispense list and calculate change
def dispense_item(item, code, money):
    for listed, listed_items in item.items():
        if code in listed_items:
            item= listed_items[code]
            break
        else:
            print(f'Invalid code "{code}".')
            return

#To check if item is in stock.
    if item["stock"] > 0:
        #dispense item and calculate change
        print(f'\ndispensing {item["item"]}....')
        change = money - item["price"]
        item["stock"]-= 1
        print(f"Returning {change: .2f} DHS....\n")
    else:
        print(f'\nError: {item["name"]} is out stock')

#Main Program
while True: 
    #print menu of the items
    print_menu(items)
    #To get valid code from the user
    code = get_code(items)
    #To get valid amount of money from user. 
    money = get_money(items , code)
    #Dispense item and calculate change
    dispense_item(items , code , money)

    #Prompt user to continue or exit.
    while True:
        response = input("\nWould you like to make another purchase? (yes/no)")
        if response.lower() == "yes":
            break
        elif response.lower()== "no":
          
            print("\nThankyou for using vending machine . Have a nice day !!!")
            exit()
        else: 
            print("Invaild response. Please Try again.")