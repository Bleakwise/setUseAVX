# setUseAVX

Adds the expression "bUseAVX = True;" to a valid part of all Build.cs source files.<br />
<br />
Usage:<br />
Replace set SourceDir as the path to your "<...>\UnrealEngine\Engine\Source" directory.<br />
Run.<br />
<br />
Known bugs:<br />
Adds duplicate expressions on consecutive runs. C# allows us to redefine bUseAVX so, we can get away with this, but it's still kind of crude.<br /> Possible Solutoin is to test the whole Build.cs file for the expressoin or conflicting expressions before starting the overwriting process.<br />
<br />
Future Goals:<br />
use a parallel_for as the outer loop<br />
take "<...>\UnrealEngine\Engine\Source" as input from the command line.
