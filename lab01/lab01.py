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

list.append( menu('Wings', 0) )
list.append( menu('Cookies', 0) )
list.append( menu('Sprin Rolls', 0) )

# printing intial values
for obj in list:
    print( obj.name, sep =' ' )



print(""" ***********************************
** What would you like to order? **
***********************************
""")

exitFlag = True
# taking user input
while(exitFlag):
    userChose = str(input("Place your order here or type exit>>  "))
    if(userChose == "exit"):
        exitFlag= False
    for obj in list:
         if(obj.name == userChose):
          obj.number+= 1



for obj in list:
    print( obj.name, obj.number, sep =' ' )



