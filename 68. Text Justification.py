##68. Text Justification
#Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

#You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

#Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

#For the last line of text, it should be left justified and no extra space is inserted between words.

#Note:

#A word is defined as a character sequence consisting of non-space characters only.
#Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#The input array words contains at least one word.


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ## O(n), O(n)
        ## middle justified and left justtified (oneword in a line or last line)
        out, cur_i, cur_j=[], 0, 0
        
        while cur_i<len(words):
            tempLen=0
            while cur_j< len(words) and tempLen+len(words[cur_j])+(cur_j-cur_i)<= maxWidth:
                tempLen+=len(words[cur_j])
                cur_j+=1
            new_line= '*'*maxWidth   
            
            ## the current line has words[cur_i: cur_j], middle justified
            if cur_j-cur_i>1 and cur_j<len(words):
                spaceBetween= (maxWidth-tempLen)//(cur_j-cur_i-1)
                extraSpace = (maxWidth-tempLen)%(cur_j-cur_i-1)
                
                cur_k=0
                for cur_word in words[cur_i:cur_j]:
                    new_line= new_line[:cur_k]+cur_word +new_line[cur_k+ len(cur_word):]
                    cur_k+=len(cur_word)
                    cur_k+= spaceBetween
                    if extraSpace:
                        cur_k+=1
                        extraSpace-=1
            else:
                cur_k=0
                for cur_word in words[cur_i:cur_j]:
                    new_line= new_line[:cur_k]+cur_word +new_line[cur_k+ len(cur_word):]             
                    cur_k+=len(cur_word)
                    cur_k+=1
            for i in range(len(new_line)):
                if new_line[i]=='*':
                    new_line= new_line[:i]+' '+ new_line[i+1:]
            
            out.append(new_line)
            cur_i=cur_j

        return out


            
            
            
            
