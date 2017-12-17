def format_name(s):
    #return s.title()每个单词首字母大写
    return s[:1].upper() + s[1:].lower()
    #return s.capitalize()#每字符串首字母大写


print(list(map(format_name, ['adam', 'LISA', 'barT'])))#注意py3中需要使用 list()转化map()
#版本库001sssss