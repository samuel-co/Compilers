from AST import bin_op
from AST import leaf

class ThreeAC:

    def __init__(self, ast):
        self.ast = ast
        self.temp_value = 1

    def post_order_traversal(self, current=None):
        if not current:
            current = self.ast
        left_child = current.left
        right_child = current.right
        #if it is an op node
        #-----------------------------------------------------------
        if type(left_child) is not bin_op:
            print('Left value ' + left_child.value)
        if type(right_child) is not bin_op:
            print('Right value ' + right_child.value)
        #----------------------------------------------------------
        if type(current) is bin_op:
            #go left
            if left_child and type(left_child) is bin_op:
                #------------------------------
                print("Go Left young man")
                self.post_order_traversal(left_child)
            #go right
            if right_child and type(right_child) is bin_op:
                #------------------------------
                print("Go Right young man")
                self.post_order_traversal(right_child)
            #generate code and store it in the node.
            # must have left and right child. Send the left value, right value
            # and operation in the form (op x y). Where op is a bin_op node and
            # x and y are leaf nodes. x and y have value fields and bin_op has
            # a code field.
            #------------------------------
            print("generate_code()")
            self.generate_code(current)

    def generate_code(self, node):
        # Types of operations switch on the possibilities.
        if node.op == '+':
            #------------------------
            print("add_op")
            node.code =  self.add_op(node, node.left, node.right)
            # -------------------------
            print(node.code)
        elif node.op == '-':
            #------------------------
            print("sub_op")
            node.code = self.sub_op(node, node.left, node.right)
        elif node.op == '*':
            node.code = self.mul_op(node, node.left, node.right)
        elif node.op == '/':
            node.code = self.div_op(node, node.left, node.right)
        elif node.op == ':=':
            node.code = self.assign_op(node, node.left, node.right)
        else:
            # error
            print("Something went wrone in generate_code()\n")

    def assign_op(self, node, lvalue, rvalue):
        print("In assignment")
        if type(rvalue) is not leaf:
            print(rvalue.code)
        else:
            print(rvalue.value)
    def add_op(self, node, lvalue, rvalue):
        # -------------------
        print("In add_op")
        instruction = None
        # generate code for the addition operations.
        # ADDI
        if type(lvalue) is leaf and type(rvalue) is leaf:
            #-------------------------------
            print("lvalue and rvalue are leaf nodes")
            # both children are leaf nodes and we're at the bottom of the tree.
            # There is no code to grab.
            if lvalue.type == 'FLOAT' and rvalue.type == 'FLOAT':
                #------------------------------
                print("Both are type FLOAT")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['ADDF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                               node.temp_register]
            # ADDI
            elif lvalue.type == 'INT' and rvalue.type == 'INT':
                #---------------------------
                print("Both are type INT")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['ADDI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                               node.temp_register]
        elif type(lvalue) is bin_op or type(rvalue) is bin_op:
            code_node = None
            not_code_node = None
            code = None
            instruction_type = None
            # Both children are not leaf nodes and we have code to grab.
            if type(lvalue) is bin_op:
                # get code from the left
                code_node = lvalue
                not_code_node = rvalue
            if type(rvalue) is bin_op:
                # get code from the right
                code_node = rvalue
                not_code_node = lvalue
            # Prepend instructions
            # Operate on the child temp register (that's where the data is) 
            # with the leaf node's value. Store in temp register.
            code = code_node.code
            rVal_temp_reg = code_node.temp_register
            if not_code_node.type == 'INT':
                instruction_type = 'ADDI'
            elif not_code_node.type == 'FLOAT':
                instruction_type = 'ADDF'
            else:
                print("There was a type mis-match in ad_op()")
            node.temp_register = 'T' + str(self.temp_value)
            self.temp_value += 1
            #----------------------------------------
            print(instruction_type)
            print(rVal_temp_reg)
            print(not_code_node.value)
            print(node.temp_register)
            #-------------------------------------
            new_code = [instruction_type + ' ' + rVal_temp_reg + ' ' 
                       + not_code_node.value + ' ' + node.temp_register]
            instruction = code
            code.extend(new_code)
        return instruction

    def sub_op(self, node, lvalue, rvalue):
        instruction = None
        # generate code for the subtraction operations.
        # SUBI
        #---------------------------------------
        print("In sub_op()")
        if type(lvalue) is leaf and type(rvalue) is leaf:
            #----------------------
            print("lvalu and rvalue are leaf nodes.")
            if lvalue.type == 'FLOAT' and rvalue.type == 'FLOAT':
                #------------------------
                print("They're both floats.")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['SUBF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                               node.temp_register]
            # SUBI
            elif lvalue.type == 'INT' and rvalue.type == 'INT':
                #------------------------
                print("They're both ints.")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['SUBI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                               node.temp_register]
        elif type(lvalue) is bin_op or type(rvalue) is bin_op:
            code_node = None
            not_code_node = None
            code = None
            instruction_type = None
            # Both children are not leaf nodes and we have code to grab.
            if type(lvalue) is bin_op:
                # get code from the left
                code_node = lvalue
                not_code_node = rvalue
            if type(rvalue) is bin_op:
                # get code from the right
                code_node = rvalue
                not_code_node = lvalue
            # Prepend instructions
            # Operate on the child temp register (that's where the data is) 
            # with the leaf node's value. Store in temp register.
            code = code_node.code
            rVal_temp_reg = code_node.temp_register
            if not_code_node.type == 'INT':
                instruction_type = 'SUBI'
            elif not_code_node.type == 'FLOAT':
                instruction_type = 'SUBF'
            else:
                print("There was a type mis-match in ad_op()")
            node.temp_register = 'T' + str(self.temp_value)
            self.temp_value += 1
            #----------------------------------------
            print(instruction_type)
            print(rVal_temp_reg)
            print(not_code_node.value)
            print(node.temp_register)
            #-------------------------------------
            new_code = [instruction_type + ' ' + rVal_temp_reg + ' ' 
                       + not_code_node.value + ' ' + node.temp_register]
            instruction = code
            code.extend(new_code)
        return instruction

    def mul_op(self, node, lvalue, rvalue):
        instruction = None
        # generate code for the multiplication operations.
        # MULI
        print("In mul_op()")
        if type(lvalue) is leaf and type(rvalue) is leaf:
            if lvalue.type == 'FLOAT' and rvalue.type == 'FLOAT':
                print("They're both floats.")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['MULF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                               node.temp_register]
            # MULI
            elif lvalue.type == 'INT' and rvalue.type == 'INT':
                print("They're both ints.")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['MULI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                               node.temp_register]
        elif type(lvalue) is bin_op or type(rvalue) is bin_op:
            code_node = None
            not_code_node = None
            code = None
            instruction_type = None
            # Both children are not leaf nodes and we have code to grab.
            if type(lvalue) is bin_op:
                # get code from the left
                code_node = lvalue
                not_code_node = rvalue
            if type(rvalue) is bin_op:
                # get code from the right
                code_node = rvalue
                not_code_node = lvalue
            # Prepend instructions
            # Operate on the child temp register (that's where the data is) 
            # with the leaf node's value. Store in temp register.
            code = code_node.code
            rVal_temp_reg = code_node.temp_register
            if not_code_node.type == 'INT':
                instruction_type = 'MULI'
            elif not_code_node.type == 'FLOAT':
                instruction_type = 'MULF'
            else:
                print("There was a type mis-match in ad_op()")
            node.temp_register = 'T' + str(self.temp_value)
            self.temp_value += 1
            #----------------------------------------
            print(instruction_type)
            print(rVal_temp_reg)
            print(not_code_node.value)
            print(node.temp_register)
            #-------------------------------------
            new_code = [instruction_type + ' ' + rVal_temp_reg + ' ' 
                       + not_code_node.value + ' ' + node.temp_register]
            instruction = code
            code.extend(new_code)
        #---------------------------------
        print("Instruction :")
        print(instruction)
        return instruction

    def div_op(self, node,lvalue, rvalue):
        instruction = None
        # generate code for the division operations.
        # DIVI
        if type(lvalue) is leaf and type(rvalue) is leaf:
            if lvalue.type == 'FLOAT' and rvalue.type == 'FLOAT':
                print("They're both floats.")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['DIVF ' + lvalue.value + ' ' + rvalue.value + ' ' +
                              node.temp_register]
            # DIVF
            elif lvalue.type == 'INT' and rvalue.type == 'INT':
                print("They're both ints.")
                node.temp_register = 'T' + str(self.temp_value)
                self.temp_value += 1
                instruction = ['DIVI ' + lvalue.value + ' ' + rvalue.value + ' ' +
                              node.temp_register]
        elif type(lvalue) is bin_op or type(rvalue) is bin_op:
            code_node = None
            not_code_node = None
            code = None
            instruction_type = None
            # Both children are not leaf nodes and we have code to grab.
            if type(lvalue) is bin_op:
                # get code from the left
                code_node = lvalue
                not_code_node = rvalue
            if type(rvalue) is bin_op:
                # get code from the right
                code_node = rvalue
                not_code_node = lvalue
            # Prepend instructions
            # Operate on the child temp register (that's where the data is) 
            # with the leaf node's value. Store in temp register.
            code = code_node.code
            rVal_temp_reg = code_node.temp_register
            if not_code_node.type == 'INT':
                instruction_type = 'DIVI'
            elif not_code_node.type == 'FLOAT':
                instruction_type = 'DIVF'
            else:
                print("There was a type mis-match in ad_op()")
            node.temp_register = 'T' + str(self.temp_value)
            self.temp_value += 1
            #----------------------------------------
            print(instruction_type)
            print(rVal_temp_reg)
            print(not_code_node.value)
            print(node.temp_register)
            #-------------------------------------
            new_code = [instruction_type + ' ' + rVal_temp_reg + ' ' 
                       + not_code_node.value + ' ' + node.temp_register]
            instruction = code
            code.extend(new_code)
        return instruction




