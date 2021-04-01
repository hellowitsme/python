# リスト
# -------------------------------------
food = list()
fruit = []

list = ["Google", "Apple", "Facebook", "Amazon"]
list.append("Microsoft") # リストに追加

list.pop() # リストの末尾から要素を取り除く
"Alibaba" in list # リストに含まれているか
len(list)


# タプル
# -------------------------------------
# タプルは変更も追加もできない
list = tuple()
list = ()

person = ("M.Jackson", 1958)
("タプルの要素が1つの場合、カンマをつける",)

# 辞書
# -------------------------------------
list = dict()
list = {}

lists = {"Will Smith": "Bad Boys", "Tom Cruise": "TOP GUN", "Denzel Washington": "EQUALIZER", "Jason Statham": "Transporter", "Leonardo DiCaprio": "The Great Gatsby"}
del lists["Will Smith"] # 削除

for list in lists:
    print(lists[list])