#!/usr/bin/env python
# coding: utf-8

# In[20]:


def Input_Output(s):
    
    replacements = { 
                "A" : "@",
                "a" : "@",
                "e" : "3",
                "i" : "1",
                "o" : "0",
                "u" : "v",
                "c" : "(",
                "s" : "$"
               }
   
    with open("Input.txt", "r") as file_obj:
        lines = file_obj.read()
        for letter in lines:
            if letter in replacements.keys():
                lines = lines.replace(letter, replacements[letter])
    with open("OutReplace.txt", "w") as file_obj:
        file_obj.write(lines)
                  
    print(lines, end = "")

s = "Input.txt"   
Input_Output(s)    


# In[17]:


with open("OutReplace.txt", "r") as f6:
    text = f6.read()
    print(text)


# In[ ]:




