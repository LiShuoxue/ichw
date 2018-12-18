"""wcount.py: 将一篇文章中的单词按照频率由大到小排序，
并且输出前面的，输出总数由命令行的参数决定。
__author__ = "Shuoxue Li"
__pkuid__  = "1800011839"
__email__  = "1800011839@pku.edu.cn"
"""

import sys
import urllib.request
import urllib.error

def wordsearch(line,punc):
    """将文本中所有的词列入一个列表中。
    """
    if punc==' ':
        return line.split(' ')
    else:
        lst=[]
        for line in line.splitlines():
            lastlist=wordsearch(line,punc[1:])
            for words in lastlist:
                lst.extend(words.split(punc[0]))
        return lst  
    
def stat(line):
    """统计每个词及其出现的数目。
    """
    statdict={}
    punc=""",.?"/()-!_*—[] """
    for x in wordsearch(line,punc):
        statdict[x]=statdict.get(x,0)+1
    if '' in statdict:
        del statdict['']
    return statdict

def wcount(lines,topn=10):
    """打印出初夏频率在前topn位的字母及其出现次数。
    """
    from collections import OrderedDict
    line=lines.lower()
    last=OrderedDict(sorted(stat(line).items(), key=lambda t: t[1]))
    last2=list(dict(last).items())[-topn:][-1::-1]
    for tuples in last2:
        print('%s    %d'%(tuples[0],tuples[1]))
        
if __name__ == '__main__':
    """执行命令行的操作
       对网页所发生错误进行指示。
    """
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        try:
            doc = urllib.request.urlopen(sys.argv[1])
        except urllib.error.URLError as err:
            print('URL错误:{}'.format(str(err)))
        except urllib.error.HTTPError as err:
            print('HTTP错误:{}'.format(str(err)))        
        except Exception as err:
            print('其他错误:{}'.format(str(err)))
        else:
            docstr = doc.read()
            doc.close()
            jstr = docstr.decode()
            if len(sys.argv) == 2:
                wcount(jstr)
            else:
                wcount(jstr,int(sys.argv[2]))
