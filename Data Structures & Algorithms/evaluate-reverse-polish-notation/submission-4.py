class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hs = {'+', '-', '*','/'}
        stack=[]

        for token in tokens:
            if token not in hs:
                stack.append(int(token))
            elif token in hs:
                
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if token=="+":
                    stack.append(op2+op1)
                if token=="-":
                    stack.append(op2-op1)
                if token=="*":
                    stack.append(op2*op1)
                if token=="/":
                    stack.append(int(op2/op1))
        
        return stack.pop()

