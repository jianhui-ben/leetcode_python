428. Serialize and Deserialize N-ary Tree
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    ##level order
    def level(self, queue):
        temp1, temp2=[], []
        for node in queue:
            if not node: 
                temp1.append(None)
                continue
            else:
                temp1.append(node.val)
            if not node.children:
                temp2+=[None, None]
            elif len(node.children)==1:
                temp2+=[node.children[0], None]
            else:
                temp2+=node.children
        return temp1, temp2
            
    
    
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        queue= [root]
        out=[]
        while queue:
            temp, queue=self.level(queue)
            out=out+temp
        for i in range(len(out)):
            if not out[i]:
                out[i]='None'
            else:
                out[i]=str(out[i])
        print(','.join(out))
        return ','.join(out)
        
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        return 
        
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
