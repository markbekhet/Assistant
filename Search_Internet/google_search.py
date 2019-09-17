
from defs import *
from conversation import *

try: 
	from googlesearch import search
	import webbrowser 

except ImportError: 
	print("No module named 'google' found") 






def opening_tabs(site_url):
	webbrowser.open_new_tab(site_url) 



	
def ask(type_of_input):	
	query = typing_or_saying_the_question(query_, type_of_input)
	
	return query

def use_certain_links(links, action , type_of_input):			#The parameter of this function is the list of links
	
	# the action parameter is used in a wrong way but i don't find another solution 
	# this variable helps to specify the number ofthe links wanted to be saved
	number_of_wanted_links = typing_or_saying_the_question(number_of_wanted_links_ , type_of_input) 
	if("none" in number_of_wanted_links.lower()):
		number_of_wanted_links = 0

	else:
		number_of_wanted_links = int(number_of_wanted_links)
	# the result of this question is a string so I  have to convert it to an integer
			
	# the number of links already saved
	already_used = 0
	saved_links = []
	while(already_used < number_of_wanted_links and number_of_wanted_links > 0 ):
		#The link number of the list called links
		link_number = typing_or_saying_the_question(link_number_ , type_of_input)
					
		number_wanted = int(link_number) - 1
		if(action == action_[0]):
			saved_links.append(links[number_wanted])
		
		elif(action == action_[1]):
			opening_tabs(links[number_wanted])

		already_used += 1



	return saved_links
	
#this function is to ask the question and to make the choice between voice and keyboard input
# This block will be repeated a lot of time so I will  make a function to make it more estatic
# This block allows to ask the question by voice or without
# It is a bad choice to build an if statement based on a parameter but I don't have
# another choice
def typing_or_saying_the_question(question, type_of_input):
	answer = ""
	if(type_of_input == type_of_input_[0]):
		answer = input(question)
	# Ask the question with the voice
	elif(type_of_input == type_of_input_[1]):
		answer = input_audio(question)

	return answer



def getting_links(query, type_of_input):
	speak.Speak(links_)
	
	links = []
	number_of_links = 0
	#I will use this variable as return value and it<s better to be here because if I want more than ten links
	saved_links = []
	# to search 
	for j in search(query, tld="co.in", num=10, stop=None, pause=0): 
		print(j)
		links.append(j)
		number_of_links += 1
	# a limit of 10 links to limit the number of tabs to not use all of the RAM
		if(number_of_links == 10):
			open_tabs = typing_or_saying_the_question(open_tabs_, type_of_input)
			# a possibility to open the tabs 
			if("y" in open_tabs.lower()):
				for link in links:
					opening_tabs(link)


			elif("n" in open_tabs.lower()):
				use_certain_links(links , action_[1], type_of_input)


			# a question to see which links to save
			save = typing_or_saying_the_question(save_links_, type_of_input)
			if ("y" in save.lower()):
				for link in links :
					saved_links.append(link)


			elif ("n" in save.lower() ):             
				temp_saved_links = use_certain_links(links , action_[0] , type_of_input)
				saved_links.append(temp_saved_links)

			

			# a question to see if those sites are enough or not
			keep_going = typing_or_saying_the_question(keep_going_)
			if("n" in keep_going.lower()):
				proceed = False
				break

			
			else :
				links = []
				number_of_links = 0


	return saved_links



			
			
def new_search(type_of_input):
	query = ask(type_of_input)
	links = getting_links(query , type_of_input)
	return links


type_of_input = typing_or_saying_the_question(question_type_of_input_, type_of_input_[1])
if(type_of_input_[1] in type_of_input):
	type_of_input = type_of_input_[1]

elif(type_of_input_[0] in type_of_input):
	type_of_input = type_of_input_[0]




new_search(type_of_input)