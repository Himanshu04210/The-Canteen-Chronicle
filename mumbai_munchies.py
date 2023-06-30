
invetory = [];

soldSnack = [];

class Snacks:
    
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability
        
        
        
def addSnack():
    snackId = int(input("Enter snack_id : "))
    name = str(input("Enter snack name : "))
    price = int(input("Enter Snack price : "))
    availability = bool(input("Enter availability (True/False) : "))
    
    snack = Snacks(snackId, name, price, availability)
    invetory.append(snack);
    return "Snack added successfully";


def deleteSnack():
    snackId = int(input("Enter snack_id : "))
    
    for i in invetory:
        if i.snack_id == snackId:
            invetory.remove(i);
            return "Snack removed successfully";
        
    return f"Snack not present with this snackId {snackId}"; 

def updateSnack():
    
    snackId = int(input("Enter snack_id : "))
    name = str(input("Enter snack name : "))
    price = int(input("Enter Snack price : "))
    availability = bool(input("Enter availability (True/False) : "))
    
    for i in invetory:
        if i.snack_id == snackId:
            i.name = name;
            i.price = price;
            i.availability = availability;
            return "Snack updated successfully";
    
    return f"Snack not present with this snackId {snackId}"; 

def buySnack():
    name = str(input("Enter snack name : "))
    for i in invetory:
        if i.name == name:
            if i.availability == "False" : return "Not available right now";
            print(f"price of the snack is {i.price}")
            money = int(input("Enter money : "))
            if(money >= i.price) :
                soldSnack.append(i);
                return("You buy the snack");
            else :
                return("Not have sufficient money")
    return f"{name} is not present";

def getAllTheSnack() :
    for i in invetory:
        
        print(f"Snack: Id- {i.snack_id}, Name-{i.name}, Price- {i.price}, Availability- {i.availability}")


def start() :
    
    while True:
        print("select choice")
        print("0. exit")
        print("1. Add a snack")
        print("2. Update a snack")
        print("3. Delete a snack")
        print("4. Buy a snack")
        print("5. See all the snack")
        
        choice = int(input("Enter your choice : "))
        if(choice == 1):
            print(addSnack())
        elif choice == 2:
            print(updateSnack())
        elif choice == 3:
            print(deleteSnack())
        elif choice == 4:
            print(buySnack())
        elif choice == 5:
            getAllTheSnack();
        else :
            print("Invalid choice, Enter again")
    

    
start();