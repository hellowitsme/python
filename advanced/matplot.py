from matplotlib import pyplot
import pandas

score = pandas.read_csv('score2.csv', encoding='utf-8')

# pandasを使ってヒストグラムを作成する方法
score.hist()
pyplot.savefig('hist2.png')
pyplot.show()

# motplotlibを使う方法
pyplot.figure('Math') # 図を作成
pyplot.xlabel('Score') # x軸の名前
pyplot.ylabel('Count') # y軸の名前
pyplot.hist(score['Math']) # ヒストグラム
pyplot.savefig('hist1.png') # ファイルに保存
pyplot.show()