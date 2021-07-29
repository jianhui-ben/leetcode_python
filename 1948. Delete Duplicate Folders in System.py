#1948. Delete Duplicate Folders in System
#Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.

#For example, ["one", "two", "three"] represents the path "/one/two/three".
#Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.

#For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
#/a
#/a/x
#/a/x/y
#/a/z
#/b
#/b/x
#/b/x/y
#/b/z
#However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
#Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

#Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.deleted = False
    
    def add_word(self, word):
        cur =  self
        for c in word:
            # cur.child[c] = TrieNode()            
            cur = cur.child[c]

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        paths.sort()
        
        root, stored = TrieNode(), defaultdict(list)
        
        for path in paths:
            root.add_word(path)

        def serialize(root, stored):
            if not root.child: return ""
            
            cur_key = []
            for next_letter, next_node in root.child.items():
                if len(next_letter):
                    cur_key.append(next_letter + ':' + serialize(next_node, stored))
            
            s = '(' + ''.join(cur_key) + ')'
            stored[s].append(root)
            return s
    
        
        # for _, child_node in root.child.items():
        serialize(root, stored)

        # print(stored.keys())
        
        for serilized_str, list_of_nodes in stored.items():
            if len(list_of_nodes) > 1:
                for node in list_of_nodes:
                    node.deleted = True
        
        
        out = []
        
        def dfsGetUnique(node, cur_path):
            nonlocal out
            if not node or node.deleted: return
            for next_letter, next_node in node.child.items():
                if not next_node.deleted:
                    out.append(cur_path + [next_letter])
                    dfsGetUnique(next_node, cur_path + [next_letter])
                
        dfsGetUnique(root, [])
        return out
                    
        
        
        
                
        
