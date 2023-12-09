import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/Acoustic Features.csv")
df['Class'] = pd.Categorical(df['Class']).codes
df['_HarmonicChangeDetectionFunction_PeriodEntropy'] = pd.to_numeric(df['_HarmonicChangeDetectionFunction_PeriodEntropy'], errors='coerce')
df = df.dropna(subset=['_HarmonicChangeDetectionFunction_PeriodEntropy'])

plt.figure(figsize=(10, 6))
sns.regplot(x='Class', y='_HarmonicChangeDetectionFunction_PeriodEntropy', data=df, scatter_kws={'s': 20, 'alpha': 0.5})
plt.title('Regression Plot of Harmonic Change Detection Function Period Entropy')
plt.xlabel('Class')
plt.ylabel('Period Entropy')
plt.savefig('results/plot.png')
