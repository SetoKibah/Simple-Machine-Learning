#Description: Build a simple machine learning python program
#Import dependencies
from sklearn.linear_model import LinearRegression
import random

#Create two empty lists
feature_set = []
target_set = []

#Get the number of rows for the data set
number_of_rows = 200

#Limit the possible values in the data set
random_number_limit = 20000

#Create the data set

#Create the feature data set
for i in range(0, number_of_rows):
  x = random.randint(0, random_number_limit)
  y = random.randint(0, random_number_limit)
  z = random.randint(0, random_number_limit)

  #Create a linear function for the target data set
  function = (10*x)+(2*y)+(3*z)

  #Append the data to the lists
  feature_set.append([x,y,z])
  target_set.append(function)

  #Create the Linear regression model
  model = LinearRegression()
  model.fit(feature_set, target_set)

  #Create the test data set
  test_set = [[8, 10, 0]] #Expected output = function(8,10,0) = (10*8) + (2*10)+ (3*0) = 100
  prediction = model.predict(test_set)
  print(f"Prediction: {prediction} Coefficients: {model.coef_}")