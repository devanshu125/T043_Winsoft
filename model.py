class eval:
    def __init__(self):
        self.location_dict = {"Khardung La": ["A", (0, 10)], "Lachulang La":["B", (10, 20)], "Sasser Pass":["C", (10, 10)],
                        "Gyong La":["D", (10, 0)], "Sia La":["E", (20, 20)], "Zoji La":["F", (20, 10)],
                        "Indira Col":["G", (20, 0)], "Rezang La":["H", (30, 10)], "Tanglang La":["I", (40, 20)],
                        "Pensi La":["J", (40, 0)], "Marsimik La":["K", (50, 10)]
                        }
    def arrange(self, k):
        b = ""
        for i in sorted(k):
            b += i
        k, b = b, k
        d = {}
        for i in range(len(k)):
            if k[i] not in d.keys():
                d[k[i]] = [i]
            else:
                d[k[i]].append(i)
        ret = []
        for i in b:
            ret.append(d[i][0])
            d[i].pop(0)
        return ret

    def decode_message(self, x, key):
        ret = ""
        ctr = 0
        step = len(x) // len(key)
        ind = self.arrange(key)
        for i in range(step):
            temp = ""
            for j in range(ctr, (len(key) * step) , step):
                # print(x[j], end="")
                temp = temp + x[j]
            for k in range(len(key)):
                ret = ret + temp[ind[k]]
                # print(temp[ind[k]], end="")

            ctr += 1
        return ret

    def extract_location(self,msg):
        master = list(self.location_dict.keys())
        ret = []
        for i in master:
            if i in msg:
                ret.append(i)
        return ret

    def run(self, x, key):
        x = "Cnwvtus KuaiTaa rlodeeurethn  an Ia_mrhs baer oag ndC_a aeoat dLj lLdio_me  p  hagZLngan _"
        key = "DELHI"
        ret = []

        ret.append("encrypted message is:")
        ret.append(x)
        ret.append("key:" + " " + key)

        decoded = self.decode_message(x, key).replace("_", "")
        ret.append("decoded message is:")
        ret.append(decoded)

        return ret
