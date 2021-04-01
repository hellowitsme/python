# フォーマット
# -------------------------------------
# titleメソッド
# 頭文字を大文字に
print("the walking dead".title())

# formatメソッド
who = input("誰が:")
where = input("どこで:")
what = input("何を:")
do = input("した:")

print("{}が、{}で、{}を、{}したw".format(who, where, what, do))

# splitメソッド
# 引数に渡した文字で分割
print("splitメソッドでは、文章を分割できます。".split("、"))

# joinメソッド
# 全ての文字列の間に新しい文字列を追加
words = ["The", "Walking", "Dead"]
print(" ".join(words))

# stripメソッド
# 空白除去
print("    The    ".strip())

# indexメソッド
# 引数に文字を渡す。最初にその文字が現れたインデックス値が帰ってくる
print("animals".index("l"))

# sliceメソッド
# オブジェクトの一部を切り取る
# 終了インデックス値の手前までしか含まない
# 最初の要素から始める場合"0"は省略可能
# 最後の要素まで含める場合終了インデックスは省略可能
list = ["Google", "Apple", "Facebook", "Amazon"]
print(list[:3])
print(list[1:])
