#!/usr/bin/env python
# coding: utf-8

# In[1]:


pc1 = [56, 48, 40, 32, 24, 16,  8,
0, 57, 49, 41, 33, 25, 17,
9,  1, 58, 50, 42, 34, 26,
18, 10,  2, 59, 51, 43, 35,
62, 54, 46, 38, 30, 22, 14,
6, 61, 53, 45, 37, 29, 21,
13,  5, 60, 52, 44, 36, 28,
20, 12,  4, 27, 19, 11,  3
]

pc2 = [
13, 16, 10, 23,  0,  4,
2, 27, 14,  5, 20,  9,
22, 18, 11,  3, 25,  7,
15,  6, 26, 19, 12,  1,
40, 51, 30, 36, 46, 54,
29, 39, 50, 44, 32, 47,
43, 48, 38, 55, 33, 52,
45, 41, 49, 35, 28, 31
]


def permutate(table, block):
    return "".join(list(map(lambda x: block[x], table)))
    
block = "1101001001101011001000110101010101110110010011101011101010001101"

resBlock = permutate(pc1, block)


L = resBlock[:28]
R = resBlock[28:]

print("C0", L)
print("D0", R)


# In[2]:


L = list(L)
R = list(R)


# In[11]:


left_rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

Kn = [ [0] * 48 ] * 16

i = 0
while i < 16:
    j = 0
    while j < left_rotations[i]:
        L.append(L[0])
        del L[0]
        R.append(R[0])
        del R[0]
        j += 1

    print("=================================================================")
    print("C", i+1,"===>",  "".join(L))
    print("D", i+1, "===>", "".join(R))
    
    Kn[i] = permutate(pc2, L + R)
    
    print("k",i+1,"===>", Kn[i])
    i += 1

L = list(L)
R = list(R)


# In[ ]:





# %%
