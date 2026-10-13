# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create a class for COVID-19 analysis
class CovidAnalysis:

    # Constructor: Load CSV dataset
    def __init__(self, file_path="COVID19_Data_Analysis_Dataset.csv"):
        try:
            # Read CSV file using Pandas
            self.df = pd.read_csv(file_path)

            # Convert Date column into datetime format
            self.df['Date'] = pd.to_datetime(self.df['Date'], dayfirst=True )

            print("Dataset Loaded Successfully!")

        except FileNotFoundError:
            # Display message if file is not found
            print("CSV file not found!")
            self.df = pd.DataFrame()

    # Calculate statistical summary
    def summary(self):
        if self.df.empty:
            return

        # Display dataset information
        print("\nDataset Information:")
        self.df.info()

        # Convert New_Cases column into NumPy array
        cases = self.df['New_Cases'].to_numpy()

        # Calculate statistical values
        print("\nStatistical Summary")
        print("Mean:", np.mean(cases))
        print("Median:", np.median(cases))
        print("Maximum:", np.max(cases))
        print("Minimum:", np.min(cases))

    # Display global COVID-19 trends
    def global_trends(self):
        if self.df.empty:
            return

        # Group data by date and calculate total values
        data = self.df.groupby('Date')[['Cumulative_Cases', 'Cumulative_Recovered','Cumulative_Deaths']].sum()

        # Create a line chart
        data.plot(figsize=(10, 5))

        # Add chart title and labels
        plt.title("Global COVID-19 Trends")
        plt.xlabel("Date")
        plt.ylabel("Total Count")

        # Display grid and chart
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Compare the top 5 countries
    def country_comparison(self):
        if self.df.empty:
            return

        # Find countries with the highest cumulative cases
        data = self.df.groupby('Country')['Cumulative_Cases'].max().nlargest(5)

        # Create a bar chart
        data.plot(kind='bar', color='skyblue')

        # Add chart title and labels
        plt.title("Top 5 Countries by COVID-19 Cases")
        plt.xlabel("Country")
        plt.ylabel("Cumulative Cases")

        # Display chart
        plt.tight_layout()
        plt.show()

    # Analyze government intervention
    def intervention(self):
        if self.df.empty:
            return

        # Create a scatter plot to compare intervention scores
        # with the number of new COVID-19 cases
        sns.scatterplot(
            data=self.df,
            x='Government_Intervention_Score',
            y='New_Cases',
            hue='Region'
        )

        # Add chart title and display
        plt.title("Government Intervention vs New Cases")
        plt.tight_layout()
        plt.show()

    # Display COVID-19 trends for top countries
    def country_trends(self):
        if self.df.empty:
            return

        # Find the top 5 countries by cumulative cases
        top = self.df.groupby('Country')[
            'Cumulative_Cases'
        ].max().nlargest(5).index

        # Filter data for those countries
        data = self.df[self.df['Country'].isin(top)]

        # Create a line chart for country-wise trends
        sns.lineplot(
            data=data,
            x='Date',
            y='Cumulative_Cases',
            hue='Country'
        )

        # Add chart title and display
        plt.title("COVID-19 Trends by Country")
        plt.tight_layout()
        plt.show()


# Create an object of the class
analyzer = CovidAnalysis()


# Repeat the menu until the user exits
while True:

    # Display menu options
    print("\n===== COVID-19 ANALYSIS =====")
    print("1. Statistical Summary")
    print("2. Global Trends")
    print("3. Country Comparison")
    print("4. Government Intervention")
    print("5. Country Trends")
    print("6. Exit")

    # Get choice from the user
    choice = input("Enter your choice: ")

    # Call the selected method
    if choice == '1':
        analyzer.summary()

    elif choice == '2':
        analyzer.global_trends()

    elif choice == '3':
        analyzer.country_comparison()

    elif choice == '4':
        analyzer.intervention()

    elif choice == '5':
        analyzer.country_trends()

    elif choice == '6':
        # Stop the program
        print("Thank you! Program Ended.")
        break

    else:
        # Handle invalid menu choices
        print("Invalid choice! Enter 1 to 6.")
