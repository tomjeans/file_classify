import numpy as np
import matplotlib.pyplot as plt
import os
labels = 'ac','fl','hc','cerebellum'
with open('log_count.txt') as f:
    line=f.readlines()
    print(float(line[18][17:])+1)
    # for lines in f.readlines():
    #  print (type(lines))
ac=float(line[15][8:])
fl=float(line[16][8:])
hc=float(line[17][8:])
cerebellum=float(line[18][17:])
fracs = [ac, fl, hc, cerebellum]
explode = [0, 0, 0, 0.1]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6
        )
plt.show()