from urllib.request import urlopen

def exchange(currency_from, currency_to, amount_from):
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%f'%\
                  (currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return float(jstr.split('"')[7].split()[0])
    
exchange(input('currency_from:'),\
        input('currency_to:'),\
         float(input('amount_from:')))