#data visualization imports / импорт библиотек для визуализации
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

print("----------------------------------------------------------------1----")
"""
temperature plot / график температур
description: you have weekly temperature data. plot temperature changes by day.
описание: у вас есть данные о температуре в течение недели. постройте график изменения температуры по дням недели.
"""
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 24, 20, 19, 21, 23, 25]
plt.plot(days, temperatures, marker='o', color='b')
plt.title('Temperature Over the Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.show()

print("---------------------------------------------------------------2-----")
"""
bar chart for grades / столбчатая диаграмма для оценок
description: you have student grades for 5 subjects. create a bar chart.
описание: у вас есть оценки студентов по 5 предметам. постройте столбчатую диаграмму.
"""
subjects = ['Math', 'Science', 'History', 'English', 'Art']
scores = [85, 92, 78, 88, 95]

plt.bar(subjects, scores, color='green')
plt.title('Student Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.show()

print("---------------------------------------------------------------3-----")
"""
scatter plot for height-weight / диаграмма рассеяния для роста и веса
description: you have height and weight data. create a scatter plot.
описание: у вас есть данные о росте и весе. постройте диаграмму рассеяния.
"""
heights = [150, 160, 170, 180, 190]
weights = [45, 55, 65, 75, 85]

plt.scatter(heights, weights, color='red')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

print("---------------------------------------------------------------4-----")
"""
data distribution visualization / визуализация распределения данных
description: plot histogram with kde for random data.
описание: постройте гистограмму с kde для случайных данных.
"""
data = np.random.normal(loc=50, scale=15, size=1000)
sns.histplot(data, kde=True, color='blue', bins=30)
plt.title('Histogram and KDE')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

print("--------------------------------------------------------------5-----")
"""
sales heatmap / тепловая карта продаж
description: create correlation heatmap for sales data.
описание: постройте тепловую карту корреляций для данных о продажах.
"""
data = {
    'Region 1': [100, 200, 150, 130],
    'Region 2': [80, 120, 140, 160],
    'Region 3': [90, 110, 115, 105],
    'Category A': [50, 60, 45, 55],
    'Category B': [75, 80, 70, 85]
}
df = pd.DataFrame(data, index=['Q1', 'Q2', 'Q3', 'Q4'])
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

print("------------------------------------------------------------6-----")
"""
multi-line plot / линейный график с несколькими линиями
description: plot sales data for multiple products over time.
описание: постройте график продаж нескольких продуктов за период.
"""
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_a_sales = [200, 220, 250, 270, 290, 310]
product_b_sales = [180, 190, 210, 240, 260, 280]
product_c_sales = [150, 170, 190, 210, 230, 250]

plt.plot(months, product_a_sales, label='Product A', marker='o', color='blue')
plt.plot(months, product_b_sales, label='Product B', marker='x', color='red')
plt.plot(months, product_c_sales, label='Product C', marker='s', color='green')

plt.title('Product Sales')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

print("-------------------------------------------------------------7-----")
"""
colored scatter plot / диаграмма рассеяния с цветами
description: plot salary vs experience colored by position.
описание: постройте график зарплат от опыта с цветами по должностям.
"""
experience = [1, 2, 3, 5, 6, 7, 2, 4, 8, 3]
salary = [40000, 45000, 50000, 65000, 70000, 75000, 48000, 52000, 80000, 54000]
positions = ['Junior', 'Junior', 'Mid', 'Senior', 'Senior', 'Senior', 'Junior', 'Mid', 'Senior', 'Mid']

colors = {'Junior': 'blue', 'Mid': 'orange', 'Senior': 'green'}
scatter_colors = [colors[pos] for pos in positions]

plt.scatter(experience, salary, c=scatter_colors, s=100)
plt.title('Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print("---------------------------------------------------------------8-----")
"""
pie chart / круговая диаграмма
description: visualize company budget distribution.
описание: визуализируйте распределение бюджета компании.
"""
expenses = {'Marketing': 5000, 'R&D': 7000, 'Operations': 4000, 'Sales': 3000, 'HR': 2000}
df = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])

plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140)
plt.title('Budget Distribution')
plt.show()