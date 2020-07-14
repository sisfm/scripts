stock={"PEN":["Lana Pen",5],
       "TSHIRT":["Lana T-Shirt",20],
       "MUG":["Lana Coffee Mug",7.5]}


basket={}

#Display User Menu
def userLogin():
    print("*****************************************MENU*******************************************")
    print("1.Display Stock")
    print("2.Add Item to Basket")
    print("3.Remove Item From Basket")
    print("4.Display Backet")
    print("5.Get the discount and total Amount")
    print("6.Empty Basket")
    print("****************************************************************************************")

#Display User Stock
def userDisplayStock():
    global stock
    print("****************************************STOCK*******************************************")
    print("****************************************************************************************")
    print("Id\t\tName\t\t\tPrice")
    for item in stock:
        print(f"{item}\t\t{stock[item][0]}\t\t\t{stock[item][1]}")
    print("\n")

#Print Basket
def userPrintBasket():
    global basket
    print("****************************************BASKET******************************************")
    print("Id\t\tName\t\tQuantity\t\tPrice\t\tComment")
    print("****************************************************************************************")
    for item in basket:
        print(f"{item}\t\t{basket[item][0]}\t\t{basket[item][1]}\t\t{basket[item][2]}")
    print("****************************************************************************************")

                       
def addItem():
    global basket
    enterId=str(input("Enter id to buy: "))
    if enterId in stock:
        if enterId in basket:
            print ("Item already in Basket")
            qnty=int(input("Enter Quantity to add: "))
            basket[enterId][1]+=qnty #Record quantity
            basket[enterId][2]=(basket[enterId][1]*stock[enterId][1]) #Record Total Price
        else:
            print ("item not in Basket")
            qnty=int(input("Enter Quantity: "))
            total=(qnty*stock[enterId][1])
            basket.update({enterId:[stock[enterId][0],qnty,total]})  #Add new item to basket
    else:
        print ("Item not in Stock. Select another item")
        userDisplayStock()
        addItem()
        
def removeItem():
    userPrintBasket()
    removeId=str(input("Enter the id need to be deleted : "))
    if removeId in basket:
        del basket[removeId] #Remove item from Basket
    else:
        print ("Item not in Basket. Select another item")
    userPrintBasket()
    login()

def getTotal():
    total=0
    print("**************************************CHECK OUT*****************************************")
    print("Id\t\tName\t\tQuantity\t\tPrice\t\tComment")
    print("****************************************************************************************")
    for item in basket:
        if item == "PEN": #Check if the Item is PEN to apply discount
            if basket[item][1]%2 == 0:
                totalPen=(basket[item][1]/2*stock[item][1]) #Apply 2x1 discount
                print(f"{item}\t\t{basket[item][0]}\t\t{basket[item][1]}\t\t{totalPen}\t\t*2x1 APPLIED")
                total+=totalPen
            else:
                print(f"{item}\t\t{basket[item][0]}\t\t{basket[item][1]}\t\t{basket[item][2]}")
                total+=basket[item][2]

        elif item == "TSHIRT": #Check if the Item is TSHIRT to apply discount
            if basket[item][1] >= 3:
                totalTshirt=(basket[item][1]*stock[item][1]*0.75) #Apply 25% discount
                print(f"{item}\t\t{basket[item][0]}\t\t{basket[item][1]}\t\t{totalTshirt}\t\t*25% DISCOUNT APPLIED")
                total+=totalTshirt
            else:
                print(f"{item}\t\t{basket[item][0]}\t\t{basket[item][1]}\t\t{basket[item][2]}")
                total+=basket[item][2] 
        else:
                print(f"{item}\t\t{basket[item][0]}\t\t{basket[item][1]}\t\t{basket[item][2]}")
                total+=basket[item][2]
    print("****************************************************************************************")
    print(f"TOTAL: {total}")
    login()
    
def clearBasket():
    global basket
    basket={} #Clear Baket
    login()



def userChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        userDisplayBasket()
        userLogin()
        userChoice()
    elif choice==2:
        addItem()
        userLogin()
        userChoice()
    elif choice==3:
        removeItem()
        userLogin()
        userChoice()
    elif choice==4:
        userPrintBasket()
        userLogin()
        userChoice()
    elif choice==5:
        getTotal()
        userChoice()
    elif choice==6:
        clearBasket()
    else:
        print("Invalid Choice. Please enter valid choice")
        userLogin()
        userChoice()
            

def login():
    userLogin()
    userChoice()
    
login()
