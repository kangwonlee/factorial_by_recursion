def factorial(n=10):
  if n < 2:
    result = 1
  else:
    result = factorial(n-1) * n
  return result

n = 5
print(f"factorial({n}) =", factorial(n))
