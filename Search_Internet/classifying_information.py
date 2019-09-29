from google_search import *

class ManagingFile:
        def __init__(self, fileName):
                self.fileName = fileName

        # In this method i will try to find the word given in parameter in the file that i want
        # this function will return an integer which will be the position of the given word 
        def reachWord(self, word)-> int :
                designedWord = "-"+ word
                file = open(self.fileName , "r")
                file.seek(0,0)
                line = file.readline()
                position = 0
                # The searching prcess in the loop
                while line != designedWord :
                        line = file.readline()

                position = file.tell()
                # I close the file at the end of the function for security reasons
                file.close()
                return position


        # This function will get the information which are under the category name
        def gettingInfo(self,word)->set:
                data = []
                designedWord = "-"+ word
                position = reachWord(fileName, designedWord)
                file = open(self.fileName,"r")
                file.seek(position, 0)
                line = file.readline()
                while "- " not in line : 
                        line = file.readline()
                        if "- " not in line :
                                data.append(line)


                file.close()
                data_set = set(data)
                return data_set


        # Hold this function because i may not use it
        def deletingInfo(self,word)->None:
                
                designedWord = "-"+ word
                position = reachWord(self.fileName,designedWord)
                file = open(self.fileName,"w+")
                file.seek(position,0)
                line = ""
                while "- " not in line : 
                        position_line = file.tell()
                        line = file.readline()
                        if "- " not in line or line == "" :
                                file.seek(position_line , 0)
                                file.write("")

                file.close()

        # This function is made to verify that i have the category in the written in the file
        # This function is used as a safe function  
        def existInTheFile(self, word)-> bool:
                file = open(self.fileName,"r")
                line = file.readline()
                while line != "" :
                        if line == word :
                                file.close()
                                return True

                        line = file.readline()

                file.close()
                return False
                




        def writing_links(self,category):
                # I do not need to open the file in writing mode before checking an existing file 
                # file = open(file_name,"a+")
                first_line = "- " + category
                #I will try to execute the function to check if the title exists and if it throws an exception the file will be created
                already_existed = True
                try:
                        already_existed = existInTheFile(self.fileName , first_line)
                except IOError :
                        print("this is a new file to be created")

                # if the file doesn't exist or the name of the category is wrong so i will open the file in appending mode and i will write the result of the search process in the file
                if already_existed == False or IOError :
                        file  = open(self.fileName, "a+")
                        file.write(first_line)
                        data = getting_links()
                        for url in data :
                                file.write("\n")
                                file.write(url)

                        file.close()
                else :

                        already_saved = gettingInfo(self.fileName, first_line)
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
                        
                        

                        file =open(self.fileName, "w+")
                        #saving the undiplacted links into the file
                        #this will rewrite the information in the file under the specified category
                        position = self.deletingInfo(self.fileName, first_line)
                        file.seek(position,0)
                        file.write("\n") 
                        for url in already_saved :
                                file.write(url)
                                file.write("\n")
                        

                file.close()
        










			
		
