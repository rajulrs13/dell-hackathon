import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

def reg_services(payload_service, payload_region, payload_year):

    # Importing Data
    print()
    print("Importing Dataset......")
    dataset = pd.read_csv('customer-dataset-reg.csv')
    
    # Processing Data
    print()
    print("Preprocessing Data.....")
    temp = dataset.iloc[:, :].values
    laptop_count=[]
    year=[]
    max_year = temp[len(temp) - 1][4]
    for i in range(2009, max_year + 1):
        year.append(i)
    if payload_service == 'RAM':        
        if payload_region == 'Global':
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1 and temp[i][13] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0 
        else:
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1  and temp[i][8]==payload_region and temp[i][13] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0   
    elif payload_service == 'HDD':
        if payload_region == 'Global':
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1 and temp[i][14] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0 
        else:
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1  and temp[i][8]==payload_region and temp[i][14] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0
    elif payload_service == 'OS':
        if payload_region == 'Global':
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1 and temp[i][15] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0 
        else:
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1  and temp[i][8]==payload_region and temp[i][15] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0
    elif payload_service == 'Office':
        if payload_region == 'Global':
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1 and temp[i][16] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0 
        else:
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1  and temp[i][8]==payload_region and temp[i][16] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0
    elif payload_service == 'Antivirus':
        if payload_region == 'Global':
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1 and temp[i][17] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0 
        else:
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1  and temp[i][8]==payload_region and temp[i][17] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0
    elif payload_service == 'Warranty':
        if payload_region == 'Global':
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1 and temp[i][18] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0 
        else:
            tempc=0
            for j in range(0,len(year)):
                for i in range(0,len(temp)):
                    if temp[i][12] == 1  and temp[i][8]==payload_region and temp[i][18] == 1:
                        if temp[i][4] == year[j]:
                            tempc=tempc+1       
                laptop_count.append(tempc)
                tempc=0

    t1=[]
    y=[]
    for j in range(0,len(year)):
        t=year[j]
        t1.append(t)
        y.append(t1)
        t1=[]
    X=y
    y=laptop_count
    
     # Training the Model
    print()
    print("Training the Model.....")
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree = 4)
    X_poly = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly, y)
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y)
    
    # Predicting the Values
    print()
    print("Predicting Values......")
    y_pred = lin_reg.predict(poly_reg.fit_transform(X))
    year_val = lin_reg.predict(poly_reg.fit_transform([[payload_year]]))
    
    return {"X" : X, "y" : y, "y_pred" : y_pred.tolist(), "year_val" : year_val.tolist()}
    

    # Visualising the Polynomial Regression results
    """plt.scatter(X, y, color = 'red')
    plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
    plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    
    # Visualising the Polynomial Regression results (for higher resolution and smoother curve)
    X_grid = np.arange(min(year), max(year), 0.1)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color = 'red')
    plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
    plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()"""
