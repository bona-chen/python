sth = "上海自来水来自海上"
print(sth.count("海"))
print(sth.count("海", 0, 5))
print(sth.index("上"))
print(sth.rindex("上"))
code = """
        print("I'm Bona")
    print("Who are you")"""
print(code)
new_code = code.expandtabs(4)
print(new_code)
print("你是我爸爸".replace("爸爸", "儿子"))
table = str.maketrans("ARCADE", "123456789")
print(table)
x = "KJDUHGKJLHFIOUYKJHXKJH*IOEYKLSH:KLISH(I*OEFILSFUHjakdghfjkasgfiujkdfbkasduf"
print(x.translate(table))
