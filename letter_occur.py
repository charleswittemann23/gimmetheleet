from collections import defaultdict
"""
Given input 
["abc", "bcd", "cde"]


return dict that shows, for each letter in lst, the letters that show up the most with that letter

ex:
{
a: [b,c], ## because a only shows up in first word, we return the other characters in the word

b: [c]

c: [b,d]
d: [c],
e: [c, d]

}
"""
example_input = ["abc", "bcd", "cde"]
def find_featured_chars(lst: list[str]) ->dict:
    occur_dih = defaultdict(dict)
    ##setup dict:
    for word in lst:
        unique_letters = set(word) ## find all of the unique letters in each word. Not important how many times the letter occurs. Unique letters max will be 26 letters. 
        #double for loop with this constraint means k^2 * n words
        for letter in unique_letters:
            for otherletter in unique_letters:
                if otherletter != letter:
                    if otherletter in occur_dih[letter]:
                        occur_dih[letter][otherletter]+=1
                    else:
                        occur_dih[letter][otherletter] =1
    ## occur dih will have a dictionary of dictionaries where the first key will be a letter, and the dictionary within will contain the frequencies of each character seen without the original key

    result = {}
    for letter,counts in occur_dih.items():
        print(f"Letter: {letter} with counts {counts}")
        max_count = max(counts.values())
        result[letter] = [other for other,count in counts.items() if count == max_count]
    return result


print(find_featured_chars(example_input))

