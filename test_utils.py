from utils import compare

print 1 , compare({},{}) == True
print 2 , compare({},[]) == False
print 3 , compare({'a':[1]}, {'a':1}) == True