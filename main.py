import sys
def isMapping(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1)!=len(s2) or len(s1)==0 or len(s2)==0:
        return False
  
    exists = {}
    
    for i in range(len(s1)):
        if s1[i] in exists:
            if not exists[s1[i]] == s2[i]:
                return False
        else:
            exists[s1[i]] = s2[i]
            
    return True


def main():

    if __name__ == "__main__":
        for i, arg in enumerate(sys.argv):
            if i==1:
                s1=arg
            elif i==2:
                s2=arg


    print(str(isMapping(s1,s2)).lower())

    return


main()

