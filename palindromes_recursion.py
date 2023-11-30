"""Find palindromes (letter palingrams) using recursion in a dictionary file."""
import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')
pali_list = []


for word in word_list:
    if len(word) == 1:
        pali_list.append(word)
    else:
        rev_word = word[::-1]
        half = len(word)//2
        for i in range(half):
            if not word[i] == rev_word[i]:
                break
            elif word[i] == rev_word[i] and i == half -1:
                pali_list.append(word)
            else:
                continue


print(f"\nNumber of palindromes found = {len(pali_list)}")
print(*pali_list, sep='\n')

