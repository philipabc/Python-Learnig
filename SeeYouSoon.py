for s in range(10):
    for e in range(10):
        for y in range(10):
            for o in range(10):
                for u in range(10):
                    for n in range(10):
                        NoRepeat={s,e,y,o,u,n}
                        if len(NoRepeat)==6:
                            if ((s*100+y*100)+(e*10+o*10)+(u+e)==(s*1000+o*100+o*10+n)):
                                print(" ",s,e,e)
                                print("+",y,o,u)
                                print("__________")
                                print(s,o,o,n)
                                print()
