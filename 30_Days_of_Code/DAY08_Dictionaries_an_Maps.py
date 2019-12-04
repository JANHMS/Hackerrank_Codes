n=int(input())
numbers=[input().split() for _ in range(n)]
phone_book={k:v for k,v in numbers}
while True:
    try:
        name=input()
        if name in phone_book:
            print("{}={}".format(name,phone_book[name]))
        else:
            print("Not found")
    except:
        break
