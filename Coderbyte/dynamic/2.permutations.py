# What is a permutation.
# A collection of things where the order matters
# In a permutation, all elements in a list are included and it is the matter of in which order they are placed.

# Given a set of N things, there are n! permutations

def permutations(elements):
   if len(elements) == 0: return [[]]
   
   firstElement = elements[0]
   rest = elements[1:]
   
   permsWithoutFirst = permutations(rest)
   perms = []
   
   for perm in permsWithoutFirst:
      for i in range(0, len(perm)+1):
         if i < len(perm):
            final = [*perm[:i], firstElement, *perm[i:]]
            
         elif i == len(perm):
            final = [*perm, firstElement]
            
         perms.append(final)
   
   return perms

print(permutations(["a", "b", "c"]))