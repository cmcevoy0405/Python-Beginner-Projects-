import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#Read Data from file
data_file_path = r"train.csv"

housing_data = pd.read_csv(data_file_path)

#Use pandas to find key statistics
print(housing_data.describe())

#Find dependent variable (Price)
print(housing_data.columns)

y = housing_data.SalePrice

#Find independent variables
feature_names = ["LotArea", "YearBuilt", "1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd"]

X = housing_data[feature_names]

#Fit the model
housing_model = DecisionTreeRegressor(random_state = 1)

housing_model.fit(X, y)

#Find house price predictions
predictions = housing_model.predict(X)

print(predictions)

print(y.head())

error = mean_absolute_error(y, predictions)
print(error)

#Using train_test_split to avoid using the same sampled for validation, getting a true model validation
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

housing_model = DecisionTreeRegressor(random_state = 1)

housing_model.fit(train_X, train_y)

val_predictions = housing_model.predict(val_X)


print(val_predictions[:5])
print(y.head())

print(mean_absolute_error(val_y, val_predictions))

#Overfitting and underfitting in the model
#function to return mae for certain values of leaf_nodes
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
#for loop printing mean_absolute_error for leaf_nodes in range 5-500, printing leaf_node value for lowest mae
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)
print(best_tree_size)

#Running optimized model
housing_model = DecisionTreeRegressor(max_leaf_nodes = best_tree_size, random_state = 1)
housing_model.fit(train_X ,train_y)
predict = housing_model.predict(X)
print(predict[:5])
mae = print(mean_absolute_error(y, predict))

#Using random forest models
rf_model = RandomForestRegressor()
rf_model.fit(train_X, train_y)

rf_predictions = rf_model.predict(val_X)
print(rf_predictions[:5])

print(mean_absolute_error(val_y, rf_predictions))
