import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/Acoustic Features 2.csv")

plt.figure(figsize=(10, 6))
sns.regplot(x='Class', y='_HarmonicChangeDetectionFunction_PeriodEntropy', data=df, scatter_kws={'s': 20, 'alpha': 0.5})
plt.title('Regression Plot of Harmonic Change Detection Function Period Entropy')
plt.xlabel('Class')
plt.ylabel('Period Entropy')
plt.show()
