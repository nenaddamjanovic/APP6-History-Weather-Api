from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read the CSV file into a DataFrame
df = pd.read_csv('files/p_dictionary.csv')


@app.route('/')
def index():
    return render_template('p_home_pandas_data.html',
                           tables=[df.to_html(classes='data')],
                           titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug=True, port=5002)

# -----------------------------------------------------------------

# List of states corresponding to each city
states = [
    'New York', 'California', 'Illinois', 'Texas', 'Arizona',
    'Pennsylvania', 'Texas', 'California', 'Texas', 'California',
    'Texas', 'Florida', 'Texas', 'Ohio', 'North Carolina',
    'California', 'Indiana', 'Washington', 'Colorado', 'District of Columbia'
]

# Add the 'State' column to the DataFrame
df['State'] = states

# Display complete the DataFrame
print(f"{df}\n")

# Select the 'Name' and 'City' columns
print(f"{df[['Name', 'City']]}\n")

# Select rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print(f"{filtered_df}\n")

# Group by 'City' and calculate the mean age for each city
grouped_df = df.groupby('City')['Age'].mean()
print(f"{grouped_df}\n")

# Calculate the mean age -> Average
mean_age = df['Age'].mean()
print(f'Mean Age: {mean_age}\n')

# Calculate the maximum salary
max_salary = df['Salary'].max()
print(f'Max Salary: {max_salary}\n')

# Calculate the minimum salary and group by age
grouped_min_salary = df.groupby("Age")['Salary'].min()
print(f'{grouped_min_salary}\n')

# The .mean() method is part of a suite of aggregation functions in pandas,
# such as .sum(), .min(), .max(), .median(), and others, which allow for
# efficient computation of summary statistics on data.
