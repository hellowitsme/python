# アナグラムは、単語を並べ替えて別の単語を作る

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(sorted("iceman"))
print(sorted("ciname"))