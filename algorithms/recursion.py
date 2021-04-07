# 再帰法は、関数からその関数自身を呼び出す
# 1).再帰終了条件を持たなければならない
# 2).状態を変えながら、再帰終了条件に進んでいかなくてはならない
# 3).再帰的に関数自信を呼び出さなくてはならない

def bottles_of_beer(bob):

    # 1)
    if bob < 1:
        print("No more bottles of beer on the wall. No more bottles of beer.")
        return
    tmp = bob

    # 2)
    bob -= 1
    print("""{} bottles of beer on the wall. {} bottles of beer. Take one down, pass it around, {}
          bottles of beer on the wall.""".format(tmp, tmp, bob))

    # 3)
    bottles_of_beer(bob)

bottles_of_beer(100)