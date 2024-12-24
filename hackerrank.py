def sameSubString(s,t,k,cost=0,count=0):
        for ind in range(len(s)):
            cost=abs(ord(s[ind])-ord(t[ind]))
            if cost<k:
                k=k-cost 
                s=s.replace(s[ind],t[ind])                 
                count+=1
            elif cost==0:
                 pass
        
            else:
                print(s)
                return count
        print(s)       
        return count
         
         
s='pranaya'
t='ranaya'
k=6
print(sameSubString(s,t,k))
