#put together some other's functions/classes and wrote some functions myself, Anthony Androulakis, 2019 
#readmat.py, wrote some functions, found 1 function & 1 class on stackoverflow, read below for sources
#How to run:
#import readmat
#readmat.load(filename, isNumber=False, isCharArray=False, isStruct=False, isFunction=False, isArray=False, isMatrix=False, isBool=False, isInf=False, isNaN=False, isFunctionHandle=False) #set one of the variable types to True
#
#How to convert mat to dictionary:
#readmat.mat2dict('filename')
#
#
# function loadmat is from stackoverflow, written by users cs01 and jpapon:
# https://stackoverflow.com/a/29126361
#
# class Struct is from stackoverflow, written by user andyvanee
# https://stackoverflow.com/a/6573827
#
# I've written function load to.
# I've also written function option so you can see which options/paths your object has. Example run: options(myMat.DWI.hdr)
# Output of function option will be a list of your options. Example: ['fname', 'dim', 'dt', 'pinfo', 'mat', 'n', 'descrip', 'private']
#
#
#The following MATLAB data types are not supported:
# string arrays
# datetime
# categorical
# table
# timetable
#
#
#What's a string array in MATLAB? (notice the pair of double quotes below)
# "example"
#What's a char array in MATLAB? (notice the pair of single quotes below)
# 'example'
#How to I convert from a string array to char array in MATLAB?
# convertStringsToChars("example")
#
#
#Functions:
# load(filename, isNumber=False, isCharArray=False, isStruct=False, isFunction=False, isArray=False, isMatrix=False, isBool=False, isInf=False, isNaN=False, isFunctionHandle=False)
# mat2obj(filename)
# mat2dict(filename)
# options(matobj)

import scipy.io as spio
import scipy.io
import numpy as np
import itertools

class Struct: #this class was written by user andyvanee (https://stackoverflow.com/a/6573827)
  '''The recursive class for building and representing objects with.'''
  def __init__(self, obj):
    for k, v in obj.items():
      if isinstance(v, dict):
        setattr(self, k, Struct(v))
      else:
        setattr(self, k, v)
  def __getitem__(self, val):
    return self.__dict__[val]
  def __repr__(self):
    return '{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for
      (k, v) in self.__dict__.items()))

def loadmat(filename): #this function was written by users cs01 and jpapon (https://stackoverflow.com/a/29126361)
    '''
    this function should be called instead of direct spio.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    '''
    def _check_keys(d):
        '''
        checks if entries in dictionary are mat-objects. If yes
        todict is called to change them to nested dictionaries
        '''
        for key in d:
            if isinstance(d[key], spio.matlab.mio5_params.mat_struct):
                d[key] = _todict(d[key])
        return d

    def _todict(matobj):
        '''
        A recursive function which constructs from matobjects nested dictionaries
        '''
        d = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, spio.matlab.mio5_params.mat_struct):
                d[strg] = _todict(elem)
            elif isinstance(elem, np.ndarray):
                d[strg] = _tolist(elem)
            else:
                d[strg] = elem
        return d

    def _tolist(ndarray):
        '''
        A recursive function which constructs lists from cellarrays
        (which are loaded as numpy ndarrays), recursing into the elements
        if they contain matobjects.
        '''
        elem_list = []
        for sub_elem in ndarray:
            if isinstance(sub_elem, spio.matlab.mio5_params.mat_struct):
                elem_list.append(_todict(sub_elem))
            elif isinstance(sub_elem, np.ndarray):
                elem_list.append(_tolist(sub_elem))
            else:
                elem_list.append(sub_elem)
        return elem_list
    data = scipy.io.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)


def mat2dict(filename): #I wrote this, runs function loadmat
    if filename[-4:]=='.mat':
      loadoutput=loadmat(filename)
      return loadoutput
    else:
      print('Only .mat files are accepted.')

def mat2obj(filename): #combines function loadmat and class Struct, I wrote this
    if filename[-4:]=='.mat':
      loadoutput=loadmat(filename)
      structoutput=Struct(loadoutput)
      return structoutput
    else:
      print('Only .mat files are accepted.')

#I wrote the following function load. If you do not know if a mat file has a number, Inf, or Nan, just choose isNumber=True. FYI: Inf is float('inf') in Python. NaN is float('nan') in Python.
def load(filename, isNumber=False, isCharArray=False, isStruct=False, isFunction=False, isArray=False, isMatrix=False, isBool=False, isInf=False, isNaN=False, isFunctionHandle=False): #data type string arrays, datetime, categorical, table, and timetable are not supported
    if filename[-4:]=='.mat':
      if not any([isNumber,isCharArray,isStruct,isFunction,isArray,isMatrix,isBool,isInf,isNaN,isFunctionHandle]):
          print('Error: variable type not indicated in input.')
      elif not all(isinstance(x, bool) for x in [isNumber,isCharArray,isStruct,isFunction,isArray,isMatrix,isBool,isInf,isNaN,isFunctionHandle]):
          print('Only boolean values (True or False) are accepted for indicating variable type.')
      elif len(list(itertools.islice(filter(None, [isNumber,isCharArray,isStruct,isFunction,isArray,isMatrix,isBool,isInf,isNaN,isFunctionHandle]), 2))) == 1:
          if isNumber or isCharArray or isInf or isNaN:
              loadoutput=loadmat(filename)
              structoutput=Struct(loadoutput)
              try:
                  return eval("structoutput."+options(structoutput)[0])
              except:
                  print('Incorrect input format.')
              
          if isStruct:
              try:
                  structoutput=mat2obj(filename)
                  return structoutput
              except:
                  print('Incorrect input format.')
              
          if isFunction:
              loadoutput=loadmat(filename)
              structoutput=Struct(loadoutput)
              try:
                  return eval("structoutput."+options(structoutput)[0]).function
              except:
                  print('Incorrect input format.')

          if isArray or isMatrix:
              loadoutput=loadmat(filename)
              structoutput=Struct(loadoutput)
              try:
                  if isinstance(eval("structoutput."+options(structoutput)[0]),np.ndarray):
                      return eval("structoutput."+options(structoutput)[0]).tolist()
              except:
                  print('Incorrect input format.')
                
          if isBool:
              loadoutput=loadmat(filename)
              structoutput=Struct(loadoutput)
              try:
                if eval("structoutput."+options(structoutput)[0])==1:
                    return True
                if eval("structoutput."+options(structoutput)[0])==0:
                    return False
              except:
                print('Incorrect input format.')
                
          if isFunctionHandle:
              loadoutput=loadmat(filename)
              structoutput=Struct(loadoutput)
              try:
                return "@"+eval("structoutput."+options(structoutput)[0]+".tolist().__dict__['function_handle'].__dict__['function']")
              except:
                print('Incorrect input format.')
      else:
          print('Error: multiple variable types selected. Only 1 variable type can be indicated in input.')
    else:
      print('Only .mat files are accepted.')

def options(matobj): #find options of object, input is your object of type <class 'readmat.Struct'>, I wrote this
    try:
        dictmatobj=dict(zip(matobj.__dict__, map(str, matobj.__dict__.values())))
        return list(eval('{key: value for key, value in '+str(dictmatobj)+".items()"+' if not key.startswith("__") and not key.startswith("_")}.keys()'))
    except:
        print("Incorrect type. Correct input is an object of type <class 'readmat.Struct'>. In other words, a MATLAB struct that's been loaded into Python through the readmat.load function.")
