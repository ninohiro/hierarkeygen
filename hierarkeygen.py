from hashlib import sha512
def hierarkeygen(path,parent_key):
    l=path.split('/',1)
    s=l[0]
    key=sha512(parent_key+s.encode()).digest()[:32]
    if len(l)==1:
        return key
    else:
        return generate(l[1],key)
