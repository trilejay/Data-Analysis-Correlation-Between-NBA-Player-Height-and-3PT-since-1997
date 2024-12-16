import kagglehub
import pandas as pd 
import openpyxl
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

# get dataset pathfile 
path1 = kagglehub.dataset_download("justinas/nba-players-data")
path2 = kagglehub.dataset_download("sumitrodatta/nba-aba-baa-stats")

print("Path to dataset file 1:", path1)
print("Path to dataset file 2:", path2)


def extract_heights(file_to_process): 
    '''
    Returns a dataframe with player_name and player_height columns
    '''
    # convert .csv file to pandas dataframe
    dataframe = pd.read_csv(file_to_process) 

    # filter .csv file for player name and height
    player_heights = dataframe[['player_name','player_height']]

    # print(player_heights)
    return player_heights

def extract_3(file_to_process):
    '''
    Extracts 3pt% and 3pa from players in file
    '''
    dataframe = pd.read_csv(file_to_process)
    percentages = dataframe[['Player', 'Pos', '3P%', '3PA', 'Season']]

    # convert season to int type (instead of 1996-1997)
    percentages['Season'] = percentages['Season'].str.split('-').str[0]
    percentages['Season'] = percentages['Season'].astype(int)
    
    # print(percentages)
    return percentages


def load_data(target_file, data):
    '''
    Loads dataframe into csv file
    '''
    data.to_csv(target_file)

# create dataframes
df1 = extract_heights('/Users/ilejay/Downloads/nba-project/all_seasons.csv')
df2 = extract_3('/Users/ilejay/Downloads/nba-project/NBA_Player_Stats_2.csv')

# merge dataframes with inner join on player name
merged_df = pd.merge(df1, df2, left_on='player_name', right_on='Player', how='inner')
merged_df = merged_df.drop(columns=['Player'])

# filter outliers
filtered_df = merged_df[(merged_df['3PA'] > 0.1) & (merged_df['3P%'] < 1.0)]


# filtered_df = filtered_df.drop_duplicates(subset='player_name', keep='last')
# correlation_per_year = filtered_df.groupby('Year').apply(lambda group: group[['player_height', '3P%']].corr().iloc[0, 1])
# correlation_per_year.to_excel("correlation.xlsx")

def calculate_correlation(dataframe):
    '''
    calculates correlation coefficient of dataframe
    '''
    
    correlation_data = []

    # group by each season, then calculate correlation coefficient 
    for season, group in dataframe.groupby('Season'):
        if not group['3P%'].isnull().all() and not group['player_height'].isnull().all():
            correlation = group['3P%'].corr(group['player_height'])
        else:
            correlation = None
        correlation_data.append({'Season': season, 'Correlation': correlation})
    
    correlation_df = pd.DataFrame(correlation_data)
    return correlation_df


print(filtered_df)
load_data('three-points.csv', filtered_df)
filtered_df.to_excel("three-points.xlsx")
correlation_df = calculate_correlation(filtered_df)
correlation_df.to_csv('correlation_per_season.csv', index=False)

plt.figure(figsize=(10, 6))
plt.scatter(correlation_df['Season'], correlation_df['Correlation'], color='blue', label='Correlation')

plt.title('Correlation Between Height and 3P% by Season', fontsize=16)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Correlation Coefficient', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()
