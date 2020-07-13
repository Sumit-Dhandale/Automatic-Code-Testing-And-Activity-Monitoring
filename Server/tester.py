import os
import sys
import subprocess
import index

####   function for comparing output   #### 
def getdata(filename):
    file,data=open(filename,'r'),[]
    try:
        for line in file:
            if(len(line.rstrip())>0):
               data.append(line.rstrip())
    finally:
               file.close()
    return data



####  function for identifying language    ####
def identify_language(filename):
    global file
    global language
    file,language=filename.split(".")




####    function to run external program  ####
def runcode():
    if language=='py':
        print("python program running")
        f1=open('input.txt','r')
        #subprocess.Popen('cmd.exe /k a.py')
        with open('outputforcheck.txt','w') as f:
            p=subprocess.run('assignment.py',shell=True,stdin=f1,stdout=f,text=True)
        f=open('outputforcheck.txt','r')
        s=f.read()
        if getdata('outputforcheck.txt')==getdata('test.txt'):
            print('First testcase is passed succcessfully')
            return 1;
        return 0;
        
    if language=='c':
        print("c program running")
    if language=='cpp':
        print("cpp program running")
    if language=='java':
        print("java program running")



def main(filename):
    identify_language(filename)
    print(file)
    print(language)
    return runcode()
