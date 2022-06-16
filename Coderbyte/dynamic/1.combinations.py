
def combinations(elements):
   if len(elements) == 0: return [[]]
   
   firstElement = elements[0]
   rest = elements[1:]
   
   combsWithoutFirst = combinations(rest)
   combsWithFirst = []
   
   for item in combsWithoutFirst:
      combsWithFirst.append([*item, firstElement])

   combsWithFirst.extend(combsWithoutFirst)
   return combsWithFirst

print(combinations(['a','b','c']))

# key things to take away
# 1. Given a number n, there is a 2^n number of possible combinations
# 2. We can generate a binary tree to represent the recursion process needed to generate those combinations
#    Tree will start with an empty array item as a root and has the item not included in the left branch and has it included in the right branch