class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = defaultdict(list)
        
        for [i,child] in enumerate(leftChild):
            parents[child].append(i)
        for [i,child] in enumerate(rightChild):
            parents[child].append(i)
            
        root=None
        for i in range(n):
            if len(parents[i])>1: return False
            if len(parents[i])==0:
                if root!=None:
                    return False
                else:
                    root = i
        if root==None: return False
        
        seen=set()
        def dfs(node):
            if node in seen: return
            seen.add(node)
            if leftChild[node]!=-1: dfs(leftChild[node])
            if rightChild[node]!=-1: dfs(rightChild[node])
        dfs(root)

        return len(seen)==n
        