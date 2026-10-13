# 🦠 COVID-19 Data Analysis Using Python

## 📌 Introduction

The COVID-19 Data Analysis project is a Python-based data analysis project developed to analyze and visualize COVID-19 data across different countries and over time.

The project uses Python libraries such as NumPy, Pandas, Matplotlib, and Seaborn to perform statistical calculations, process datasets, and create meaningful visualizations.

It helps users understand the trends in cumulative cases, recoveries, deaths, and new daily cases. It also explores the relationship between government intervention scores and new COVID-19 cases.

This project uses a menu-driven system that allows users to select different analysis options and view results according to their requirements.

## 🎯 Objectives

The main objectives of this project are:

- To analyze COVID-19 data using Python.
- To load and process CSV datasets using Pandas.
- To perform numerical calculations using NumPy.
- To calculate statistical values such as mean, median, maximum, and minimum.
- To analyze cumulative COVID-19 cases, recoveries, and deaths.
- To visualize global COVID-19 trends over time.
- To compare COVID-19 cases across different countries.
- To analyze the relationship between government intervention scores and new cases.
- To display country-wise cumulative case trends.
- To develop programming skills using classes, objects, methods, loops, and conditional statements.
- To understand practical applications of data analysis and visualization.

## 🛠️ Technologies Used

### 1. Python
Python is the main programming language used to develop the project. It provides a simple way to perform data processing, calculations, and visualization.

### 2. NumPy
NumPy is used for numerical operations and statistical calculations.

**Functions used:**
- `np.mean()` – Calculates the average value.
- `np.median()` – Calculates the middle value.
- `np.max()` – Finds the maximum value.
- `np.min()` – Finds the minimum value.
- `to_numpy()` – Converts a Pandas column into a NumPy array.

### 3. Pandas
Pandas is used to load, organize, filter, and analyze the COVID-19 dataset.

**Functions used:**
- `pd.read_csv()` – Reads the CSV dataset.
- `pd.to_datetime()` – Converts dates into datetime format.
- `groupby()` – Groups records by country or date.
- `nlargest()` – Selects the largest values.
- `isin()` – Filters records that match selected values.
- `DataFrame.empty` – Checks whether the DataFrame is empty.

### 4. Matplotlib
Matplotlib is used to create charts and visualize data.

**Functions used:**
- `plt.title()` – Adds a chart title.
- `plt.xlabel()` – Adds a label to the X-axis.
- `plt.ylabel()` – Adds a label to the Y-axis.
- `plt.grid()` – Displays grid lines.
- `plt.tight_layout()` – Adjusts the chart layout.
- `plt.show()` – Displays the chart.

### 5. Seaborn
Seaborn is used to create statistical visualizations.

**Functions used:**
- `sns.scatterplot()` – Creates a scatter plot.
- `sns.lineplot()` – Creates a line chart.

## ✨ Features

### 1. Statistical Summary
This feature displays basic information about the dataset and calculates statistical values for daily new COVID-19 cases.

It includes:
- Dataset information
- Mean daily cases
- Median daily cases
- Maximum daily cases
- Minimum daily cases

These values help summarize the distribution of new cases in the dataset.

### 2. Global COVID-19 Trends
This feature displays global trends in cumulative cases, recoveries, and deaths over time.

The data is grouped by date, and the cumulative values are added across the available country records.

The line chart helps users compare how these three measures change over the recorded period.

### 3. Country Comparison
This feature identifies the top five countries according to their maximum recorded cumulative case values.

A bar chart is created to compare the selected countries.

It helps users quickly identify which countries have the largest recorded cumulative case totals in the dataset.

### 4. Government Intervention Analysis
This feature creates a scatter plot to examine the relationship between government intervention scores and new COVID-19 cases.

The chart uses:
- X-axis: Government Intervention Score
- Y-axis: New Cases
- Color: Region

The visualization helps users explore patterns between intervention scores and reported new cases. However, it does not establish that government interventions caused a particular change in cases.

### 5. Country-wise Trends
This feature identifies the top five countries by cumulative cases and displays their cumulative case trends over time.

A line chart is used to show the recorded changes for each selected country.

Different colors represent different countries, making comparisons easier.

## 📂 Project Structure

```text
COVID-19-Data-Analysis/
│
├── covid_analysis.py
│
├── COVID19_Data_Analysis_Dataset.csv
│
└── README.md
```

### File Description

- **covid_analysis.py:** Contains the Python class, analysis methods, visualization functions, and menu-driven program.
- **COVID19_Data_Analysis_Dataset.csv:** Contains the COVID-19 dataset used for analysis.
- **README.md:** Provides project information, installation instructions, features, and usage details.

*Note: Replace `covid_analysis.py` with your actual Python filename if it is different.*

## 📊 Dataset Information

The project uses a CSV file named:

`COVID19_Data_Analysis_Dataset.csv`

The dataset should contain the following columns:

| Column Name | Description |
|---|---|
| Date | Date of the recorded observation |
| Country | Name of the country |
| New_Cases | Number of newly reported cases |
| Cumulative_Cases | Total reported cases up to the observation |
| Cumulative_Recovered | Total recorded recoveries |
| Cumulative_Deaths | Total recorded deaths |
| Government_Intervention_Score | Recorded intervention score |
| Region | Geographical region |

The exact column names must match those used in the Python program.

The dataset should contain valid records for the selected analyses. Missing or invalid values may require additional data cleaning.

## ⚙️ Installation and Setup

Follow these steps to run the project on your computer.

### Step 1: Install Python

Install Python if it is not already installed on your computer.

Verify the installation by running:

```bash
python --version
```

### Step 2: Install Required Libraries

Open the terminal in VS Code and run:

```bash
pip install numpy pandas matplotlib seaborn
```

These libraries are required for data analysis and visualization.

### Step 3: Create the Project Folder

Create a folder named:

`COVID-19-Data-Analysis`

Place the Python file and CSV dataset inside the folder.

### Step 4: Open the Project in VS Code

Open Visual Studio Code, select **File → Open Folder**, and choose the project folder.

### Step 5: Check the Dataset Path

Ensure that `COVID19_Data_Analysis_Dataset.csv` is located in the correct folder or update the file path in the Python program.

### Step 6: Run the Python Program

Open the terminal in the project folder and execute:

```bash
python covid_analysis.py
```

Use your actual Python filename in this command.

### Step 7: Select a Menu Option

When the menu appears, enter the number of the analysis you want to perform.

## 🖥️ Menu-Driven System

The program provides the following menu:

```text
===== COVID-19 ANALYSIS =====
1. Statistical Summary
2. Global Trends
3. Country Comparison
4. Government Intervention
5. Country Trends
6. Exit
```

### Menu Options Explained

**Option 1 – Statistical Summary**

Displays dataset information and statistical values for new COVID-19 cases.

**Option 2 – Global Trends**

Displays a chart of cumulative cases, recoveries, and deaths over time.

**Option 3 – Country Comparison**

Displays a bar chart comparing the top five countries by cumulative cases.

**Option 4 – Government Intervention**

Displays a scatter plot of government intervention scores and new cases.

**Option 5 – Country Trends**

Displays cumulative case trends over time for the top five countries.

**Option 6 – Exit**

Displays an exit message and terminates the program.

## 🔍 Working of the Project

The project follows these steps:

1. Import the required Python libraries.
2. Create the `CovidAnalysis` class.
3. Load the CSV dataset using Pandas.
4. Convert the date column into datetime format.
5. Check whether the dataset is available.
6. Perform statistical calculations using NumPy.
7. Group and filter the data using Pandas.
8. Generate charts using Matplotlib and Seaborn.
9. Display a menu to let users select an operation.
10. Repeat the menu until the user selects Exit.

## 🧠 Python Concepts Used

This project demonstrates several important Python concepts.

### Object-Oriented Programming
- Classes
- Objects
- Constructors
- Instance variables
- Methods

### Data Analysis
- Pandas DataFrames
- NumPy arrays
- Statistical calculations
- Grouping and filtering
- Date conversion

### Control Flow
- `if`, `elif`, and `else`
- `while` loop
- `break` statement

### Exception Handling
- `try` and `except`
- Handling missing dataset files

### Data Visualization
- Line charts
- Bar charts
- Scatter plots
- Chart titles and axis labels
- Legends and grid lines

## 📈 Expected Results

After successfully running the project, users can expect:

- Statistical values for new COVID-19 cases.
- A global trend chart for cumulative cases, recoveries, and deaths.
- A bar chart comparing five countries.
- A scatter plot showing intervention scores against new cases.
- A line chart showing cumulative case trends for selected countries.

The actual results depend on the contents and quality of the CSV dataset.

## ⚠️ Important Notes

- Keep the CSV file in the correct location.
- Use the exact column names expected by the program.
- Install all required libraries before running the code.
- Ensure that the date column contains valid dates.
- The country comparisons depend on the recorded cumulative case values.
- The analysis describes the supplied dataset and should not be treated as real-time COVID-19 statistics.
- The intervention visualization shows an association, not proof of causation.

## 🚀 Future Improvements

The project can be enhanced in several ways:

- Add interactive charts and dashboards.
- Allow users to select specific countries.
- Add date-range filters.
- Include missing-value handling and data validation.
- Add more statistical measures, such as standard deviation.
- Add moving averages to smooth daily case trends.
- Include additional comparisons between regions.
- Export analysis results to CSV files.
- Add a graphical user interface.
- Develop an interactive dashboard using Streamlit.

## 🎓 Learning Outcomes

Through this project, I practiced:

- Loading and analyzing CSV datasets.
- Using Pandas for data manipulation.
- Performing numerical calculations with NumPy.
- Creating visualizations using Matplotlib and Seaborn.
- Applying object-oriented programming concepts.
- Writing menu-driven Python programs.
- Organizing code into reusable methods.
- Understanding the importance of data visualization.
- Interpreting patterns in historical data.

## 🏁 Conclusion

The COVID-19 Data Analysis project demonstrates the practical use of Python for data analysis and visualization. By combining NumPy, Pandas, Matplotlib, and Seaborn, the project processes COVID-19 records and presents important trends through statistical summaries and charts.

This project provides practical experience in programming, data manipulation, statistical analysis, and visualization. It also builds a foundation for more advanced projects in Data Science, Machine Learning, and exploratory data analysis.

## 👩‍💻 Author

**Digna Vora**

B.Sc. IT – AI & ML Specialization

**Areas of Interest:**
- Python Programming
- Data Science
- Artificial Intelligence
- Machine Learning
- Data Analysis



⭐ If you find this project useful, feel free to explore the code and learn from it.
