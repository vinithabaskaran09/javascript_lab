"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # pass  # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    # pass  # TODO: replace this line with your code
    even_nums = [] 

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num) 
    
    return even_nums 


def get_odd_indices(items):
    # pass  # TODO: replace this line with your code
    odd_indices = []
    for index in range(len(items)):
        if index % 2 != 0:
            odd_indices.append(items[index])
    
    return odd_indices


def print_as_numbered_list(items):
    # pass  # TODO: replace this line with your code
    i = 1

    for item in items:
        print(f"{i}. {item}") 
        i += 1
    


def get_range(start, stop):
    # pass  # TODO: replace this line with your code
    nums = []
    for num in range(start,stop):
        nums.append(num)
        
    return nums
        


def censor_vowels(word):
    # pass  # TODO: replace this line with your code
    chars = ""

    for letter in word:
        if letter in "aeiou":
            chars += "*"
        else:
            chars += letter 
    
    # print(chars) 
    return chars 



def snake_to_camel(string):
    # pass  # TODO: replace this line with your code
    camel_case = []
    new_string = string.split("_")
    for char in new_string:
        camel_case.append(char.upper())
        
    return " ".join(camel_case)


def longest_word_length(words):
    # pass  # TODO: replace this line with your code
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word) 
    
    return longest 


def truncate(string):
    # pass  # TODO: replace this line with your code
    truncate_sting = [string[0]]
    
    
    for char in string:
        if char != truncate_sting[-1]:
            truncate_sting.append(char)

    return "".join(truncate_sting)


def has_balanced_parens(string):
    # pass  # TODO: replace this line with your code
    parens = 0 

    for char in string:
        if char == "(": 
            parens += 1
        elif char == ")":
            parens -= 1 
        
            if parens < 0:
                return False 
    
    return parens == 0 

# string = "aaabbbbbcccdd"
def compress(string):
#     # pass  # TODO: replace this line with your code
    compressed = []
    
    currchar = ""
    charcount = 0
    
    for letter in string:
        if letter != currchar: 
            # appent the currchar and number of count into compressed 
            compressed.append(currchar)
            
            if charcount > 1:
                compressed.append(str(charcount))
                
            currchar = letter
            charcount = 0
            
        charcount += 1
    
    compressed.append(currchar)
    if charcount > 1:
        compressed.append(str(charcount))
        
    return "".join(compressed)