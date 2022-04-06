def sum_to (n):
  total = 0
  for num in range(1, n+1):
    total += num
  return total
print(sum_to(6))
print(sum_to(10))


def largest_num (nums):
  largest_number = 0
  for num in nums:
    if num > largest_number:
      largest_number = num
  return largest_number
print(largest_num([1, 2, 3, 4, 0]))
print(largest_num([10, 4, 2, 231, 91, 54]))


def occurrences (a,b):
  return a.count(b)
print(occurrences("fleep floop", 'o'))
print(occurrences("fleep floop", 'p'))
print(occurrences("fleep floop", 'e'))
print(occurrences("fleep floop", 'fl'))


def product(*args):
  total = 1
  for arg in args:
    total *= arg
  return total
print(product(-1, 4))    
print(product(2, 5, 5))    
print(product(4, 0.5, 5))    
