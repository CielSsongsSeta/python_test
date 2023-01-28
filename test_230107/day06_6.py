import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font = font_manager.FontProperties(fname='gulim.ttc').get_name()

lst = [10,20,12,31,41,90,66,11,44,88]
plt.title('분포도')
plt.xlabel('점수')
plt.ylabel('갯수')
plt.hist(lst)
plt.show()
