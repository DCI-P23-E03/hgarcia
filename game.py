#constants
C_BEGIN = "1"
C_EXPLANATION = "2"
C_EXIT = "3"


#this functions prints the menu and asks for input  
def get_menu_option():
    print("\n-----The python challenge game------")
    print("MENU")
    print("(1) Begin")
    print("(2) Explanation")
    print("(3) EXIT")
    menu_option = input("CHOOSE:")
    return menu_option
#end get_menu_option()

#this function prints a text depending to choice selected by user
def print_selection (curr_option):
    if curr_option == C_BEGIN:
        #code for Begin
        print("The game is to biuld this game. And seems to be working!") 
    elif curr_option == C_EXPLANATION:
        #code for explanation
        print("This is the explanation of how the game works. Not much to explain though. Press 1 ;)")
    else:
        #ask for a valid option
        print("Please choose a valid option from the menu")
#end print_selection()

#start of the main program----------------------------------
current_option = get_menu_option()
while current_option !=C_EXIT:

    #print selected option 
    print_selection(current_option)
    
    #ask for next option    
    current_option = get_menu_option()

#exit loop    

#print exit titles and finish program
print("Exiting game, have fun!")

#end of the main program-----------------------------------
