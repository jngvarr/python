t='23*x^5'
print(int(t[:t.find('*')])) # 23 до знака *
print(int(t[t.find('^') + 1:])) # после знака ^