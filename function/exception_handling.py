chara = "abcdefghij"
print(chara.index("h"))

def result():
    try:
        print(chara.index("o"))
    except:
        print("Not Found")

result()
