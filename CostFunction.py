#Implementation of cost function

def computeCost(X,y,theta):
  k = (1 // (2 * m))
  theta0 = 5
  theta1 = 1
  total = 0
  for i in range(m):
    total = total + (((theta0 + theta1*X[i])-y[i])**2)
  return k* total
    
