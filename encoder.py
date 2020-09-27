class message_encoder:

    def __init__(self):
        None

    def encode(self, message , key):
        ret = []
        if len(message) % len(key)==0:
            r=int(len(message)/len(key))
        else:
            r=int(len(message)/len(key)+1)
        di=dict()
        li=list()
        for i in key:
            li.append(i)
        x=0
        for j in range(0,r,1):
            for i in li:
                if j==0:
                    words=list()
                else:
                    words=di[i]
                if x>=len(message):
                    break;
                y=message[x]
                words.append(y)
                di[i]=words
                x=x+1
        li.sort()
        x=0
        for i in li:
            words=di[i]
            for j in range(r):
                if x>=len(message):
                    ret.append("_")
                    print("_",end="")
                    x=x+1
                else:
                    ret.append(words[j])
                    print(words[j],end="")
                    x=x+1

        return ret
