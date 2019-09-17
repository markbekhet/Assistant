from google_search import *



def reach_word(file_name, word) :
        file = open(file_name , "r")
        file.seek(0,0)
        line = file.readline()
        position = 0
        while line != word :
                line = file.readline()
        position = file.tell()
        return position


        
def getting_info(file_name,word):
        file = open(file_name,"r")
        data = []
        line = file.readline()
        position = reach_word(file_name, word)
        file.seek(position, 0)
        while "- " not in line : 
                line = file.readline()
                if "- " not in line :
                        data.append(line)


        file.close()
        data_set = set(data)

        
        return data_set


# Hold this function because i may not use it
def deleting_info(file_name,word):
        file = open(file_name,"w+")
        
        position = reach_word(file_name,word)
        file.seek(position,0)
        while "- " not in line : 
                position_line = file.tell()
                line = file.readline()
                if "- " not in line or line == "" :
                        file.seek(position_line , 0)
                        file.write("")

        file.close()


def exist_in_the_file(file_name, word):
        file = open(file_name,"r")
        line = file.readline()
        while line != "" :
                if line == word :
                        file.close()
                        return True

                line = file.readline()

        file.close()
        return False
                




def writing_links(file_name,category):
        # I do not need to open the file in writing mode before checking an existing file 
         # file = open(file_name,"a+")
        first_line = "- " + category
        #I will try to execute the function to check if the title exists and if it throws an exception the file will be created
        already_existed = True
        try:
                already_existed = exist_in_the_file(file_name , first_line)
        except IOError :
                print("this is a new file to be created")

        if already_existed == False or IOError :
                file  = open(file_name, "a+")
                file.write(first_line)
                data = getting_links()
                for url in data :
                        file.write("\n")
                        file.write(url)

                file.close()
        else :

                already_saved = getting_info(file_name, first_line)
                #==================================================================================================================================================================#
                #this variable describes the new data obtained by the search
                data = new_search()
                # this variable is used to have the new data without duplication using the double 
                # for loop because it can happen that the link will be appearead twice if i will do the same search engine
                #or the same words to search for something

                #Finally to avoid duplication i will use a set 

                data_set = set(data)
                already_saved.union(data_set)
                #length_already_saved = len(already_saved)
                
                #new_one = []
                #for info in data:
                #        number = 0
                #        for url in already_saved:
                #                if(url != info):
                #                        number += 1

                #        if number == length_already_saved :
                #                new_one.append(info)

                file =open(file_name, "w+")
                #saving the undiplacted links into the file
                position = reach_word(file_name, first_line)
                file.seek(position,0)
                file.write("\n") 
                for url in already_saved :
                        file.write(url)
                        file.write("\n")
                        

                file.close()
        










			
		
