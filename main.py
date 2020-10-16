def factorial(n=10):

  print(f"factorial({n})")

  if n < 2:
    print(f"n = {n} < 2")
    result = 1
  else:
    print(f"n = {n} >= 2")
    result = factorial(n-1) * n
  print("result =", result)
  return result

n = 5
print(f"factorial({n}) =", factorial(n))
