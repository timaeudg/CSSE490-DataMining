# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
import matplotlib as plt

# <codecell>

hair_eye_color = pd.read_csv("HairEyeColor.csv", index_col=0)

# <codecell>

pivoted = pd.pivot_table(hair_eye_color, values='Freq', rows=['Eye', 'Sex'], cols=['Hair'])

# <codecell>

hairSexSum = 1.0*pivoted.sum(axis=1)

# <codecell>

normalized_pivoted = 100.0*pivoted.div(1.0*hairSexSum, axis='index')

# <codecell>

normalized_pivoted

# <codecell>

axes = normalized_pivoted.plot(kind='bar', stacked=True)
plt.pyplot.show()

# <codecell>


# <codecell>


# <codecell>


