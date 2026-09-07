#Imported libraries required for random selection and time delay
import random
import time

#The list that will hold the user input options
the_options = []

#Function that generates the options based on user input
def generate_options():
    global the_options
    user_input = input("How many options will you input?")

    #Prevents invalid inputs and prompts the user to enter a valid number
    try:
        #Makes sure the user input is a positive integer greater than 1
        if int(user_input) <= 1:
            print("Please enter a positive number greater than 1.")
            generate_options()

        else:
            #Converts user input from a string to an integer
            user_input = int(user_input)
            #Prompts the user to enter each option and appends it to the list of options
            for i in range(user_input):
                option = input(f"Enter option {i + 1}: ")
                the_options.append(option)
                print(the_options)
            
            print("List generated successfully! Now processing complex decision making and generating results...")
            time.sleep(3)
            complex_decision_making()
            
    #Handles the case where the user enters a non-integer value
    except ValueError:
        print("Please enter a valid number.")
        generate_options()

#Randomly selects an option from the list of options
def complex_decision_making():
    global the_options
    selected_option = random.choice(the_options)
    print(f"After complex decision making, the selected choice is: {selected_option}")

#Main function that initiates the program
generate_options()