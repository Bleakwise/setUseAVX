##5. setUseAVX
setUseAVX is a simple script that adds the expression "bUseAVX = True;" to a valid part of all Build.cs source files. AVX support was added in Unreal Engine 4.9 on a per-module basis.
    New: AVX support can now be enabled on a per-module basis by settings bUseAVX = true in a module's .Build.cs rules file.
As of 4.11 the release branch of UE4 has over 400 Build.cs files, making it quite tedious to add bUseAVX = True; to every single one. The aim of this script is to parse Build.cs files, and if the appropriate code-block is present it adds the aformentioned expressoin on a new line.
  

###1. Usage:
  1. Replace set SourceDir as the path to your "<...>\UnrealEngine\Engine\Source" directory.
  2. Run.

###2. Future Goals:<br />
  1. Parallelize the outer loop.
  2. Take "<...>\UnrealEngine\Engine\Source" as input from the command line.

###3. Known bugs:
  1. Adds duplicate **_bUseAVX = True;_** expressions on consecutive runs. C# allows us to redefine bUseAVX so, we can get away with this, but it's still kind of crude.
    1. Solutoin: Test the whole Build.cs file for the expressoin or conflicting expressions before starting the overwriting process.
  2. Because of the logic involved, there is an issue writing to the correct locatoin if using non-conforming (UE4 uses something like Allman style) indent style, such as those that place the opening brace **_{_** on the same line as the class constructor's signature, ie: *_public AITestSuite(TargetInfo Target){_*
    1. Solution: Use pattern matching to test for an opening brace on the same line as the constructor signature 

###4. The MIT License (MIT)
>
>Copyright (c) 2016 Russell Barlow III
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
>of this software and associated documentation files (the "Software"), to deal
>in the Software without restriction, including without limitation the rights
>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
>copies of the Software, and to permit persons to whom the Software is
>furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
>copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
>SOFTWARE.
