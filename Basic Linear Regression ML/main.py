import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

model = LinearRegression(normalize=False)
data = pd.read_excel('C:\dev\Projects\Basic Linear Regression ML\data.xlsx')

# X = input, Y = predict
x = data.drop('billing', axis=1)
y = data.billing

#7 * 0.14 = ~1
xtrain, xval, ytrain, yval = train_test_split(x, y, test_size=0.14, random_state=0)

model.fit(xtrain, ytrain)
p = model.predict(xval)
p = format(p[0], '.2f')
print("expected billing :", p)

plot_seaborn = data
plot_seaborn.at[6, 'billing'] = p

sns.lmplot(x='drinks', y='deaths', hue='billing', data=plot_seaborn);
plt.title('Billing x Drinks x Deaths')
plt.show()