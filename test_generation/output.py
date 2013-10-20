import unittest, inspect
import input
import itertools

class tempVar(object):
    range = 0
    array_min = []
    array_max = []   
    def __init__(self,range):
        self.range = range

# Get doc in main
def getInputDocs():
    a = inspect.getdoc(input.main)
    a = inspect.cleandoc(a)
    b = a.splitlines()
    line1 = b[0]
    z = inspect.getargspec(input.main)
    param_number =  z[0].__len__()
    count_i = 0
    RangeVariable = []
    while count_i < param_number :
        line1 = b[count_i]
        range = line1.split(':')[1]
        range = inspect.cleandoc(range)
        range1 = range.split(']')
        i = 0
        array_min = []
        array_max = []
        temp_var = tempVar(len(range1)-1)
        while i < len(range1)-1 :
            temp_range = range1[i]
            temp_min = temp_range[ temp_range.find('[')+1 : temp_range.find(';')      ]
            temp_min = float(temp_min)
            array_min.append( temp_min )
            
            temp_max = temp_range[ temp_range.find(';')+1 : temp_range.__len__() ]
            temp_max = float(temp_max)
            array_max.append( temp_max )
            i+=1
        i = 0
        while i < len(array_min) :
            i+=1
        temp_var.array_min = array_min
        temp_var.array_max = array_max
        RangeVariable.append(temp_var)    
        count_i+=1  
    return RangeVariable

class Test(unittest.TestCase):
    pass
def test_generator(*a):
    def test(self):
        self.assertEqual(input.main(*a), 1) 
    return test

if __name__ == "__main__":
    temp = getInputDocs()
    listMinItem = []
    listMaxItem = []
    for lst in temp:
        listMinItem.append(lst.array_min)
        listMaxItem.append(lst.array_max)
    
    for temp in itertools.product(*listMinItem):
        test_name   = 'test_%s' % str(temp)
        test = test_generator(temp)
        setattr(Test, test_name, test) 
    unittest.main()
    
