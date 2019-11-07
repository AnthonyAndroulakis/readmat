# mattools
Helpful functions for loading .mat Matlab files into Python. Most data types are supported.       
       
# Prerequisites:     
python3    
python modules:     
+ scipy    
+ numpy    
+ itertools    
      
# Functions:     
1) `load(filename, isNumber=False, isCharArray=False, isStruct=False, isFunction=False, isArray=False, isMatrix=False, isBool=False, isInf=False, isNaN=False, isFunctionHandle=False)`     
2) `mat2obj(filename)`     
3) `mat2dict(filename)`    
4) `options(matobj)`    

# How structs are loaded:
The load function loads your matlab structure as an object in Python. What does this mean? Basically, the method of exploring the depths of your struct in Python is similar to what you'd do in python. Pretty neat examples below:      

| MATLAB        | Python        |
| ------------- |:-------------:|
| DWI.dat(1,1,1)      | myMat.DWI.dat[0][0][0] |
| DWI.hdr.private.hdr     | myMat.DWI.hdr.private.hdr      |
| lesion_jhu.mean | myMat.lesion_jhu.mean      |
| data.grades(101) | myMat.data.grades[100]      |
       
# Known limitations:    
## The following Matlab data types are not supported:   
+ string arrays (for example: "example" \[notice the pair of double quotes])   
+ datetime   
+ categorical   
+ table    
+ timetable    

# Extras:
All the necessary instructions are covered in this README document. However, if you'd like examples and/or extra explanations, look at the comments at the top of mattools.py.
