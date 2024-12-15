## Algorithmic Thinking and Data Structures

def capitalize_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the words back into a single string
    result_string = ' '.join(capitalized_words)
    
    return result_string

# Testing
print(capitalize_words("hi")) 
print(capitalize_words("i love programming"))  
