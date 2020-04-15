try:
    foo = open(
        "Day 4\\ErrorHandling\\foo.txt")
except Exception as e:
    print(str(e))
else:
    print(foo.read())
finally:
    print("finished")
