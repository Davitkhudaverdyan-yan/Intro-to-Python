a = [1, 4, 5, 7, 8, -2, 0, -1]
print(a[3],a[5])


print(a)
a.sort(reverse = True)
print("a_sorted=",a)

a_sorted = a.sort(reverse = True) 
print(a[1:3])
print(a[2:6])

a_sorted= [-2, -1, 0, 1, 4, 5, 7, 8]
del a_sorted[2:4]
print(a_sorted)

b = ["grapes", "Potatoes", "tomatoes","Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted = sorted(b)
print(b_sorted)

c = list(a[1:4] + b[4:7])
print(c)