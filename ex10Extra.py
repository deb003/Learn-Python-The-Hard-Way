count = 0
while True:
    for i in ["/","-","|","\\","|",5]:
        print "%s" % i,
    count += 1
    if count > 8:
        break
#If you want to understand it more, remove the \r in print statement.
