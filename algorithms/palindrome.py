def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Apple")) 
print(palindrome("level"))