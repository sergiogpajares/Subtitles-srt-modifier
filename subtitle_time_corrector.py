# -*- coding: utf-8 -*-
#
#  Subtitles_time_corrector.py
#  
#  Copyright 2020 Sergio G. Pajares <sergio.garcia.pajares@alumnos.uva.es>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# ==================================================================== #
# --------------------------- IMPORTS -------------------------------- #
# ==================================================================== #
import os
from math import log10, ceil

# ==================================================================== #
# ------------------------- DEFINITIONS ------------------------------ #
# ==================================================================== #

class time:
    def __init__(self,tiempo):
        '''
        Time constructor
        
        PARAMETERS
            tiempo, str: time in format hh:mm:ss,sss
                         in which hh must be int
                                  mm must be int
                                  ss must be float
        '''
        
        assert isinstance(tiempo,str) , 'tiempo must be an string'
        
        #erase blank space
        while tiempo[0] == ' ':
            tiempo = tiempo[1:]
        
        #Parse
        self.h = int(tiempo[0:2])
        self.m = int(tiempo[3:5])
        self.s = float(tiempo[6:].replace(decimal_separator,'.'))
    
    def __add__(a,b):
        '''
        Sum up two time objects
        '''
        result=time(str(a))
               
        result.s += b.s
        result.m += b.m + result.s // 60
        result.s =  a.s % 60
        result.h += b.h + result.m // 60
        result.m = int(result.m % 60)
        result.h = int(result.h)
        
        return result
    
    def __sub__(a,b):
        '''
        Substract two time objects
        '''
        result=time(str(a))
        
        result.s -= b.s
        result.m -= b.m + a.s // 60
        result.s = a.s % 60
        result.h -= b.h + b.m // 60
        result.m = int(a.m % 60)
        result.h = int(a.h) 
    
    def seconds (self):
        '''
        Returns the time as a float in seconds
        '''
        
        return a.s + a.m*60 + a.h*3600
    
    def seconds_delay(self, delay):
        '''
        Add some delay in seconds to the time
        
        PARAMETERS
            delay, number: amout of seconds to incremet the time 
        '''       
        self.s += delay
        self.m += self.s // 60
        self.s = self.s % 60
        self.h += self.m // 60
        self.h = int(self.h)
        self.m = int(self.m % 60)
        
        return self

    def __str__(self):
        '''
        Prints the time in the input format hh:mm:ss,sss
        '''
        assert self.h <= 99 , 'time to big to be holded'
        string ='{:02d}:{:02d}:{:06.3f}'.format(self.h,self.m,self.s)
        return string.replace('.',decimal_separator)

# ==================================================================== #        
# ------------------------- MAIN DATA -------------------------------- #
# ==================================================================== #
decimal_separator = ','
delay = .5 #seconds
path = '5x04  Doctor Who __ The Time of Angels.en.srt'
new_name = '_modified' #name appended at the end of out file


# ==================================================================== #
# -------------------------- LET'S ROCK ------------------------------ #
# ==================================================================== #
'''
a = time('00:01:58,325')
b = time('00:05:03,000')
print(a)
print(b)
print(a+b)
print(a)
print(b)
print(a.seconds_delay(1))
'''


# -------------------------- FILE NAMING ----------------------------- #
if not os.path.isfile(path) : raise ValueError('The file does not exist')
print('Opening files')


#open input file
i = open(path, 'r')

#open output file
if path[-4] == '.': #case there extension
    extension = path[-4:]
    path = path[:-4]+new_name+extension
    
    #check if the file already exists
    if os.path.isfile(path):
        print('file <{}> already exist'.format(path))
        counter=1
        path = path[:-4]+str(counter)+extension
        while os.path.isfile(path):
            counter += 1
            digits = ceil(log10(counter))
            print('file <{}> already exist'.format(path))
            path = path[:-(digits+4)]+str(counter)+extension
            
else:# case there no extension
    path = path + new_name

    #check if the file already exists
    if os.path.isfile(path):
        print('file <{}> already exist'.format(path))
        counter=1
        path = path[:-1]+str(counter)+extension
        while os.path.isfile(path):
            counter += 1
            digits = ceil(log10(counter))
            print('file <{}> already exist'.format(path))
            path = path[:-digits]+str(counter)+extension


o = open(path , 'w')

# ------------------------ FILE PROCESING ---------------------------- #
line = i.readline()
print('Reading has started. Your file is being converted.')
while line != '':
    #number line
    o.write(line)
    
    #time line
    line = i.readline()
    t1=time(line[:12])
    t2=time(line[16:])
    t1.seconds_delay(delay)
    t2.seconds_delay(delay)
    o.write('{} --> {}\n'.format(t1,t2))
    
    #text line
    line = i.readline()
    while not (line == '\n' or line=='')  :
        o.write(line)
        line=i.readline()
    o.write(line)
    line = i.readline()

print('Conversion has finished. Closing your files')
i.close()
o.close()
