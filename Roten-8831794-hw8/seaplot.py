# for inline plots in jupyter
# %matplotlib inline
# import matplotlib
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
# import seaborn
import seaborn as sns

# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})

# import uniform distribution
from scipy.stats import expon
data_expon = expon.rvs(scale=1,loc=0,size=10000)

ax = sns.distplot(data_expon,
                  kde=True,
                  bins=100,
                  color='red',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')

#plt.show()
