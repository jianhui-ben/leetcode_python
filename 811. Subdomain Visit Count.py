#811. Subdomain Visit Count

#A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

#Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

#We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

#Example 1:
#Input: 
#["9001 discuss.leetcode.com"]
#Output: 
#["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
#Explanation: 
#We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ## hashtable
        
        stored = defaultdict(int)
        for i in cpdomains:
            cnt, domain =int(i[0:i.index(" ")]), i[i.index(" ")+1:]
            saved_index = [k for k, v in enumerate(domain) if v=='.']
            stored[domain]+=cnt
            for k in saved_index:
                stored[domain[k+1:]]+=cnt
                
        
        return [str(cnt)+" "+ domain for domain, cnt in stored.items()]
            
                
            


