import matplotlib.pylab as plt
from pylab import csv2rec, legend
trends = csv2rec('trends.csv')
plt.plot(
	trends.week_start, trends.kayak,
	trends.week_start, trends.textbooks,
	trends.week_start, trends.skiing,
	trends.week_start, trends.global_warming,
	trends.week_start, trends.spring_break)
legend(('kayak','textbooks','skiing','global warming', 'spring break'))
plt.show()

years = np.array([x.year for x in trends.week_start])
start_2004 = np.min(np.where(years==2004))
start_2005 = np.min(np.where(years==2005))
start_2006 = np.min(np.where(years==2006))

max_kayak_2004 = trends[np.argmax(trends.kayak[0:start_2005])][0:start_2005]
