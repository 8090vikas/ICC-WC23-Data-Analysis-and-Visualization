import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


bat_df = pd.read_csv('icc_wc_23_bat.csv')
bowl_df = pd.read_csv('icc_wc_23_bowl.csv')


bat_df['strike_rate'] = (bat_df['runs'] / bat_df['balls']) * 100  
bat_df['strike_rate'] = bat_df['strike_rate'].round(2)


bowl_df['economy_rate'] = (bowl_df['runs'] / bowl_df['overs']).round(2)




top_10_batters = bat_df.nlargest(10, 'runs')
plt.figure(figsize=(12, 6))
plt.bar(top_10_batters['player'], top_10_batters['runs'], color='skyblue')
plt.xlabel('Players')
plt.ylabel('Total Runs')
plt.title('Top 10 Players by Total Runs Scored')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


bat_df_filtered = bat_df[bat_df['balls'] >= 50]
top_10_strikers = bat_df_filtered.nlargest(10, 'strike_rate')
plt.figure(figsize=(12, 6))
plt.bar(top_10_strikers['player'], top_10_strikers['strike_rate'], color='orange')
plt.xlabel('Players')
plt.ylabel('Strike Rate')
plt.title('Top 10 Players by Strike Rate (Minimum 50 Balls Faced)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


team_runs = bat_df.groupby('team')['runs'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(team_runs.index, team_runs.values, color='green')
plt.xlabel('Teams')
plt.ylabel('Total Runs')
plt.title('Team-wise Total Runs Scored')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


top_10_batters['4s'] = top_10_batters['4s'].astype(int)
top_10_batters['6s'] = top_10_batters['6s'].astype(int)
plt.figure(figsize=(12, 6))
bar_width = 0.35
index = np.arange(len(top_10_batters['player']))
plt.bar(index, top_10_batters['4s'], bar_width, label='4s', color='blue')
plt.bar(index + bar_width, top_10_batters['6s'], bar_width, label='6s', color='red')
plt.xlabel('Players')
plt.ylabel('Count')
plt.title('Comparison of 4s and 6s Hit by Top 10 Players')
plt.xticks(index + bar_width / 2, top_10_batters['player'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()


top_10_bowlers = bowl_df.nlargest(10, 'wickets')
plt.figure(figsize=(12, 6))
plt.bar(top_10_bowlers['player'], top_10_bowlers['wickets'], color='purple')
plt.xlabel('Players')
plt.ylabel('Wickets')
plt.title('Top 10 Bowlers by Wickets Taken')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


bowl_df_filtered = bowl_df[bowl_df['overs'] >= 10]
top_10_economy = bowl_df_filtered.nsmallest(10, 'economy_rate')
plt.figure(figsize=(12, 6))
plt.bar(top_10_economy['player'], top_10_economy['economy_rate'], color='teal')
plt.xlabel('Players')
plt.ylabel('Economy Rate')
plt.title('Top 10 Bowlers by Economy Rate (Minimum 10 Overs Bowled)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


team_wickets = bowl_df.groupby('team')['wickets'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(team_wickets.index, team_wickets.values, color='gold')
plt.xlabel('Teams')
plt.ylabel('Total Wickets')
plt.title('Team-wise Total Wickets Taken')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


top_10_bowlers['maidens'] = top_10_bowlers['maidens'].astype(int)
top_10_bowlers['wd'] = top_10_bowlers['wd'].astype(int)
plt.figure(figsize=(12, 6))
plt.bar(index, top_10_bowlers['maidens'], bar_width, label='Maidens', color='blue')
plt.bar(index + bar_width, top_10_bowlers['wd'], bar_width, label='Wides', color='red')
plt.xlabel('Players')
plt.ylabel('Count')
plt.title('Comparison of Maidens and Wides by Top 10 Bowlers')
plt.xticks(index + bar_width / 2, top_10_bowlers['player'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
