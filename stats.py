#counts the number of words in a file
def word_counter (book):
	return len(book.split())


#creates a dictionary the counts how many of each character are in the book.
def character_counter(book):
    dicionario = {}
    for character in book:
        character = character.lower ()
        if character in dicionario:
            dicionario [character] += 1  
        else:
            dicionario [character] = 1
    return dicionario

def sort_on(sorted):
    return sorted["num"]


def results_sorter (results):
    dictionarie = {}
    sorted_list = []
    for entry in results:
        dictionarie ["entry_name"] = entry
        dictionarie ["num"] = results.get(entry)
        sorted_list.append (dictionarie)
        dictionarie = {}

    
    return sorted_list
