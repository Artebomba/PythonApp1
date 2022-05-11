def EnterProducts():
    DataBying = {}
    DetailsEnter = True
    while DetailsEnter:
        details = input("Press A to add a product, Q to quit: ")
        if details == "A" or details == "a":
            product = input("Enter a product (object): ")
            quantity = int(input("Enter quantity (total amount): "))
            DataBying.update({product: quantity})
        elif details == "Q" or details == "q":
            DetailsEnter = False
        else:
            print("Enter a property option!")
    return DataBying

def getPrice(product, quantity):
    priceData = {
        "Apple": 2,
        "Banana": 4,
        "Tomato": 3,
        "Bean": 1.5,
        "Potato": 2.2
    }
    subtotal = priceData[product] * quantity 
    if quantity >=2:
        print("Here are", product + '(s/es): $' + str(priceData[product]) + 'x' + str(quantity) + '=' + '$' + str(subtotal))
    else:
        print("Here is", product + ': $' + str(priceData[product]) + 'x' + str(quantity) + '=' + '$' + str(subtotal) )
    return subtotal
    
def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount = billAmount * 0.8
            discount = 20
        elif membership == "Silver":
            billAmount = billAmount * 0.9
            discount = 10    
        elif membership == "Bronze":
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + '% off for ' + membership + ' ' + 'membership on total amount: $' + str(billAmount))
    else:
        print("No discount on amount less than $25")
    return billAmount

def makeBill(DataBying, membership):
    billAmount = 0
    for key, value in DataBying.items():
        billAmount += getPrice(key,value)
    billAmount = getDiscount(billAmount, membership)
    print("The discounted amount is $" + str(billAmount))
    
DataBying = EnterProducts()
membership = input("Enter your membership: ")
makeBill(DataBying, membership)