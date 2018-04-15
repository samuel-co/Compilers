class stack():
    def __init__(self):
        self.stack = []

    def put(self, value):
        self.stack.append(value)

    def get(self):
        out = self.stack[-1]
        self.stack = self.stack[:-1]
        return out

class func_op():
    def __init__(self, name=None):
        self.name = name
        self.body = []

class while_op():
    def __init__(self):
        self.cond = None
        self.body = []

class if_op():
    def __init__(self):
        self.cond = None
        self.if_body = []
        self.else_body = []

class sys_op():
    def __init__(self, left=None,right=None, op=None):
        self.op = op
        self.left = left
        self.right = right

class comp_op():
    def __init__(self, left=None, right=None, op=None):
        self.op = op
        self.left = left
        self.right = right

class bin_op():
    def __init__(self, left=None, right=None, op=None):
        self.left = left
        self.right = right
        self.op = op
        self.code = []
        self.temp_register = None

class leaf():
    def __init__(self, value=None, in_type=None):
        self.value = value
        self.type = in_type

