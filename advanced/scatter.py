import pandas
from matplot import pyplot

score = pandas.read_csv('score2.csv', encoding='utf-8')
score.plot.scatter('English', 'Japanese', s=100, c='white', edgecolor='blue', figsize=(6, 6))

pyplot.savefig('scatter1.png')
pyplot.show()