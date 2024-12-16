# NBA Player Height vs 3-Point Performance Analysis
# Overview
This project builds an end-to-end ETL pipeline to analyze the correlation between NBA player height and 3-point shooting performance since 1997. Data is extracted from Kaggle datasets and web scraping from BasketballReference – cleaned, combined, and analyzed.
The results include visualizations showcasing the change in trends and correlation over time.

# Features
Data Extraction: Combined player height data from Kaggle with 3-point performance stats scraped from Basketball-Reference.
Data Transformation: Filtered outliers, removed duplicates, and normalized season formats for consistency.
Correlation Analysis: Calculated the correlation coefficient between player height and 3-point shooting percentage for each season.
Visualization: Trend-line analysis visualized on Power BI. Created scatter plots of correlations by season using Matplotlib.
Data Storage: Saved the cleaned dataset and correlation results into CSV and Excel formats.

# Technologies Used
Python: Core programming language
Pandas: Data manipulation and transformation
BeautifulSoup: Web scraping
Matplotlib: Data visualization
Power BI: Data visualization

# Results
The analysis results show a significant decrease in the correlation between NBA player height and 3-point field goal percentage, over the seasons.
Loss of data during cleaning and transformation process, as well as the validity of data scrapes may lead to inaccuracies in the result.

