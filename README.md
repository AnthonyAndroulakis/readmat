# readmat
[![Build Status](https://travis-ci.org/AnthonyAndroulakis/readmat.svg?branch=master)](https://travis-ci.org/AnthonyAndroulakis/readmat.svg?branch=master)

readmat is a Python package with helpful functions for loading .mat MATLAB files into Python. Most data types are supported.

# Installation:   
```
pip install readmat
```

# Prerequisites:     
python 3    
python modules:     
+ scipy    
+ numpy    
      
# Functions:     
```
load(filename, isNumber=False, isCharArray=False, isStruct=False, isFunction=False, isArray=False, isMatrix=False, isBool=False, isInf=False, isNaN=False, isFunctionHandle=False)
```     
- Example: `matdata1 = readmat.load('matfile1.mat', isCharArray=True)`
- Usage depends on data type. For structs, an example usage is `matdata1.this.is.a.test`. For all other data types, `matdata1`.
- Input: .mat file
- Output: depends on data type
```
mat2obj(filename)
```
- Example: `matdata2 = readmat.mat2obj('matfile2.mat')`
- Example Usage: `matdata2.this.is.a.test`
- Input: .mat file
- Output: object
```
mat2dict(filename)
```
- Example: `matdata3 = readmat.mat2dict('matfile3.mat')`
- Example Usage: `matdata3['this']['is']['a']['test']`
- Input: .mat file
- Output: dictionary
```
options(matobj)
```
- Example: `readmat.options(matdata1)`
- Example: `readmat.options(matdata2)`
- Input: object
- Output: list of options

# How structs are loaded:
The load function loads your MATLAB structure as an object in Python. What does this mean? Basically, the method of exploring the depths of your struct in Python is similar to what you'd do in python. Pretty neat examples below:      

| MATLAB        | Python        |
| :-------------: |:-------------:|
| DWI.dat(1,1,1)      | myMat.DWI.dat[0][0][0] |
| DWI.hdr.private.hdr.test.hello     | myMat.DWI.hdr.private.hdr.test.hello      |
| lesion_jhu.mean | myMat.lesion_jhu.mean      |
| data.grades(101) | myMat.data.grades[100]      |
       
# Known limitations:    
## The following MATLAB data types are not supported:   
+ string arrays (for example: "example" \[notice the pair of double quotes])   
+ datetime   
+ categorical   
+ table    
+ timetable    

# Tips for overcoming/bypassing limitations:
+ convert string arrays to char arrays, command: `char(stringarray)`
+ convert datetime to either a char array or a struct, command: `char(vardatetime)` or `struct(vardatetime)`    
+ convert categorical to double, command: `double(varcategorical)`
+ convert table to cell array, command: `arrayfun(@convertStringsToChars,arrayfun(@string,[vartable.Properties.VariableNames;table2cell(vartable)]),'UniformOutput',false)`
+ convert timetable to cell array, command: `horzcat(vertcat('Time',cellstr(char(vartimetable.Properties.RowTimes))), arrayfun(@convertStringsToChars,arrayfun(@string,[vartimetable.Properties.VariableNames;table2cell(vartimetable)]),'UniformOutput',false))`
       
# Sources cited:
Although I did write part of readmat's code , without the amazing stackoverflow answers from the following stackoverflow users, this project would not have be possible:      
users cs01 and jpapon: https://stackoverflow.com/a/29126361     
user andyvanee: https://stackoverflow.com/a/6573827     
      
# License
This software includes a [MIT license](https://opensource.org/licenses/MIT).
