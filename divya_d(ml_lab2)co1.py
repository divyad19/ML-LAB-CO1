# -*- coding: utf-8 -*-
"""divya.d(ml lab2)co1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pOaii582zr2iJcrXCxj_Rdw3iiGtxQ2E
"""



"""#### Activity 1: Create Customized Line plots.

Given the dataset of the average annual salary (in dollars) of developers of various programming languages. Create customized line plots to compare the salary variations **Age-wise** for **Python** developer with **Javascript** developer.

**Link to the Dataset**: https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/10-Subplots/data.csv
"""

# Step 1: Import necessary modules to create dataframe and line plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Create a Dataframe and store it in a variable from the given dataset
sal_df=pd.read_csv(" https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/10-Subplots/data.csv")
# Print the first 5 rows in the DataFrame
sal_df.head()

# Step 3: Create a customised line plot for comparing the Age-wise annual salary variations for Python developer with JavaScript developer.  Use the 'seaborn-dark' style
plt.figure(figsize=(15,5))
plt.title("LINE GRAPH OF SALARY")

plt.plot(sal_df['Python'],"r--o",label="Python	")
plt.plot(sal_df['JavaScript'],"y--o",label="JavaScript")
plt.legend()
plt.xlabel("age")
plt.ylabel("salary")
plt.grid()
plt.show()



"""**Q**: What can you conclude from the above comparison ?

**A**:salary of python developers are higher than Javascript
"""



"""#### Activity 2.1: Create a Pandas DataFrame

Create a Pandas DataFrame by using the below link which has the dataset of Tips taken on the total bill amount in restaurants in the CSV format:

**Dataset Link** : https://raw.githubusercontent.com/jiss-github123/tips/main/tips.csv

Also, print the first five rows of the dataset.
"""

# Create a pandas DataFrame
import pandas as pd

r_f=pd.read_csv("https://raw.githubusercontent.com/jiss-github123/tips/main/tips.csv")
r_f.head()

"""#### Activity 2.2: Create a Gender wise Count plot

Create a gender wise count plot by using the values in the `sex` column.
"""

# Gender wise count plot for the 'sex' values in the 'tip_df' DataFrame on the x-axis.
import seaborn as sb
plt.figure(figsize=(5,3))
plt.title("gender count")
sb.countplot(x='sex',data=r_df,hue='sex')
plt.grid()
plt.show()

"""So according to the above count plot, the number of `Female` is less than the number of `Male` in the dataset.

**Q** : Which gender is recorded more in the dataset ?

**A** :MALE

#### Activity 3: Histogram using `hist()` Function

Given a list of random age of 100 individuals in a range between 1 and 91. Write a code to visualise the values in the list using a histogram.

```
age_list = [1,1,2,3,3,5,7,8,9,10,
     10,11,11,13,13,15,16,17,18,18,
     18,19,20,21,21,23,24,24,25,25,
     25,25,26,26,26,27,27,27,27,27,
     29,30,30,31,33,34,34,34,35,36,
     36,37,37,38,38,39,40,41,41,42,
     43,44,45,45,46,47,48,48,49,50,
     51,52,53,54,55,55,56,57,58,60,
     61,63,64,65,66,68,70,71,72,74,
     75,77,81,83,84,87,89,90,90,91
     ]
```

**Steps to Follow**:

1. Import the `matplotlib.pyplot` module.

2. Set the size of the plot using the `figsize` attribute of the `figure()` function.

3. Pass the `age_list` list inside the `hist()` function and set `bins = 5`.

4. Display the histogram using the `show()` function of the `matplotlib.pyplot` module.
"""

age_list = [1,1,2,3,3,5,7,8,9,10,
     10,11,11,13,13,15,16,17,18,18,
     18,19,20,21,21,23,24,24,25,25,
     25,25,26,26,26,27,27,27,27,27,
     29,30,30,31,33,34,34,34,35,36,
     36,37,37,38,38,39,40,41,41,42,
     43,44,45,45,46,47,48,48,49,50,
     51,52,53,54,55,55,56,57,58,60,
     61,63,64,65,66,68,70,71,72,74,
     75,77,81,83,84,87,89,90,90,91
     ]
# Import the 'matplotlib.pyplot' module.
import matplotlib.pyplot as plt
# Set the size of the plot using the 'figsize' attribute of the 'figure()' function.
plt.figure(figsize=(7,3))
# Pass the 'age_list' list inside the 'hist()' function and set 'bins = 5'.
plt.hist(age_list ,bins=10)
# Display the histogram using the 'show()' function of the 'matplotlib.pyplot' module.
plt.show()

"""#### Activity 4: Lineplot using `plot()` Function"""

"""
Draw a line in a diagram from position (1, 3) to (2, 10) then to (6, 12) and finally to position
(18, 20). (Mark each point with a beautiful green colour and set line colour to red and line style
dotted)
 """
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,6,18])
ypoints=np.array([3,10,12,20])
plt.plot(xpoints,ypoints,marker='o',color="red",mfc='g',mec='r',linestyle='dotted')
plt.show()

"""
Draw a plot for the following data:

Temperature in degree Celsius ,  Sales

        12                       100
        14                       200
        16                       250
        18                       400
        20                       300
        22                       450
        24                       500

"""
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([12,14,16,18,20,22,24])
ypoints=np.array([100,200,250,400,300,450,500])
plt.plot(xpoints,ypoints,marker='o',color="green",mfc='k',mec='k',linestyle='dotted')
plt.show()

"""#### Activity 5: Bar graph using `bar()` Function"""

"""
Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           7.7  6.7

(i) Write a Python programming to display a bar chart
    of the popularity of programming Languages.
"""

data={'java':22.2,'python':17.2,'php':8.8,'javascript':8,'c#':7.7,'c++':6.7}
plt.bar(data.keys(),data.values(),color="cyan",edgecolor="k")
plt.show()

"""#### Activity 6: Piechart using `pie()` Function"""

"""
Write a Python programming to create a pie chart
   of the popularity of programming Languages.

Programming languages: Java Python PHP JavaScript C# C++
Popularity           : 22.2 17.6   8.8 8          7.7 6.7

"""
data={'java':22.2,'python':17.2,'php':8.8,'javascript':8,'c#':7.7,'c++':6.7}
plt.pie(data.values(),labels=data.keys(),shadow=True)
plt.show()