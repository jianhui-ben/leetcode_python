#726. Number of Atoms
#Given a chemical formula (given as a string), return the count of each atom.

#The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

#One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

#Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

#A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

#Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        ## stack + recursion
        ## use a stack to find where the end ')' is
        ## use recursion to find the map of string in '()'
        ## O(n**2) time, O(n) space
        self.stack = []
        def recursion(s):
            stored = defaultdict(int)
            i=0
            new_atom, atom_cnt= '', ''
            while i<len(s):
                if s[i]=='(':
                    i_start=i
                    self.stack.append(s[i])
                    while i<len(s) and self.stack:
                        i+=1
                        if s[i]=='(':
                            self.stack.append(s[i])
                        elif s[i]==')':
                            self.stack.pop()
                    sub_stored = recursion(s[i_start+1:i])

                elif s[i] ==')':
                    i_start=i
                    i+=1
                    while i<len(s) and s[i].isdigit():
                        i+=1
                    if i==i_start+1:
                        multi= 1
                    else:
                        multi = int(s[i_start+1: i])
                    for atom, cnt in sub_stored.items():
                        stored[atom]+=cnt*multi
                elif s[i].isupper():
                    if new_atom:
                        if not atom_cnt:
                            stored[new_atom]+=1
                        else:
                            stored[new_atom]+=int(atom_cnt)
                    new_atom, atom_cnt = '', ''
                    new_atom+=s[i]
                    i+=1
                elif s[i].islower():
                    new_atom+=s[i]
                    i+=1
                elif s[i].isdigit():
                    atom_cnt+=s[i]
                    i+=1
            ## add the atom left     
            if new_atom:
                if atom_cnt: 
                    stored[new_atom]+=int(atom_cnt)
                else:
                    stored[new_atom]+=1
            return stored
                
        stored = recursion(formula)
        out = ''
        for name, count in sorted(stored.items()):
            out+=name
            if count>1:
                out+= str(count)
        return out
        
        
