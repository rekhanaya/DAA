# Longest Common Prefix
def longestCommonPrefix(a):
  size = len(a)

  if (size == 0):
    return ""

  if (size == 1):
    return a[0]

  a.sort()

  end = min(len(a[0]), len(a[size - 1]))

  i = 0
  while (i < end and a[0][i] == a[size - 1][i]):
    i += 1

  pre = a[0][0:i]
  return pre

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
result = longestCommonPrefix(arr)
print(result)

arr = ["apple", "ape", "april"]
result = longestCommonPrefix(arr)
print(result)
