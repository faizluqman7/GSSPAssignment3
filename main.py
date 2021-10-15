import sys
#importing random to generate a random confirmation number when the user buys a product
import random

class Product:
	def __init__(self, productName, productPrice):
		self.Name = productName
		self.Price = productPrice
		self.ID = random.randint(0,9999)

	def setName(self, name):
		self.Name = name

	def setPrice(self, price):
		self.Price = price

	def getName(self):
		return self.Name

	def getPrice(self):
		return self.Price

	def getID(self):
		return self.ID
		

class ProductManager:
	def __init__(self):
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
				#name of the file of the product user wants to search from, will be called through the function and the name of file will be validated there
				filename = sys.stdin.readline().strip()
				while filename[-4:] != ".csv":
					sys.stdout.write("File must end in .csv format! Re-Enter: ")
					sys.stdout.flush()
					filename = sys.stdin.readline().strip()

			
				#get the list of all the products in that catalog (reads from file) 
				#read_items function with the second parameter "title" returns a list of all the
				#titles (product names) of all the products in that particular file
				#products store a LIST of all of the products
				products = []
				try:
					file = open(filename, "r")
					file_contents = file.readline()
					while file_contents!="":
						file_contents_splitted = file_contents.split(",")
						product_object = Product(file_contents_splitted[0].strip(), file_contents_splitted[1].strip())
						products.append(product_object)
						file_contents = file.readline()
					
					file.close()
				except:
					sys.stdout.write("File does not exist!")

				
				#process of searching through one by one of all the products in the products list of items to match the user's search query
				#search counter necessary to check what index is currently now searching
				search_counter = 0
				#found variable is necessary to indicate if the product is found AT ALL inside the file
				#this is needed to display appropriate message later on.
				found = False
				#loop through the list of products sequentially to find the matching product with the user's search query
				while search_counter < len(products) and found == False:
					#if the product is found in the file, the index of the item is set to
					#the location of where the product was found
					if products[search_counter].getName() == search_query:
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
					sys.stdout.write("Successfully bought "+products[item_index].getName()+"! \nThank you for your purchase! Your confirmation number is "+str(confirmation_number)+"\nThank you for shopping with Shopada! \n")
					
					#if the user chooses to check the price of the product instead of buying,
				elif next_option =="B":
					#item_price stores the price of the partcular item the user searches for
					#in the search query previously
					item_price = products[item_index].getPrice()
					sys.stdout.flush()
					#price will be displayed to the user
					sys.stdout.write("The price for "+products[item_index].getName()+" is $"+str(item_price)+"\n")
					
				else:
					#when product not found
					sys.stdout.write("We were unable to find the product you were looking for, would you like to list the new item for sale if you have it? (Y if yes): ")
					sys.stdout.flush()
					#asks the user if the user wants to add a new item to the file instead
					#if the user has the item, although not found in the file previously
					add_new_if_have = sys.stdin.readline().strip()
					
					#if the user chooses to add a new product to the database
					if add_new_if_have =="Y":
						#add new items subroutine will run
						self.add_new_items()
	#if the user enters a character other than Y, the program will assume that the user does not wish
	#to take the offer of adding new item.
						
						#display the next message after all the process of searching and checking has been run through
				#display message to ask whether to add new item or search for item
				sys.stdout.write("What is your next choice? \n[A]Search for item \n[B]Add new item \nAny other key to stop. Enter choice: ")
				sys.stdout.flush()
				choice = sys.stdin.readline().strip()
			
			#choice B is when the user chooses to add new item to the file.	
			elif choice =="B":
				#add new items to the file subroutine will run and subsequently add new items to the file
				self.add_new_items()
				#next option is prompted to ask whether the user chooses to continue searching, adding or
				#pressing any other key will stop the while loop, subsequently ending the program.
				sys.stdout.write("What is your next choice? \n[A]Search for item \n[B]Add new item \nAny other key to stop. Enter choice: ")
				sys.stdout.flush()
				choice = sys.stdin.readline().strip()
				
	def add_new_items(self):
		sys.stdout.write("Enter the product name:")
		sys.stdout.flush()
		productname = sys.stdin.readline().strip()
    
		sys.stdout.write("Enter the filename you want to save it to: ")
		sys.stdout.flush()
		filename = sys.stdin.readline().strip()
    
		while filename[-4:]!=".csv":
			sys.stdout.write("Invalid file name, re enter: ")
			sys.stdout.flush()
			filename = sys.stdin.readline()
      
		resume = True
		try:
			sys.stdout.write("Enter price: ")
			sys.stdout.flush()
			price = float(sys.stdin.readline())
      
			new_product = Product(productname, price)
		except:
			sys.stdout.write("Invalid price! Re-Enter record please")
			resume = False
      
		if resume:
			try:
				current_products = []
	        
				file_to_read = open(filename, "r")
				file_line_current = file_to_read.readline()
				while file_line_current!="":
					current_products.append(file_line_current)
					file_line_current = file_to_read.readline()
	          
				file_to_read.close()
	        
				file_open = open(filename, "w")
				line_to_write = new_product.getName()+","+str(new_product.getPrice())+"\n"
				counter = 0
				while counter < len(current_products):
					file_open.write(current_products[counter])
					counter+=1
	          
				file_open.write(line_to_write)
	        
				file_open.close()

				sys.stdout.write("Succesfully written ti file! \n")
			except:
				sys.stdout.write("Unable to write o file!")
      

my_product_manager = ProductManager()
