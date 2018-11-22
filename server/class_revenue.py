# Importing the libraries
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd

def class_service(payload_age, payload_year, payload_ram, payload_hdd, payload_location, payload_warranty):
    
    # Importing Data
    print()
    print("Importing Dataset......")
    dataset = pd.read_csv('ram-hdd-final.csv')
    
    # Processing Data
    print()
    print("Preprocessing Data.....")
    X_test= [{"Year":payload_year,"RAM":payload_ram,"HDD":payload_hdd,"Location":payload_location,"Warranty":payload_warranty,"Age":payload_age}]
    x_t=[[X_test[0]['Year'], X_test[0]['RAM'],X_test[0]['HDD'],X_test[0]['Location'], X_test[0]['Warranty'], X_test[0]['Age']]]

    X = dataset.iloc[:, 3:9].values
    xtemp=np.ndarray.tolist(X)
    xtemp=xtemp+x_t
    xtemp=np.array(xtemp)
    X=xtemp

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    X[:,0]=labelencoder_X.fit_transform(X[:,0])
    X[:,1]=labelencoder_X.fit_transform(X[:,1])
    X[:,2]=labelencoder_X.fit_transform(X[:,2])
    X[:,3]=labelencoder_X.fit_transform(X[:,3])

    onehotencoder = OneHotEncoder(categorical_features = [0])
    X = onehotencoder.fit_transform(X).toarray()
    X = X[:, 1:]

    onehotencoder = OneHotEncoder(categorical_features=[9])
    X = onehotencoder.fit_transform(X).toarray()
    X = X[:, 1:]

    onehotencoder = OneHotEncoder(categorical_features=[13])
    X = onehotencoder.fit_transform(X).toarray()
    X = X[:, 1:]

    onehotencoder = OneHotEncoder(categorical_features=[18])
    X = onehotencoder.fit_transform(X).toarray()
    X = X[:, 1:]

    y=dataset.iloc[:,12].values

    E=X[:-1,:]
    
    # Training the Model
    print()
    print("Training the Model.....")
    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    classifier.fit(E, y)

    X_yo=X[2000]

    # Predicting the Values
    print()
    print("Predicting Values......")
    X_yo=X_yo.reshape(1, -1)
    y_pred = classifier.predict(X_yo)
    temp_list = y_pred.tolist()
    num = temp_list[0]

    suggestions = {}
    suggestions['Need']='No'
    if int(payload_age) <= 50:
        if num == 1:
            suggestions['Need']='Yes'
            suggestions['RAM']=[]
            suggestions['HDD']=[]
            suggestions['Warranty']='No'
            if payload_ram <= 4:
                suggestions['RAM'].append('HDD')
            if payload_hdd < 500:
                suggestions['HDD'].append('RAM')
                suggestions['HDD'].append('OS')
            if payload_warranty + int(payload_year) <= 2019:
                suggestions['Warranty']='Yes'

    return {"retvalue" : y_pred.tolist(),"suggestions": suggestions}
