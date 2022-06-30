from logging import exception
from sklearn import svm,metrics
import glob, os.path, re

files = glob.glob("deeplearning/train/*.txt")  
print(files)

count = [0]*26
print(count)