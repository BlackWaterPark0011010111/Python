import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

print("----------------------------------------------------------------1----")
"""
Построение графика температур
Описание: У вас есть данные о температуре в течение недели. Постройте график изменения температуры по дням недели.
"""
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 24, 20, 19, 21, 23, 25]
plt.plot(days, temperatures, marker='o', color='b')
plt.title('Temperature Over the Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.show()





print("---------------------------------------------------------------2-----")

"""Столбчатая диаграмма для оценок
Описание: У вас есть оценки студентов по 5 предметам. Постройте столбчатую диаграмму для этих данных.
"""
subjects = ['Math', 'Science', 'History', 'English', 'Art']
scores = [85, 92, 78, 88, 95]

plt.bar(subjects, scores, color='green')
plt.title('Student Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.show()

print("---------------------------------------------------------------3-----")

"""Диаграмма рассеяния для роста и веса
Описание: У вас есть данные о росте и весе группы людей. Постройте диаграмму рассеяния для этих данных.
"""

heights = [150, 160, 170, 180, 190]
weights = [45, 55, 65, 75, 85]

# Plotting scatter plot
plt.scatter(heights, weights, color='red')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
print("---------------------------------------------------------------4-----")

"""
Визуализация распределения данных (Гистограмма и Ядерная оценка плотности)
Описание: У вас есть набор случайных данных. Постройте гистограмму, а также добавьте к ней график ядерной оценки плотности, чтобы увидеть, как данные распределяются.
"""


# Generating random data
data = np.random.normal(loc=50, scale=15, size=1000)

# Построение гистограммы с KDE  Plotting histogram with KDE

sns.histplot(data, kde=True, color='blue', bins=30)

# Настройки графика GRAPHIC SETTINGS
plt.title('Histogram and KDE of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
print("--------------------------------------------------------------5-----")


"""
У вас есть данные о продажах по различным регионам и категориям товаров. Постройте тепловую карту для анализа корреляций между различными переменными.
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


plt.title('Heatmap of Correlations')
plt.show()

print("------------------------------------------------------------6-----")

""" Линейный график с несколькими линиями для разных групп
Описание: У вас есть данные о продажах по различным продуктам в разные месяцы. Постройте линейный график, где будут отображены данные для нескольких продуктов одновременно.

"""

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_a_sales = [200, 220, 250, 270, 290, 310]
product_b_sales = [180, 190, 210, 240, 260, 280]
product_c_sales = [150, 170, 190, 210, 230, 250]

# Построение линейного графика
plt.plot(months, product_a_sales, label='Product A', marker='o', color='blue')
plt.plot(months, product_b_sales, label='Product B', marker='x', color='red')
plt.plot(months, product_c_sales, label='Product C', marker='s', color='green')

# Настройки графика
plt.title('Sales of Products Over 6 Months')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

print("-------------------------------------------------------------7-----")

""" Диаграмма рассеяния с цветами в зависимости от категории
Описание: У вас есть данные о зарплатах и опыте сотрудников, а также информация о их должностях. Постройте диаграмму рассеяния, где цвет точек будет зависеть от должности.

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

""" Визуализация с использованием Pandas и matplotlib (Круговая диаграмма)
Описание: У вас есть данные о распределении расходов в бюджете компании. Постройте круговую диаграмму для визуализации долей расходов по категориям.
"""

# Данные о расходах 
expenses = {'Marketing': 5000, 'R&D': 7000, 'Operations': 4000, 'Sales': 3000, 'HR': 2000}

# Преобразование данных в DataFrame Converting data to DataFrame
df = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])

# Построение круговой диаграммы  Plotting a pie chart
plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140)

# Настройки графика Plot settings
plt.title('Company Budget Expenses Distribution')
plt.show()