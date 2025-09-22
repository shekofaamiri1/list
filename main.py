l= ["reza", "neda", "sahel","ali",""]
i=0
while i < len(l):
    s = l[i]
    j=0
     while j < len(s):
          if j % 2 ==0:
            print(s[j].upper(), end="")