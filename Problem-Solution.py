#Imported libraries required for random selection and time delay
import random
import time

#The list that will hold the user input options
the_options = []

#Function that generates the options based on user input
def generate_options():
    #Calls the global variable the_options to be used within the function
    global the_options
    #Prompts the user to input the number of options they want to enter
    user_input = input("How many options will you input?")

    #Prevents invalid inputs and prompts the user to enter a valid number
    try:
        #Makes sure the user input is a positive integer greater than 1
        if int(user_input) <= 1:
            print("Please enter a positive number greater than 1.")
            #recalls the function to try again
            generate_options()

        else:
            #Converts user input from a string to an integer
            user_input = int(user_input)
            #Prompts the user to enter each option and appends it to the list of options
            for i in range(user_input):
                #Prompts the user to enter an option and appends it to the list of options
                option = input(f"Enter option {i + 1}: ")
                the_options.append(option)
                #Prints the current list of options after each entry
                print(the_options)
            #Prints a message indicating that the list has been generated successfully and that the program will now process
            print("List generated successfully! Now processing complex decision making and generating results...")
            time.sleep(3)
            complex_decision_making()
            
    #Handles the case where the user enters a non-integer value
    except ValueError:
        print("Please enter a valid number.")
        #recalls the function to try again
        generate_options()

#Randomly selects an option from the list of options
def complex_decision_making():
    #Calls the global variable the_options to be used within the function
    global the_options
    #Randomly selects an option from the list of options and prints it
    selected_option = random.choice(the_options)
    print(f"After complex decision making, the selected choice is: {selected_option}")

#Main function that initiates the program
generate_options()