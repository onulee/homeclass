from sklearn.preprocessing import PolynomialFeatures


poly = PolynomialFeatures(degree=2,include_bias=False)
poly.fit([[2,3,4]])
print(poly.transform( [[2,3,4]] ))
print(poly.transform( [[2,3,4]] ).shape)