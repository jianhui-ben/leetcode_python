#93. Restore IP Addresses
#Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

#A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

#Example 1:

#Input: s = "25525511135"
#Output: ["255.255.11.135","255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ##backtracking
        ## time 3**4
        
        
        out = []
        def backtrack(rest, path):
            if path[0]=='4':
                if not rest:
                    out.append(path[2:-1])
                return
            for i in range(1, min(4, len(rest)+1)):
                if (rest[0]=='0' and len(rest[:i])==1) or \
                ((int(rest[:i])>0 and int(rest[:i]))<=255 and rest[0]!='0'):
                    path=str(int(path[0])+1)+path[1:]
                    backtrack(rest[i:], path+rest[:i]+'.')
                    path=str(int(path[0])-1)+path[1:]    
        backtrack(s, '0#')
        return out
        