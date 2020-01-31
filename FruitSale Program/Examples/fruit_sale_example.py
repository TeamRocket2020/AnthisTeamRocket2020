import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
turnover_k_euros = [12, 34, 31, 20]

plt.bar(x, turnover_k_euros, width=0.4)
plt.xticks(np.arange(4), ('apple', 'banana', 'cherry', 'durian'))
plt.xlabel('Product')
plt.ylabel('Turnover (K euros)')

plt.show()
