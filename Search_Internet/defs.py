from enum import *
import os
#This file will contain all the constants of my program
#To seperate a constant from a variable in the program
#The constant will be marked with an underscore after it's name
query_ = "what do you want to search for? "
links_ = "The possible sites for this search are :"
action_ =("save" , "open")
link_number_ = "What is the number of the link wanted to be saved or opened ?"
number_of_wanted_links_ = "How many links do you want to save or open ?  "
open_tabs_ = "Do you want to open those links ? (Y/N) "
save_links_ = "Do you want to save all those links? (Y/N)"
keep_going_ = "Do you want to continue to search ? (Y/N)"
voice_error = "sorry I didn't recognize your voice . Can you repeat what you said ? "  
type_of_input_ = ("keyboard" , "voice")
question_type_of_input_ = "How do you want your assistant to help you by keyboard input or voice input ? say " + type_of_input_[0] + " or " + type_of_input_[1]
