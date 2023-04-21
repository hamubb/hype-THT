```python
class Solution:
       def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted())
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

```
In line 1 it is not necessary to use classes since we will not be reusing this code. A simple function will do. For writing beautiful
software in python please refer to the Zen of Python which you can access via typing `import this` when in the python interpretor. Sometimes
> simple is better than complex

On line number 2 please try to stick to the python coding style guide which is enforced by P.E.P.8. Function/method names 
should be in lower_case with _ in between like : ```def group_anagrams(strs)``` Please refer to [PEP8](https://peps.python.org/pep-0008/)
for writing beautiful software with python.

On line 4, when naming loop variables inside a for loop please try to use words that are more understandable to us humans. The more understandable
they are the eaiser they will be to use. I suggest using singular nouns  for the loop variable and plurals for the iterable/sequence. Please 
note this does not affect how your programm will run but will help someone who is reading your code. As Guido Van Rossum, the creator of Python,
has noted:

> Code is read more often than it is written. 

Code should always be written in a way that promotes readability.  Also on the same line please take a look at your indentation. The python 
interpretor will be :angry: and will scream at you when you mess up the indentation. As a rule of thumb please note that whenenver we have a ":" (colon) the next line
should be indented with 4 spaces to mark the function or class  block.

On line number 5: `x = "".join(sorted())` you declared a loop variable which you never used. Sorted expects you to pass an argument which you never did. For help 
with python builtin functions please type `help(sorted)` when in the python repl so you can see what sorted expects you to pass to it.

Overally, your code will run if you fix :hammer_and_wrench: the problems that I have highlighted above. Also, please refer to the PEP8 document or even keep
one under your pillow so that fellow python programmers who read your code will not cry. :smile:
