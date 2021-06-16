#Decrypt Message

#An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that they indeed encrypt their messages, and studied their method of encryption.

#Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

#Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

#For instance, to encrypt the word “crime”

#Decrypted message:	c	r	i	m	e
#Step 1:	99	114	105	109	101
#Step 2:	100	214	319	428	529
#Step 3:	100	110	111	116	113
#Encrypted message:	d	n	o	t	q

#The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

#Explain your solution and analyze its time and space complexities.

#Examples:

#input:  word = "dnotq"
#output: "crime"

#input:  word = "flgxswdliefy"
#output: "encyclopedia"



def decrypt(word):
  
  stack = [ord(i) for i in word] #100	110	111	116	113
  second_step, out = [None] * len(stack), [None] * len(stack)
  second_step[0] = stack[0]
  out[0] = stack[0] - 1
  for i in range(1, len(stack)):
    
    cur_sum = stack[i] - second_step[i-1]
    
    while cur_sum <97:
      cur_sum += 26
      
    out[i] =  cur_sum
    second_step[i] = cur_sum + second_step[i-1]
    
  return ''.join([chr(i) for i in out])
    
  
  
  '''
  111    = (105) dec[n] + 214 (second step in previous index) - 26 * m
  second step = (105) dec[n] + 214 (second step in previous index
  '''
  
