# Simple linear regression
import numpy as np 
import matplotlib.pyplot as plt 
  
'''
Reference: https://www.geeksforgeeks.org/linear-regression-python-implementation/

Simple linear regression: y=a+bx

b = cov(x,y) / var(y) = sum[(x-x_m)(y-y_m)]/sum[(x-x_m)^2] = (sum(Xi*Yi) - n*X_mean*Y_mean) / (sum(Xi^2) - n*X_mean^2)
a = Y_mean - b*X_mean 

R^2 = 1 - sum(Yi-Yi^)^2/sum(Yi-Yi_mean)^2
'''

def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 

    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # plotting the residual error 
    plt.scatter(x, y_pred-y, color = "green", 
               marker = "x", s = 30) 
    plt.axhline(0)
    # plot residual error as histogram
    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax.hist( y_pred-y, density=True)
    # function to show plot 
    plt.show() 
  
def main(): 
    # observations 
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
  
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb_0 = {} \n b_1 = {}".format(b[0], b[1])) 

    y_pred = b[0] +b[1]*x
    y_mean = np.mean(y)
    r_squared = 1 - np.sum((y_pred -y)*(y_pred-y)) /  np.sum((y -y_mean)*(y-y_mean)) 
    r_squared_adjusted = 1 - (1-r_squared*r_squared)* (len(y)-1)/(len(y)-1-1)

    print(f"r_squared score:{r_squared}, Adjusted r_squared:{r_squared_adjusted}")
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
  
if __name__ == "__main__": 
    main() 

# Multi-linear regression
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model, metrics 

'''
explained_variance_score = 1 – Var{y – y’}/Var{y}
( coefficient of determination / R^2 score)
'''
  
# load the boston dataset 
boston = datasets.load_boston(return_X_y=False) 
  
# defining feature matrix(X) and response vector(y) 
X = boston.data 
y = boston.target 
  
# splitting X and y into training and testing sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, 
                                                    random_state=1) 
  
# create linear regression object 
reg = linear_model.LinearRegression() 
  
# train the model using the training sets 
reg.fit(X_train, y_train) 
  
# regression coefficients 
print('Coefficients: \n', reg.coef_) 
  
# variance score: 1 means perfect prediction 
print('Variance score: {}'.format(reg.score(X_test, y_test))) 
  
# plot for residual error 
  
## setting plot style 
plt.style.use('fivethirtyeight') 
  
## plotting residual errors in training data 
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
            color = "green", s = 10, label = 'Train data') 
  
## plotting residual errors in test data 
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
            color = "blue", s = 10, label = 'Test data') 
  
## plotting line for zero residual error 
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2) 
  
## plotting legend 
plt.legend(loc = 'upper right') 
  
## plot title 
plt.title("Residual errors") 
  
## function to show plot 
plt.show() 

# polynominal regression
# first generate polynominal features with degree
# for example, if degree=2 input feature[x1,x2] => output is [1, x1, x2, x1^2, x2^2, x1x2]
# Then, fit linear regression line with newly created features


from sklearn.preprocessing import PolynomialFeatures 
 
# generate polynominal features 
poly = PolynomialFeatures(degree = 2) 
X_poly = poly.fit_transform(X) 
  
lin2 = LinearRegression() 
lin2.fit(X_poly, y) 


# lazy function
# RDD and Lazy function
import copy

class Datasource():

    def __init__(self,ls):
        self.ls=ls
        self.steps=[]

    def map(self, func):

        new_instance = copy.deepcopy(self)
        new_instance.steps.append((func,False))

        return new_instance

    def filter(self, func):

        new_instance = copy.deepcopy(self)
        new_instance.steps.append((func,True))

        return new_instance

    def collect(self):

        for func,is_filter in self.steps:
            if is_filter:
                self.ls = [ x for x in self.ls if func(x)]
            else:
                self.ls = list(map(func,self.ls))

        return self.ls       

d = Datasource([1,2,3]).map(lambda x: x*2).filter(lambda x: x==4).map(lambda x: x/2)

d1 = Datasource([1,2,3])
d2 = d1.map(lambda x: x*2)
d3 = d2.filter(lambda x: x==4)
d4 = d3.map(lambda x: x/2)

print(d1.collect())
print(d2.collect())
print(d3.collect())
print(d4.collect())


# Part of ARIMA model- auto regression
# y = a +fi1*X[i-1] + fi2*X[i-2]

import numpy as np

def pred_ar2(data, steps):

    X = np.array(data)
    X_mean = np.mean(X)
    N = len(data)

    c0 = np.var(X)

    # input is constant time series data
    if c0 == 0:
        for i in range(steps):
            data.append(data[-1])

    X_c11 = X[:-1]
    X_c12 = X[1:]

    c1 = np.sum((X_c11 - X_mean)*(X_c12 - X_mean)) / (N-1)

    X_c21 = X[:-2]
    X_c22 = X[2:]

    c2 = np.sum((X_c21 - X_mean)*(X_c22 - X_mean)) / (N-2)

    r1 = c1/c0
    r2 = c2/c0

    print(f"c0={c0}, c1= {c1}, c2 = {c2}, r1 = {r1}, r2={r2}")

    # if input is data looks like [1,-1,1,-1,...]
    if r1==-1:
        for i in range(steps):
            data.append(data[-2])

    fi1 = r1*(1-r2)/(1-r1*r1)
    fi2 = (r2 - r1*r1) / (1-r1*r1)

    print(f"fi1={fi1}, fi2= {fi2}")  

    for i in range(steps):
        data.append(fi1*data[-1] + fi2*data[-2])  

    return data

if __name__ =="__main__":

    x =[1,2] 

    for i in range(2,100):
        x.append (0.75*x[-1]-0.25*x[-2])

    pred=pred_ar2(x, 5)
