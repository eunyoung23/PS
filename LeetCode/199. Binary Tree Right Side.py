class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def fill(self,node,result,depth):
        if not node:
            return
        if depth==len(result):
            result.append(node.val)
            
        self.fill(node.right,result,depth+1)
        self.fill(node.left,result,depth+1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result_list=[]
        
        self.fill(root,result_list,0)
        
        return result_list
