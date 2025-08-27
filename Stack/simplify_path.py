'''
Leetcode # 71. Simplify Path


You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

    A single period '.' represents the current directory.
    A double period '..' represents the previous/parent directory.
    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:

    The path must start with a single slash '/'.
    Directories within the path must be separated by exactly one slash '/'.
    The path must not end with a slash '/', unless it is the root directory.
    The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.

Return the simplified canonical path.
'''

def simplifyPath(path):
    stack = []
    cur = ""                    # current file path we are looking at      
    for c in path + "/":        # Go through every char in the input path + the trailing slash
        if c == "/":            # if the char = a slash
            if cur == "..":     # Special case!
                if stack:       # Pop our stack if its none empty
                    stack.pop()
            elif cur != "" and cur != ".": # Other special cases. If its not empty and if curr is not a . operator
                stack.append(cur)          # Add to our stack
            cur = ""            # once we are done, reset
        else:                   # If its any other char, simply add it to the curr file we are looking.
            cur += c 
    # Note: We are either adding a file to our stack or we are removing a file from the stack
    
    # Our stack will look like stack = ["abc", "def"],
    # Start/Begin our result string with a / and join the strings together and place / between them
    return "/" + "/".join(stack)  # Now stack = /abc/def 

# Test cases here: 
path = "/a//b/../...///c/./d/"

result = simplifyPath(path)
print(result)