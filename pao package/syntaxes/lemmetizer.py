#! python 
# lemmetizer.py \
import tokenize 
import re

# ANCHOR TOKENIZER
class tokenizing(object):
    def __init__(self, token, regex):
        super(tokenizing).__init__(token, regex)
    

    def __init_subclass__(cls):
        return super().__init_subclass__()

class Lemmetizer(object):
    def __init__(self, /):
        pass

class Manager(tokenizing, Lemmetizer):
    ''' 
    class RepositoryType(Enum):
        HG = auto()
        GIT = auto()
        SVN = auto()
        PERFORCE = auto()

    class Repository():
        _registry = {t: {} for t in RepositoryType}

        def __init_subclass__(cls, scm_type=None, name=None, **kwargs):
            super().__init_subclass__(**kwargs)
            if scm_type is not None:
                cls._registry[scm_type][name] = cls

    class MainHgRepository(Repository, scm_type=RepositoryType.HG, name='main'):
        pass

    class GenericGitRepository(Repository, scm_type=RepositoryType.GIT):
        pass


    '''

    def __init__(self, /, token: str = None):
        self.token = token

    def start(self, /):
        '''
        >>> # explication and motivation below

        >>> class QuestBase:
        ...    # this is implicitly a @classmethod (see below for motivation)
        ...    def __init_subclass__(cls, swallow, **kwargs):
        ...        cls.swallow = swallow
        ...        super().__init_subclass__(**kwargs)

        >>> class Quest(QuestBase, swallow="african"):
        ...    pass

        >>> Quest.swallow
        'african'
        
        '''
        return 'ci'



class AnalyseTheCode(Lemmetizer):
    def __init_subclass__(cls):
        return super(Lemmetizer).__init_subclass__()

    def __format__(self, format_spec):
        return super().__format__(format_spec)

    def __reduce_ex__(self, protocol):
        return super().__reduce_ex__(protocol)

    def __repr__(self, name):
        self.name = name
        return super(Lemmetizer).__repr__()


string = AnalyseTheCode().__repr__('louis')
print(string)

        
import re
 
str = 'There are 10,000 to 20000 students in the college. This can mean anything.\n'
 
pat = r'are{1,}\s[a-z0-9,\s]+'
 
match = re.search(pat, str)
matches = re.findall(pat, str)
 
if match is None:
    print('Pattern not found')
else:
    print('Pattern found!')
    print('Match object', match)
    print('Listing all matches:', matches)