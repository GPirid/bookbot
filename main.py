#imports the word_counter function for the stats file
from stats import word_counter
from stats import character_counter
from stats import results_sorter
from stats import sort_on
import sys

#reads txt. file and turns it into a string, which is later stored in the "book" variable
def get_book_text(relative_path):
	with open (relative_path) as f:
		return f.read()



#defines main function
'''	
gets the directory from which it must read. Then stores text as as string in the variable "book".
Then, the word_counter function is called and stores the number of words in the variable "words".
Finally, the whole text contained in the "book" variable and the number of words stored in the "words"
variable are printed on screen.
'''
def main ():
	try:	
			if len(sys.argv) != 2:
				print ("'Usage: python3 main.py <path_to_book>'")
				sys.exit (1)
			
			else:
				print ("============ BOOKBOT ============")
				print ("This program counts the number of words and the instances of each character in a .txt document.")
				print ("Usage: python3 main.py <path_to_book>")
				directory = sys.argv[1]
				book = get_book_text(directory)
				words = word_counter(book)		
				print (f"Analyzing book found at {directory}...")
				print ("=================================")
				print (book)
				print ("----------- Word Count ----------")
				print(f"Found {words} total words in the document")
				print("--------- Character Count -------")
				results = character_counter(book)
				results = results_sorter (results)
				results.sort(reverse=True,key=sort_on)
				for result in results:
					if result ["entry_name"].isalpha():
						print(f"{result["entry_name"]}: {result["num"]}")
				print ("============= END ===============")
				
			
	except EOFError:
		return 0
	
	
#executes main function
main()