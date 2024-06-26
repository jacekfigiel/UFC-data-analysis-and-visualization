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


def save_plot_to_png(fig, slide_title):
    img_path = f"{slide_title}.png"
    fig.savefig(img_path)
    slide_layout = prs.slide_layouts[5]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    title.text = slide_title
    pic = slide.shapes.add_picture(img_path, Inches(1), Inches(1), width=Inches(8.5), height=Inches(4.75))

# Stance Distribution
fig = plt.figure()
sns.countplot(data=df, x='stance', color='green')
plt.title('Stance Distribution')
save_plot_to_png(fig, 'Stance Distribution')
plt.close(fig)

# Stance vs. Strikes Landed
fig = plt.figure()
sns.boxplot(data=df, x='stance', y='significant_strikes_landed_per_minute', color='green')
plt.title('Stance vs. Strikes Landed')
save_plot_to_png(fig, 'Stance vs. Strikes Landed')
plt.close(fig)
