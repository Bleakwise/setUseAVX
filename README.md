### What is setUseAVX and why was it made?
setUseAVX is a simple script that adds the expression **_bUseAVX = True;_** to the class constructors of all Build.cs source files. This script was written because enabling AVX in all Build.cs files one by one by hand is a very tedious process, and even more tedious to carry out every time Epic pushes a new release. 

Unreal Engine 4 has had the optoin to target AVX instructions as of Unreal Engine 4.9. AVX hardware support has been included in AMD and Intel desktop products since the releases of Bulldozer and Sandy Bridge respectfully.

For more on AVX itself and why you would want to use it:<br />
https://software.intel.com/en-us/articles/introduction-to-intel-advanced-vector-extensions

For more about what was added in 4.9:<br />
https://www.unrealengine.com/blog/unreal-engine-49-released
>New: AVX support can now be enabled on a per-module basis by settings bUseAVX = true in a module's .Build.cs rules file.
  

### Usage:
  1. Replace set SourceDir as the path to your "<...>\UnrealEngine\Engine\Source" directory.
  2. Run.

### Future Goals:<br />
  1. Parallelize the outer loop.
  2. Take "<...>\UnrealEngine\Engine\Source" as input from the command line.

### Known bugs:
  1. Adds duplicate **_bUseAVX = True;_** expressions on consecutive runs. C# allows us to redefine bUseAVX an almost unlimited number of times, so, we can get away with this, but I don't see this passing as a feature so it needs to be fixed.
    1. Solutoin: Test the whole Build.cs file for the expressoin or conflicting expressions before starting the overwriting process.
  2. There is an issue writing to the correct locatoin if using non-conforming (UE4 uses something like Allman style) indent style such as those that place the opening brace on the same line as the class constructor's signature like so: <br /> **_public AITestSuite(TargetInfo Target){_**
    1. Solution: Use pattern matching to test for an opening brace on the same line as the constructor signature 

### Advisory:
I released this script because I found it useful for my personal needs but user disgression is advised.

### The MIT License (MIT)
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
