try:
  i=int(input("Enter Number: "))
except ValueError:
  print("Enter Integer type data")
while i>1:
  def coltaz(n):
    if n%2==0:
      n=n//2
      print(n)
      return(n)
    else:
      n=3 * n + 1
      print(n)
      return(n)
  i=coltaz(i)