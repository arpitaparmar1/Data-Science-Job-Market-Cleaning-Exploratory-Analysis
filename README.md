# Data-Science-Job-Market-Cleaning-Exploratory-Analysis
This project involves an end-to-end data cleaning and analysis pipeline for a dataset of Data Science Job Postings. The primary goal was to transform raw, unstructured job descriptions and salary data into a clean format suitable for identifying key salary drivers and the most in-demand technical skills in 2025.

📂 Project Structure:

DS_clean_data.py: The Python script containing the cleaning logic, feature engineering, and visualization code.

Uncleaned_DS_jobs.csv: The raw dataset featuring messy salary strings, unstructured job descriptions, and mixed company ratings.

clean_data1.csv: The final, high-quality dataset ready for machine learning or reporting.

🛠️ Data Engineering & Cleaning:

The script implements several sophisticated cleaning techniques using pandas and numpy:

Salary Parsing: Deconstructed the Salary Estimate column to create new numeric features: Min_salary, Max_salary, and Avg_salary.

Company Name Sanitization: Removed rating scores that were appended to company names (e.g., "Company\n3.5" to "Company").

State Extraction: Parsed the Location field to isolate the Job_state and standardized "Remote" listings.

Company Age: Calculated the age of each company based on the current year (2025) and the Founded year.

Missing Value Handling: Identified and replaced placeholder values like -1 and "Unknown" with NaN for statistical accuracy.

📊 Visual Insights:

The analysis produces several key visualizations using Seaborn and Matplotlib:

Skill Distribution by Title: A pie chart visualizing which job titles require the highest density of technical skills.

Salary Benchmarking: (Optional code included) Analysis of average salaries across the top 5 most common job titles.

Revenue Analysis: A distribution plot of company revenues across the dataset.

🚀 Installation & Usage:

1.Clone the repository:

Bash

(https://github.com/arpitaparmar1/Data-Science-Job-Market-Cleaning-Exploratory-Analysis

2.Install dependencies:

BasH

pip install pandas numpy matplotlib seaborn

3.Run the script:

Ensure the file path in DS_clean_data.py matches your local directory and run:

Bash

python DS_clean_data.py

