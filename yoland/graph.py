import numpy as np
import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn import cross_validation

train_set = pandas.read_csv("./data/train_ver2.csv")
print(train_set.desc())
