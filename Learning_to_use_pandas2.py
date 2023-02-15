import pandas as pd
d = {
     'Machine Learning Tasks': ['Clustering', 'Classification', 'Regression Analysis', 'Dimensionality Reduction'],
     'Example of algorithms #1': ['K-means', 'SVM', 'Linear Regression', 'PCA'],
     'Example of algorithms #2': ['K-means++', 'Multiclass SVM', 'Nonlinear regression', 'ICA']}
df = pd.DataFrame(data=d)
df
