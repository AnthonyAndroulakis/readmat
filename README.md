# mattools
Helpful functions for loading .mat Matlab files into Python. Most data types are supported.       
       
# Prerequisites:     
python3    
python modules:     
+ scipy    
+ numpy    
+ itertools    
      
# Functions:     
+ `load(filename, isNumber=False, isCharArray=False, isStruct=False, isFunction=False, isArray=False, isMatrix=False, isBool=False, isInf=False, isNaN=False, isFunctionHandle=False)`     
+ `mat2obj(filename)`     
+ `mat2dict(filename)`    
+ `options(matobj)`    
       
# Known limitations:    
## The following Matlab data types are not supported:   
+ string arrays (for example: "example" \[notice the pair of double quotes])   
+ datetime   
+ categorical   
+ table    
+ timetable    

# Extras:
All the necessary instructions are covered in this README document. However, if you'd like examples and/or extra explanations, look at the comments at the top of mattools.py.
