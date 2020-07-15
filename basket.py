import copy
stock={"PEN":["Lana Pen",5],
       "TSHIRT":["Lana T-Shirt",20],
       "MUG":["Lana Coffee Mug",7.5]}

basket={} #Set empty Basket
                       
def addItem(basket,stock):
    error=None
    enterId=str(input("Enter id to buy: "))
    if enterId in stock:
        if enterId in basket:
            qnty=int(input("Item already in Basket. Enter Quantity to add: "))
            basket[enterId][1]+=qnty #Record quantity
            basket[enterId][2]=(basket[enterId][1]*stock[enterId][1]) #Record Total Price
        else:
            qnty=int(input("Item not in Basket. Enter Quantity: "))
            total=(qnty*stock[enterId][1])
            basket.update({enterId:[stock[enterId][0],qnty,total]})  #Add new item to basket
    else:
        error="Item not in Stock. Select another item"
    return basket,error

def removeItem(basket):
    error=None
    removeId=str(input("Enter the id need to be deleted : "))
    if removeId in basket:
        del basket[removeId] #Remove item from Basket
    else:
        error="Item not in Basket. Select another item"
    return basket,error

def checkout(basket,stock):
    temp=copy.deepcopy(basket)
    for item in temp:
        if item == "PEN": #Check if the Item is PEN to apply discount
            if temp[item][1]%2 == 0:
                temp[item][2]=(temp[item][1]/2*stock[item][1]) #Apply 2x1 discount
                temp[item].append("*2x1 discount")
        elif item == "TSHIRT": #Check if the Item is TSHIRT to apply discount
            if temp[item][1] >= 3:
                temp[item][2]=(temp[item][1]*stock[item][1]*0.75) #Apply 25% discount
                temp[item].append("*25% discount")
    return temp
    
def clearBasket(basket):
    basket={} #Clear Basket
    return basket
    
def userChoice():
    global basket
    choice=int(input("Please enter user choice : "))
    if choice==1:
        userDisplayStock(stock)
        userLogin()
        userChoice()
    elif choice==2:
        basket,error=addItem(basket,stock)
        if error is not None:
            printError(error)
        userLogin()
        userChoice()
    elif choice==3:
        basket,error=removeItem(basket)
        if error is not None:
            printError(error)
        userLogin()
        userChoice()
    elif choice==4:
        userPrintBasket(basket)
        userLogin()
        userChoice()
    elif choice==5:
        temp=checkout(basket,stock)
        userPrintCheckout(temp)
        clearBasket(basket)
        userLogin()
        userChoice()
    elif choice==6:
        basket=clearBasket(basket)
        userLogin()
        userChoice()
    else:
        print("Invalid Choice. Please enter valid choice")
        userLogin()
        userChoice()
            

def login():
    userLogin()
    userChoice()

#Display User Menu
def userLogin():
    print("*****************************************MENU*******************************************")
    print("1.Display Stock")
    print("2.Add Item to Basket")
    print("3.Remove Item From Basket")
    print("4.Display Basket")
    print("5.Checkout")
    print("6.Empty Basket")
    print("****************************************************************************************")

#Display User Stock
def userDisplayStock(stock):
    print("****************************************STOCK*******************************************")
    print("Id\t\tName\t\t\tPrice")
    print("****************************************************************************************")
    for item in stock:
        print(f"{item}\t\t{stock[item][0]}\t\t{stock[item][1]}")
    print("\n")

#Print Basket
def userPrintBasket(cart):
    print("****************************************BASKET******************************************")
    print("Id\t\tName\t\tQuantity\t\tPrice\t\tComment")
    print("****************************************************************************************")
    for key,value in cart.items():
        print(f"{key}\t\t", end='')
        for item in value:
            print(f"{item}\t\t", end='')
        print("\n")
    print("****************************************************************************************")

def userPrintCheckout(cart):
    total=0
    print("***************************************CHECKOUT*****************************************")
    print("Id\t\tName\t\tQuantity\t\tPrice\t\tComment")
    print("****************************************************************************************")
    for key,value in cart.items():
        print(f"{key}\t\t", end='')
        for item in value:
            print(f"{item}\t\t", end='')
        total+=cart[key][2]
        print("\n")
    print("****************************************************************************************")
    print(f"TOTAL: ${total}")
    print("****************************************************************************************")

def printError(error):
    print(error)

if __name__ == '__main__':
    login()