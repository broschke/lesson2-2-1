import scipy.stats as stats
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.boxplot(x)
#plt.show()
plt.savefig("boxplot.png")

plt.hist(x, histtype='bar')
#plt.show()
plt.savefig("hist.png")

graph1 = stats.probplot(x, dist="norm", plot=plt)
#plt.show()
plt.savefig("qq.png")

