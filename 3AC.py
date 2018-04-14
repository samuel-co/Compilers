

class 3AC:

    temp_value = 1

    def __init__(self, ast):
        self.ast = ast

    def post_order_traversal(self):
        self.ast = current
        #if it is an op node
        if type(current) is bin_op:
            #go left
            if (left_child = current.left) and
                    type(left_child) is bin_op:
                post_order_traversal(left_child)
            #go right
            if (right_child = current.right) and
                    type(right_child) is bin_op:
                post_order_traversal(right_child)

            #generate code and store it in the node.
            # must have left and right child. Send the left value, right value
            # and operation in the form (op x y). Where op is a bin_op node and
            # x and y are leaf nodes. x and y have value fields and bin_op has
            # a code field.
            generate_code(current)

    def generate_code(self, node):
        # Types of operations switch on the possibilities.
        if node.op == '+':
            node.temp_register = 'T' + str(global temp_value)
            node.code =  add_op(this, node.left.value, node.right.value)
            global temp_value += 1
        elif node.op == '-':
            node.temp_registar = 'T' + str(global temp_value)
            node.code = sub_op(node.left.value, node.right.value)
            global temp_value += 1
        elif node.op == '*':
            node.temp_registar = 'T' + str(global temp_value)
            node.conde = mul_op(node.left.value, node.right.value)
            global temp_value += 1
        elif node.op == '/':
            node.temp_registar = 'T' + str(global temp_value)
            node.code = div_op(node.left.value, node.right.value)
            global temp_value += 1
        else:
            # error
            print("Something went wrone in generate_code()\n")

    def add_op(self, node, lvalue, rvalue):
        instruction = None
        # generate code for the addition operations.
        # ADDI
        if lvalue.type == 'float' and rvalue.type == 'float':
            instruction = ['ADDI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                           node.temp_register]
        # ADDF
        elif lvalue.type == 'int' and rvalue.type == 'int':
            instruction = ['ADDF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                           node.temp_register]

        return instruction

    def sub_op(self, lvalue, rvalue):
        instruction = None
        # generate code for the subtraction operations.
        # SUBI
        if lvalue.type == 'float' and rvalue.type == 'float':
            instruction = ['SUBI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                           node.temp_register]
        # SUBF
        elif lvalue.type == 'int' and rvalue.type == 'int':
            instruction = ['SUBF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                           node.temp_register]
        return instruction

    def mul_op(self, lvalue, rvalue):
        instruction = None
        # generate code for the multiplication operations.
        # MULI
        if lvalue.type == 'float' and rvalue.type == 'float':
            instruction = ['MULI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                           node.temp_register]
        # MULF
        elif lvalue.type == 'int' and rvalue.type == 'int':
            instruction = ['MULF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                           node.temp_register]
        return instruction

    def div_op(self, lvalue, rvalue):
        instruction = None
        # generate code for the division operations.
        # DIVI
        if lvalue.type == 'float' and rvalue.type == 'float':
            instruction = ['DIVI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                          node.temp_register]
        # DIVF
        elif lvalue.type == 'int' and rvalue.type == 'int':
            instruction = ['DIVF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                          node.temp_register]
        return instruction




