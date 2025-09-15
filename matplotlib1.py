
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = np.linspace(0,10,100)
# y = np.sin(x)
# plt.plot(x,y,color = "red",linestyle ='--',marker = 'o')
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x, y, color="red", marker="x")
# plt.title("Scatter Plot")
# plt.show()

# categories = ['A','B','C']
# values = [3,7,5]
# plt.bar(categories, values, color = ['red','green','blue'])
# plt.title("Bar Plot")
# plt.show()

# categories = ['A','B','C']
# values = [3,7,5]
# plt.barh(categories, values, color = ['red','green','blue'])
# plt.title("Bar Plot")
# plt.show()

# data = np.random.randn(1000)
# plt.hist(data, bins =30, color = 'skyblue', edgecolor = 'black')
# plt.title("Histogram")
# plt.show()

# sizes  = [20,30,25,25]
# labels = ['A','B','C','D']
# plt.pie(sizes,labels=labels, autopct = '%1.1f%%', startangle = 90)
# plt.title("Pie Chart")
# plt.show()

# days = [1,2,3,4,5]
# sleeping = [7,8,6,11,7]
# eating = [2,3,4,3,2]
# working = [7,8,7,2,2]
# playing = [8,5,7,8,13]
# plt.stackplot(days,sleeping,eating,working,playing,labels = ['Sleep','Eat','Work','Play'])
# plt.legend(loc = 'upper left')
# plt.title("Stacked Area Plot")
# plt.show()

# data= np.random.normal(100,20,200)
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()

# df = sns.load_dataset("tips")
# sns.histplot(df["total_bill"],bins= 20, kde= True, color= "skyblue")
# plt.title("Histogram + KDE")
# plt.show()

# data = pd.DataFrame({
#     "category":['A','B','C','D'],
#     "value" : [4,7,2,9]
# })
# sns.barplot(x ="category" , y = "value" , data= data)
# plt.title("Normal Bar Chart (Seaborn)")
# plt.show()

# df = sns.load_dataset("tips")
# sns.countplot(x = "day", data=df, palette = "Set2")
# plt.title("Count Plot")
# plt.show()



# df = sns.load_dataset("tips")
# sns.boxplot(x = "day", y="total_bill", data= df, palette = "pastel")
# plt.title("Box Plot")
# plt.show()

df = sns.load_dataset("tips")
sns.scatterplot(x = "total_bill", y="tip" , data = df, hue="sex" , style="time")
plt.title("Scatter Plot")
plt.show()




import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

columns = ['buying','maint','doors','persons','lug_boot','safety','class']
df = pd.read_csv("car.data",names=columns)

print(df)
