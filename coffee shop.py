print("---Welcome to Aui's Coffee---")     
def coffee(coffee):
    coffee_sel=""
    if coffee == 1:
        coffee_sel+="Espresso"
    if coffee == 2:
        coffee_sel+="Capucino"
    if coffee == 3:
        coffee_sel+="Latte"
    return coffee_sel

def type_coffee(type_sel):
    type_c=[]
    
    if type_sel == 1:
        type_c.append("Hot")
        type_c.append(55)
    if type_sel == 2:
        type_c.append("Cold")
        type_c.append(60)
    return type_c
  
    #def1  MENU PROGRAM
print(" ")
number=int(input("Please type 1 to show menu:"))
if number == 1:
    print(" ")
    print("---Choose the menu---")
    print("1.Espresso")
    print("2.Cappucino")
    print("3.Latte")   
    #def2 SELECT COFFEE PROGRAM
    coffee_sel=""
    print(" ")
    sel_coffee=int(input("Select coffee:"))
    coffee_sel=(coffee(sel_coffee))
  
    #def3 SELECT TYPE PROGRAM
    print(" ")
    print("--Choose the type of the coffee--")
    print("1.Hot 55 baht")
    print("2.Cold 60 baht")
    ls_type=[]
    print(" ")
    type_sel=int(input("Select type:"))
    ls_type=type_coffee(type_sel)

    print("---You chose",ls_type[0],coffee_sel,ls_type[1],"baht---")

    # cash 
    print(" ")
    money=int(input("Input your money:"))
    cash=0
    cash=ls_type[1]
    if money > cash:
      result=money-cash
      print("You recieved a chang of %d baht"%result)
      print("--Thank you--")
    elif money == cash:
      print("--Thank you--")
    else:
      print("Not enough money")
      print("Please try again")

else:
  print("Sorry,someting went wrong")