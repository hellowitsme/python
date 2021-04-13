# Pandasの主要な機能は、データフレームオブジェクト
# 数値以外のデータも扱えることや、列名を指定できるなどが特徴
import pandas as pd

score = pd.read_csv('client.csv', encoding='utf-8')
# print(score)

# 指定した列だけ
print(score['First'])

# 複数列の指定
print(score[['First', 'Second']])

# スライスで指定した行を取得
print(score[: 6])
print(score[40:])

# 行と列の指定
print(score[['First']][20:31])

# 条件に合う要素を取得
print(score[score['First'] >= 80])
queryメソッドを使う方法
print(score.query('First == 90'))


# データに新しい列を追加
score['Total'] = score['First'] + score['Second'] + score['Third']
score['Total'] = score.sum(1)
print(score)

# csvファイルに保存
score.to_csv('result.csv', index=False)
score.to_csv('result.csv')