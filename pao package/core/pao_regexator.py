# REGEXATOR by louispuyo

# REGEX MODELS
regexDotPoint = r"\<\$|^;.*;" #1 
regexDotPointDollarB2E = r"\<\$|^;.*;|\/>" #2
regexBracketStoFunction = r"\$\d.*}" #3
regexHashStoNumber = r"#.\d+" #4
RegexAtsto = r"@.*\(" #5
REgexAtStoAndArg = r"@.*\)" #6
regexbaliseHTM = r"<[^<>]+>"
ParsingUrl = r"^(((https?|ftp):\/\/)?([\w\-\.])+(\.)([\w]){2,4}([\w\/+=%&_\.~?\-]*))*$"
#1=> ; content... ;
#2=> <$ ;content...; />
#3=> $<int>{$name: function} ---> example: $1{'myFunction': GetStarted} ----> [STO[#1: lambda x: x+1]]
#4=> sto(#(10)) ---> to stock a value at the adress 10 of your redis server [session] or docker server
#5=> @sto(   |limite|  [...])
#6=> @sto(mycontainer)
PaoMustache = {'<$':lambda x: x+1, '/>': lambda x: x-1}

'''
    1 - allow lambda function 
    2 - allow normal function
'''
# SIMPLE REGEX
startWithDollar = r'^\$'
negationOperator = r'!{...}'
rdSuffix = r'(?<=r)d'

class cursor_reg():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.coord = (start, end)
        self.slice = (end-start)
    
    def decode(self, string):
        cache = {}
        for i in range(len(string)-1):
            cache += string[i]
            if CheckMatchingCode(cache, '.*'):
                return Interpretor(cache) 
    
    def Interpretor(self, key: str) -> callable:
        ''' Interpretor str -> <fun> '''
        return PaoMustache[f'{key}']


# TODO -> make the other regex #
result_deb = cursor_reg(0,1).Interpretor('<$')(1)
result_fin = cursor_reg(0,1).Interpretor('/>')(1)
print(result_deb, result_fin)



