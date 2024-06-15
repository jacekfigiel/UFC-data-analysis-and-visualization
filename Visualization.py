import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


df = pd.read_csv('ufc-fighters-statistics.csv')
# fill gaps in stance
df['stance'] = df['stance'].fillna('Unspecified')

# calculate the day of birth
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%Y-%m-%d', errors='coerce')
df['age'] = df['date_of_birth'].apply(lambda x: datetime.now().year - x.year if pd.notnull(x) else None)

# Handle the placeholder date by setting the age to None for those entries
df['age'] = df['age'].replace(datetime.now().year - 1900, None)

print(df.columns)
print(df.head())
print(df.info())

'''stance viz'''
sns.countplot(data=df, x='stance', color='green')

'''comparing stance to strikes landed'''
sns.boxplot(data=df, x='stance', y='significant_strikes_landed_per_minute', color='green')

'''Distribution of Wins, Losses, and Draws'''
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(df['wins'], bins=20, kde=True, ax=axs[0], color='green').set(title='Wins Distribution')
sns.histplot(df['losses'], bins=20, kde=True, ax=axs[1], color='red').set(title='Losses Distribution')
sns.histplot(df['draws'], bins=20, kde=True, ax=axs[2], color='blue').set(title='Draws Distribution')

'''Height vs. Weight'''
sns.scatterplot(data=df, x='height_cm', y='weight_in_kg', hue='stance', palette='muted')
plt.title('Height vs. Weight')

'''Age Distribution'''
sns.histplot(df['age'], bins=20, kde=True, color='purple')
plt.title('Age Distribution')

sns.pairplot(df, vars=['significant_strikes_landed_per_minute', 'significant_striking_accuracy', 'significant_strikes_absorbed_per_minute', 'significant_strike_defence'], hue='stance', palette='bright')

'''Takedown metrics'''
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

sns.boxplot(data=df, x='stance', y='average_takedowns_landed_per_15_minutes', ax=axs[0, 0])
axs[0, 0].set_title('Average Takedowns per 15 Minutes')

sns.boxplot(data=df, x='stance', y='takedown_accuracy', ax=axs[0, 1])
axs[0, 1].set_title('Takedown Accuracy')

sns.boxplot(data=df, x='stance', y='takedown_defense', ax=axs[1, 0])
axs[1, 0].set_title('Takedown Defense')

sns.boxplot(data=df, x='stance', y='average_submissions_attempted_per_15_minutes', ax=axs[1, 1])
axs[1, 1].set_title('Average Submissions per 15 Minutes')


'''win rate vs significant striking'''
# Calculate win rate
df['total_fights'] = df['wins'] + df['losses'] + df['draws']
df['win_rate'] = df['wins'] / df['total_fights']

sns.scatterplot(data=df, x='significant_striking_accuracy', y='win_rate', hue='stance', palette='viridis')
plt.title('Win Rate vs. Significant Striking Accuracy')


fig, axs = plt.subplots(1, 2, figsize=(15, 5))

sns.violinplot(data=df, x='stance', y='reach_in_cm', ax=axs[0])
axs[0].set_title('Reach Distribution by Stance')

sns.violinplot(data=df, x='stance', y='weight_in_kg', ax=axs[1])
axs[1].set_title('Weight Distribution by Stance')



plt.tight_layout()
plt.show()