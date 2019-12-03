import pandas as bi

x = {'Box': ['Box1','Box1','Box1','Box2','Box2','Box2'],
     'Dimension': ['Length','Width','Height','Length','Width','Height'],
     'Value': [6,4,2,5,3,4]}

a = bi.DataFrame (x, columns = ['Box','Dimension','Value'])

n = a.pivot_table(index=['Box'], columns = 'Dimension', values = 'Value')

n['Volume'] = n.Length*n.Height*n.Width