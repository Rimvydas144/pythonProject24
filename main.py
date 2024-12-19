import seaborn as sns
import  numpy as np
import matplotlib.pyplot as plt
a = np.arange(1,11)
b = np.random.randint(-5,25,10)
sns.scatterplot(x=a,y=b)
plt.show()
