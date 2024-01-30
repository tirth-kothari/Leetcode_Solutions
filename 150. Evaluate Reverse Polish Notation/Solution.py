class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
                match i: 
                    case '+':
                        l=stack.pop()
                        r=stack.pop()
                        stack.append(l+r)
                    case '-':
                        l=stack.pop()
                        r=stack.pop()
                        stack.append(r-l)
                    case '*':
                        l=stack.pop()
                        r=stack.pop()
                        stack.append(l*r)
                    case '/':
                        l=stack.pop()
                        r=stack.pop()
                        stack.append(int(r/l))
                    case _:                  
                        stack.append(int(i))
        return stack[0]
