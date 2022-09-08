Notebook 

This contains the code for problem 1 and problem 2.
Problem 1 : Regex to extract the numbers from the string. 
Problem 2 : Predict whether the customer is likely to check in or not.
1) First feature analysis is performed. Example - cancellation percentage as per Nationality, Distribution channel and Marketing segment is analyzed.
2) Appropriate features are designed based on the above analysis.
3) Feature selection is done based on the feature importance obtained from Random Forest Model.
4) Selected features are used to train a neural network for predicting whether customer will check in or not.
5) Streamlit app is developed and deployed.


Link to colab notebook:
https://colab.research.google.com/drive/19Ej0PGEtXW-Wmt4x2PtwsoN73UIxgOMb#scrollTo=e8671bdf

Link to streamlit app:
https://shridharkn-temp-streamlitapp-j8sh8n.streamlitapp.com/

Link to screencast:
https://watch.screencastify.com/v/pV8YoZXBk62Z1Y7C9JQT


Answers to bonus questions:
1)

2.	Explain back propagation and tell us how you handle a dataset if 4 out of 30 parameters have null values more than 40 percentage?

i.	Backpropagation is the process of adjusting the weights and bias of the neural network based on loss computed. Weights and biases are tuned such that the loss function is minimized (Example – MSE in case regression, Binary cross entropy in case of binary classification). It is the crucial part in neural network training. It computes the gradient of the chosen loss function for by chain rule. Every forward propagation results in predictions based on the weights and biases at that time. Loss is computed and back propagation is initiated to adjust the weights and biases such that loss function is minimized.

ii.	Handling missing values: If the data set has large number of missing values, then possible solutions can be 
      1.	Drop the features that have large number of missing values if they are not a good predictor.
      2.	Treat the missing values as a separate category. Categorize the features with available data into groups. Whenever there is no information, then a new category called “No Info Available” can be made. Then one hot encode the feature so that it can now be used in the model.
      3.	Impute the missing values using nearest neighbors method( not recommended if missing data is very high in number).
      
