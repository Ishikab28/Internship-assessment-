import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score, classification_report 
import pickle as pickle



# Create X and Y data
def create_model(data):
    X = data.drop(['diagnosis'], axis=1)
    Y = data['diagnosis']
      
# Scale the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

# Split the data 
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )
    
# Training the model
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
# Testing the model 
    y_pred = model.predict(X_test)
    print('Accuracy of our model: \n', accuracy_score(Y_test, y_pred))
    print()
    print('Classification report: \n', classification_report(Y_test, y_pred))

    return model, scaler

    

def get_clean_data():
    data = pd.read_csv("data/data.csv")
    
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})   
    
    return data

def main():
    data = get_clean_data()
    print(data.head())
    print(data.info())
    
    model, scaler = create_model(data)
    
    with open('model/model.pkl', 'wb') as file:
        pickle.dump(model, file)
        
    with open('model/scaler.pkl', 'wb') as file:
        pickle.dump(scaler, file)
    
    # test_model(model)


if __name__ == "__main__":
    main()