import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

apple_stock_data = pd.read_csv('AppleCompanyStockCSV.csv')
print("The Apple company stock data set is as follows :\n ", apple_stock_data)

feature_list = ['month', 'open', 'high', 'low', 'close', 'volume']

# Separating the features for processing
X_range = apple_stock_data.loc[:, feature_list].values
print("The data set values for computation :\n", X_range)

# Getting the different class labels
Y_range = apple_stock_data.loc[:, ['year']].values
print("Y_Range :", Y_range)
# Standardizing the feature set using the StandardScaler that brings the mean value of a column to zero and the standard
# deviation to 0
X = StandardScaler().fit_transform(X_range)
print("The dataset after standardizing :\n", X)

# Applying PCA on the dataset for reducing the number of features so that the visualization of the data is clear and
# concise. This process is also called as dimensionality reduction.
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X)
principal_data_frame = pd.DataFrame(data=principal_components, columns=['principal_component_1', 'principal_component_2'])
print("The PCA's are as follows : \n", principal_data_frame)

# Concatenating the results along with the target values i.e., the Y_range
principal_data_frame['Target'] = Y_range
print("The final data frame with the concatenated target values : \n", principal_data_frame)

# Plotting the dimensionality reduced data
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA for Apple stock information', fontsize=20)

targets = [_ for _ in range(2000, 2019)]
print("The targets are: ", targets)
for target in targets:
    # In the following LOC's, we are plotting the rows such that each target row will be mapped with the row having the
    # same target value and then all these values are collected in the variable indicesToKeep.
    # After that we are passing the x value and the y value to the scatter function where 'p_c_1' and 'p_c_2' are the
    # column names to be plotted. In simple words, all the rows which are part of 'Iris_viriginca' are clubbed together
    # and then the 'p_c_1' gives the x value of the row from indicesToKeep is plotted, similarly the y value
    indicesToKeep = principal_data_frame['Target'] == target
    ax.scatter(principal_data_frame.loc[indicesToKeep, 'principal_component_1'],
               principal_data_frame.loc[indicesToKeep, 'principal_component_2'])
ax.legend(targets)
ax.grid()
plt.show()
print("WE learned about PCA in this assignment")
