"""currency.py: 返回浮点类型的货币变换结果

__author__ = "Shuoxue Li"
__pkuid__  = "1800011839"
__email__  = "1800011839@pku.edu.cn"
"""
def before_space(s):
    """返回第一个空格之前的字符串片段。
    """
    return s.split(' ')[0]

def after_space(s):
    """返回第一个空格之后的字符串片段且不含空格。
    """
    return s[len(before_space(s))+1:]

def first_inside_quotes(s):
    """返回第一对双引号之间的字符串片段，不含引号。
    """
    num1=s.index('"')
    num2=s[num1+1:].index('"')
    return s[num1+1:num1+num2+1]

def get_from(s):
    """返回json中"from" : 之后引号之中的内容。
    """
    str1='"from" : '
    return first_inside_quotes(s[str.find(s,str1)+len(str1):])
    
    
def get_to(s):
    """返回json中"to" : 之后引号之中的内容。
    """
    str1='"to" : '
    return first_inside_quotes(s[str.find(s,str1)+len(str1):])

def has_error(s):
    """若json中"success" : 之后为true，则返回False；反之返回True。
    """
    str1='"success" : '
    str2=s[str.find(s,str1)+len(str1):]
    crit=eval(str2[0:str.find(str2,',')].capitalize())
    return not crit

def currency_response(currency_from, currency_to, amount_from):
    """返回输入货币种类与数量得到的json字符串。
    """
    from urllib.request import urlopen

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%f'\
                  %(currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    json=docstr.decode('ascii')   
    return json

def iscurrency(currency):
    """若输入币种非规范或错误，则返回False."""
    str=currency_response(currency,'CNY',1.0)
    return not has_error(str)

def exchange(currency_from, currency_to, amount_from):
    """返回货币的兑换值。且为浮点数。"""
    return float(before_space(get_to(currency_response(\
           currency_from, currency_to, amount_from))))


"""以下代码用于测试。
"""
def test_before_space():
    assert '2'==before_space('2 Chinese Yuan')
    assert 'Cho'==before_space('Cho nguoi')
    assert '?"'==before_space('?" "!')
    
def test_after_space():
    assert 'Chinese Yuan'==after_space('2 Chinese Yuan')
    assert 'DAFH'==after_space('Using DAFH')
    assert '  say loi '==after_space('khong   say loi ')

def testA():
    test_before_space()
    test_after_space()
    
def test_first_inside_quotes():
    assert 'B C'==first_inside_quotes('A "B C"')
    assert 'B C'==first_inside_quotes('A "B C","d e"')
    assert not '"B C"'==first_inside_quotes('A "B C"C"')
    
def test_get_from():
    assert 'done'==get_from('"from" : "done"')
    assert ''==get_from('body,"from" : """D"""')
    assert not '"2 Chinese Yuan"'==get_from('"from" : "2 Chinese Yuan"')
    
def test_get_to():
    assert 'done'==get_to('"to" : "done"')
    assert ''==get_to('body,"to" : """D"""')
    assert not '"2 Chinese Yuan"'==get_to('"to" : "2 Chinese Yuan"') 
    
def test_has_error():
    assert False==has_error('"success" : true, "error" : "" ')
    assert True==has_error('"success" : False, "error" : "" ')
    assert not True==has_error\
    ('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros",\
    "success" : true, "error" : "" }')

def testB(): 
    test_first_inside_quotes()
    test_get_from()  
    test_get_to()
    test_has_error()
    
def testC():
    assert currency_response('USD','EUR',2.5)==\
    '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'
    assert currency_response('YMMD','EUR',2.5)==\
    '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    assert currency_response('CNY','VND',1.0)==\
    '{ "from" : "1 Chinese Yuan", "to" : "3373.6019135739 Vietnamese Dong", "success" : true, "error" : "" }'
    
def test_iscurrency():
    assert True==iscurrency('EUR')
    assert False==iscurrency('YMMD')
    assert False==iscurrency(3)

def test_exchange():
    assert exchange('USD','CNY',1)==6.8521
    assert exchange('CNY','VND',1)==3373.6019135739
    assert not exchange('USD','CNY',1)==6.8520

def testD():
    test_iscurrency()
    test_exchange()
    
def testAll():
    testA()
    testB()
    testC()
    testD()

def main():
    a=input('currency_from:')
    b=input('currency_to:')
    c=float(input('amount_from:'))
    print(exchange(a,b,c))
    testAll()
    
if __name__ == '__main__':
    main()
