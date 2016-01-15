# The MIT License (MIT)
# 
# Copyright (c) 2016 Russell Barlow III
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from __future__ import print_function
from __future__ import division
import os

SourceDir = "D:\Users\Russell\Documents\Unreal Projects\UnrealEngine\Engine\Source"
buildFilesList=[]

def buildBuildFileList(SourceDir):
    for root, dirs, files in os.walk(SourceDir):
        for buildFile in files:
            if 'Build.cs' in buildFile:
                buildFilesList.append(os.path.join(root, buildFile))
            
    return buildFilesList

def editBuildFile(file_name):
    seek_target = "TargetInfo"
    file_object = open(file_name, "rt+")
    file_buffer = file_object.readlines()
    
    
    for i in range(len(file_buffer)):
        if seek_target in file_buffer[i]:
            for j in range(len(file_buffer)):
                if '{' in file_buffer[i+j]:
                    file_buffer.insert(i+j+1, "\t\t\tbUseAVX = true;\n")
                    file_object.seek(0)
                    file_object.writelines(file_buffer)
                    file_object.truncate()
                    file_object.close()
                    return file_buffer
    file_object.close()
        
    return file_buffer

def editBuildFileList(SourceDir):
    buildFilesList = buildBuildFileList(SourceDir)
    
    for file_index in range(len(buildFilesList)):
        editBuildFile( buildFilesList[file_index] )
        
editBuildFileList(SourceDir)