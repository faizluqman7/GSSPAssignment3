import sys
#importing random to generate a random confirmation number when the user buys a product
import random

#product class to store the data type of product objects
class Product:
	#initializer/constructor to create and initialize the product name and price
	def __init__(self, productName, productPrice):
		#set the name and price to a certain value by taking in the parameters in the constructor
		self.__Name = productName
		self.__Price = productPrice
		
#returns the name of the product to the object calling it
	def getName(self):
		return self.__Name
		
#returns the name of the price of the product object to the object calling it
	def getPrice(self):
		return self.__Price


		
#the MAIN application class HERE
class ProductManager:
	#constructor to begin taking input and display outputs to user
	def __init__(self):
		#products instance variable to store the product data type
		#this instance variable is storing OBJECTS 
		self.__products = []

		#welcome message and prompt to the user to begin the program
		sys.stdout.write("Welcome to the Shopada E-Commerce Platform! \nPress [A] to search for an item \nPress [B] to add a new item. \nPress any other key to terminate the program \nEnter choice: ")
		sys.stdout.flush()
		choice = sys.stdin.readline().strip()
		
		#while the user inputs A or B, the program runs repeatedly until the user
		#stops, by entering any other character other than A or B
		#A if the customer wants to search for an item in the catalog
		#B if the customer wants to add new item to the catalog
		while choice =="A" or choice=="B":
			#Search for item if choice is A
			if choice=="A":
				sys.stdout.write("Please enter your search query: ")
				sys.stdout.flush()
				#the item (search query) the user wants to find in the catalog
				search_query = sys.stdin.readline().strip()
				
				#prompt and input for asking the user which database/which catalog
				#in this case which file the user wants to search for the product from
				sys.stdout.write("Please enter the name of the file you would like to search your items from: ")
				sys.stdout.flush()
				#name of the file of the product user wants to search from, will be called through the validateFileName method and the name of file will be validated there
				filename = self.__validateFileName()

			
				#try to open the file the user specifies previously
				try:
					#file variable is the file object
					file = open(filename, "r")
					#read from the opened file
					file_contents = file.readline()
					#keep reading the file until last line which is blank
					while file_contents!="":
						#split the file contents into a list of product name and product price, index 0 is the name and 1 is the price
						file_contents_splitted = file_contents.split(",")
						#create a new product OBJECT when the product is read from file
						product_object = Product(file_contents_splitted[0].strip(), file_contents_splitted[1].strip())
						#store the products OBJECT into the products instance variable declared at the start of this constructor
						self.__products.append(product_object)
						#read the next line and repeat until no more lines
						file_contents = file.readline()
					#close file after all operations done
					file.close()
				#if user specifies a file that does not exist, this exception will catch it		
				except:
					sys.stdout.write("File does not exist!")

				
				#process of searching through one by one of all the products in the products list of items to match the user's search query
				#search counter necessary to check what index is currently now searching
				search_counter = 0
				#found variable is necessary to indicate if the product is found AT ALL inside the file
				#this is needed to display appropriate message later on.
				found = False
				#loop through the list of products sequentially to find the matching product with the user's search query
				while search_counter < len(self.__products) and found == False:
					#if the product is found in the file, the index of the item is set to
					#the location of where the product was found
					#get the name of the products from the products instance variable
					if self.__products[search_counter].getName() == search_query:
							#item found
							#item_index is the location of the item found in the array
						item_index = search_counter
						#found set to true to stop the loop AND display the 
						#appropriate message afterwards
						found = True
						#search counter incremented to search in the index of the next
						#location in the list
					search_counter+=1
					
					#when the product is not found at last after looping through the entire
					#array, the next option will be to exit the search phase,
					#so therefore a message will prompt later on whether the user wants to add new item to
					#the file
				if found == False:
					sys.stdout.write("Product not found! \n")
					next_option = "Exit"
					#if the product is found, a new menu will display to ask the user what
					#the user wants to do after they found the product.
				else:
					sys.stdout.write("Product found! \nWhat would you like to do with this product? \n[A]Buy It Now! \n[B]Check Price  \nEnter your choice: ")
					sys.stdout.flush()
					#next option will be either A or B whether the user wants to buy the product (A) or
					#just to check the price
					next_option = sys.stdin.readline().strip()

					#this is to validate the inputs, the user will enter either capital A or B as
					#specified by the user guide. IF not, this loop will keep asking the user to try again.
					while choice !="A" and choice!="B":
						sys.stdout.write("Invalid! Please enter a correct character, A or B: ")
						sys.stdout.flush()
						next_option = sys.stdin.readline().strip()

				
				#if the result of next_option is A,
				#then the user will buy the product
				if next_option =="A":
					#buy it now
					#a random confirmation number is generated as the user buys the product
					#followed by a message to the user
					#item index indicates the location of the item inside the products list
					#so therefore the product will be displayed to the user
					confirmation_number = random.randint(1,99999)
					sys.stdout.write("Successfully bought "+self.__products[item_index].getName()+"! \nThank you for your purchase! Your confirmation number is "+str(confirmation_number)+"\nThank you for shopping with Shopada! \n")
					
					#if the user chooses to check the price of the product instead of buying,
				elif next_option =="B":
					#item_price stores the price of the partcular item the user searches for
					#in the search query previously
					#getPrice will get the price of the item from the products instance variable
					item_price = self.__products[item_index].getPrice()
					sys.stdout.flush()
					#price will be displayed to the user
					sys.stdout.write("The price for "+self.__products[item_index].getName()+" is $"+str(item_price)+"\n")
					
				else:
					#when product not found
					sys.stdout.write("We were unable to find the product you were looking for, would you like to list the new item for sale if you have it? (Y if yes): ")
					sys.stdout.flush()
					#asks the user if the user wants to add a new item to the file instead
					#if the user has the item, although not found in the file previously
					add_new_if_have = sys.stdin.readline().strip()
					
					#if the user chooses to add a new product to the database
					if add_new_if_have =="Y":
						#add new items method will be executed
						self.__addNewItems()
	#if the user enters a character other than Y, the program will assume that the user does not wish
	#to take the offer of adding new item.
						
						#display the next message after all the process of searching and checking has been run through
				#display message to ask whether to add new item or search for item
				sys.stdout.write("What is your next choice? \n[A]Search for item \n[B]Add new item \nAny other key to stop. Enter choice: ")
				sys.stdout.flush()
				choice = sys.stdin.readline().strip()
			
			#choice B is when the user chooses to add new item to the file.	
			elif choice =="B":
				#add new items to the file method will be called and subsequently add new items to the file
				self.__addNewItems()
				#choice is prompted to ask whether the user chooses to continue searching, adding or
				#pressing any other key will stop the while loop, subsequently ending the program.
				sys.stdout.write("What is your next choice? \n[A]Search for item \n[B]Add new item \nAny other key to stop. Enter choice: ")
				sys.stdout.flush()
				choice = sys.stdin.readline().strip()

	#a method to add new items to the file			
	def __addNewItems(self):
		#prompt to ask user for name of product to be stored in the file
		sys.stdout.write("Enter the product name:")
		sys.stdout.flush()
		productname = sys.stdin.readline().strip()

		#name of file the user will store to
		sys.stdout.write("Enter the filename you want to save it to: ")
		sys.stdout.flush()
		filename = self.__validateFileName()

		#resume variable necessary to indicate if the price is valid or not, if it is valid then the add new product operation will continue, else just stop because it is invalid
		resume = True
		#try to input price and check if valid price or not
		try:
			sys.stdout.write("Enter price: ")
			sys.stdout.flush()
			price = float(sys.stdin.readline())
      #create a new product object if it is successful in obtaining a valid price
			new_product = Product(productname, price)
			#catch the error if invalid data type of price is inputted
		except:
			sys.stdout.write("Invalid price! Re-Enter record please")
			#resume will set to false because the subsequent operation cannot continue
			resume = False
     #if no errors in the price, the program will go ahead and continue adding the record to the file 
		if resume:
			try:
				#current products is a list of all the lines in the existing file
				#it stores STRINGS NOT OBJECTS unlike the previous operation of reading from file, the process is similar but different algorithm of reading from file hence this code is different and not duplicated
				#the way this is different from previous file read is that this does not create objects after reading from file, it just stores the entire line
				current_products = []
	      #the file to be read from at first to prevent existing data from being lost  
				file_to_read = open(filename, "r")
				#current file line is read from the file
				file_line_current = file_to_read.readline()
				#keep reading until file reaches the end
				while file_line_current!="":
					#place the current line into the
					current_products.append(file_line_current)
					#read next line
					file_line_current = file_to_read.readline()
	      #close file after everything settled    
				file_to_read.close()
			except:
				#if the existing file does not exist, the exception will handle
				sys.stdout.write("Existing file does not exist")
				
#try to write the new record the user had just inputted 
			try:	
				#open the file object for writing new line to the file
				file_open = open(filename, "w")
				#get the name and price of the NEW product object the user had created
				#and put it into one line for writing to the file specified
				line_to_write = new_product.getName()+","+str(new_product.getPrice())+"\n"
				#this counter is for the process of writing existing file contents to the file
				counter = 0
				#keep on writing the existing file contents stored in current_products list to the file
				while counter < len(current_products):
					#write the contents of that list to the file
					file_open.write(current_products[counter])
					#increment counter to write next list index
					counter+=1
	      #write the new line the user entered its name and price finally    
				file_open.write(line_to_write)
	      #close the file after all is done  
				file_open.close()
#prompt for saying if the file is written to successfully
				sys.stdout.write("Succesfully written to file! \n")
			except:
				#catch any error if the file is not able to be written to
				sys.stdout.write("Unable to write to file!")

#method to validate the file name the user inputs
	def __validateFileName(self):
		#takes the user input of the name of the file
		filename = sys.stdin.readline().strip()
		#keep asking for the filename if the filename does not end in .csv
		while filename[-4:] != ".csv":
			sys.stdout.write("File must end in .csv format! Re-Enter: ")
			sys.stdout.flush()
			#user re enters filename until valid
			filename = sys.stdin.readline().strip()
#finally return back the validated file name to the user
		return filename.strip()
      
#call the main class to start the program
my_product_manager = ProductManager()