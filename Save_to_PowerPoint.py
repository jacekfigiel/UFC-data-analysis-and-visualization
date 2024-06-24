import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from pptx import Presentation
from pptx.util import Inches

df = pd.read_csv('ufc-fighters-statistics.csv')

df['stance'] = df['stance'].fillna('Unspecified')

# calculate the day of birth
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%Y-%m-%d', errors='coerce')
df['age'] = df['date_of_birth'].apply(lambda x: datetime.now().year - x.year if pd.notnull(x) else None)

# Handle the placeholder date by setting the age to None for those entries
df['age'] = df['age'].replace(datetime.now().year - 1900, None)

# Create a PowerPoint presentation object
prs = Presentation()



