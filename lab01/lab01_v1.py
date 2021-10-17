print("Restaurant menu")
print(""" **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
************************************** """)

print(""" ***********************************
** What would you like to order? **
***********************************""")

# constrctor
class menu: 
    def __init__(self, name, number): 
        self.name = name 
        self.number = number
# creating list       
list = [] 

list.append( {'Wings', 0} )
list.append( {'Cookies', 0})
list.append( {'Sprin Rolls',0} )



# printing intial values
for obj in list:
    print( obj )



print(""" ***********************************
** What would you like to order? **
***********************************
""")

exitFlag = False
# taking user input
while(exitFlag):
    userChose = str(input("Place your order here or type exit>>  "))
    if(userChose == "exit"):
        exitFlag= False
    for obj in list:
         if(obj.name == userChose):
          obj.number+= 1
          print("** " + str(obj.number)+" order of "+obj.name +" have been added to your meal **")

         if(userChose== 'summary'):
              for obj in list:
               print( obj.name, obj.number, sep =' ' )






