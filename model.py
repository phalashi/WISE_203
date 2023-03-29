# %%
# Importing modules

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import *


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis


import matplotlib.pyplot as plt
import seaborn as sns


# %%
# Reading in data
df = pd.read_csv("phishing.csv")


# %%
# Extracting labels
labels = df.loc[:, ~df.columns.str.contains('class')]


# %%
# Extracting target
target = df['class']

training_labels, testing_labels, training_target, testing_target  = train_test_split(labels, target, random_state = 42, )

classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)

# Fitting classifier
classifier.fit(training_labels, training_target)

# Updating predictions dict
prediction = classifier.predict(testing_labels)