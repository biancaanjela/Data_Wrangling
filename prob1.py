import pandas as bi

one = {'Student': ['Ice Bear','Panda','Grizzly'],
         'Math': [80,95,79]}

a = bi.DataFrame (one, columns = ['Student','Math'])

two = {'Student': ['Ice Bear','Panda','Grizzly'],
         'Electronics': [85,81,83]}

b = bi.DataFrame (two, columns = ['Student','Electronics'])

three = {'Student': ['Ice Bear','Panda','Grizzly'],
         'GEAS': [90,79,93]}

c = bi.DataFrame (three, columns = ['Student','GEAS'])

four = {'Student': ['Ice Bear','Panda','Grizzly'],
         'ESAT': [93,89,88]}

d = bi.DataFrame (four, columns = ['Student','ESAT'])


x = bi.merge(a,b,
         how='outer', on='Student')

y = bi.merge(c,d,
         how='outer', on='Student')

z = bi.merge(x,y,
         how='outer', on='Student')

cai = bi.melt(z, id_vars=['Student'], value_vars=['Math','Electronics','GEAS','ESAT']).rename(columns={'variable' : 'Subject', 'value' : 'Grades'})