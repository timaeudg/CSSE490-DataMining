# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd

# <codecell>

crimes = pd.read_csv("Crimes_-_2001_to_present.csv", index_col=0)

# <codecell>

crimes.columns

# <codecell>

print crimes['Ward'].value_counts().to_string()

# <codecell>

deathly_violent = ['HOMICIDE']

# <codecell>

violent_crimes_lots = crimes.ix[(crimes['Primary Type'].isin(deathly_violent)) & (crimes['Ward'] == 28)]
violent_crimes_few = crimes.ix[(crimes['Primary Type'].isin(deathly_violent)) & (crimes['Ward'] == 19)]
violent_crimes_mid = crimes.ix[(crimes['Primary Type'].isin(deathly_violent)) & (crimes['Ward'] == 18)]

# <codecell>

import matplotlib.pylab as plt

# <codecell>

import numpy as np
colors_lots = np.where(violent_crimes_lots['Arrest'], 'g', 'r')
colors_few = np.where(violent_crimes_few['Arrest'], 'g', 'r')
colors_mid = np.where(violent_crimes_mid['Arrest'], 'g', 'r')

# <codecell>

fig = plt.figure(figsize=(10,10), dpi=200)
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Latitude')
ax1.set_ylabel('Longitude')
ax1.set_title('28th Ward Crime locations')
ax1.set_autoscale_on(False)
ax1.set_xlim([crimes['Longitude'].min(), crimes['Longitude'].max()])
ax1.set_ylim([crimes['Latitude'].min(), crimes['Latitude'].max()])
violent_scatter = plt.scatter(violent_crimes_lots['Longitude'], violent_crimes_lots['Latitude'], c=colors_lots)
plt.savefig("bigCrime.png", dpi=92)

# <codecell>

fig = plt.figure(figsize=(10,10), dpi=200)
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Latitude')
ax1.set_ylabel('Longitude')
ax1.set_title('19th Ward Crime locations')
ax1.set_autoscale_on(False)
ax1.set_xlim([crimes['Longitude'].min(), crimes['Longitude'].max()])
ax1.set_ylim([crimes['Latitude'].min(), crimes['Latitude'].max()])
violent_scatter = plt.scatter(violent_crimes_few['Longitude'], violent_crimes_few['Latitude'], c=colors_few)
plt.savefig("fewCrime.png", dpi=92)

# <codecell>

fig = plt.figure(figsize=(10,10), dpi=200)
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Latitude')
ax1.set_ylabel('Longitude')
ax1.set_title('18th Ward Crime locations')
ax1.set_xlim([crimes['Longitude'].min(), crimes['Longitude'].max()])
ax1.set_ylim([crimes['Latitude'].min(), crimes['Latitude'].max()])
violent_scatter = plt.scatter(violent_crimes_mid['Longitude'], violent_crimes_mid['Latitude'], c=colors_mid)
plt.savefig("midCrime.png", dpi=92)

# <codecell>

violent_crimes_lots['Arrest'].value_counts().plot(kind='bar', title="28th Ward Homicide Arrests")

# <codecell>

violent_crimes_mid['Arrest'].value_counts().plot(kind='bar', title="18th Ward Homicide Arrests")

# <codecell>

violent_crimes_few['Arrest'].value_counts().plot(kind='bar',title="19th Ward Homicide Arrests")

# <codecell>


