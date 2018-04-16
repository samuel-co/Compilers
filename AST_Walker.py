from Node import *

class ast_walker:

    def __init__(self, tree, symbol_table):
        self.tree = tree
        self.symbol_table = symbol_table
        self.indentation = 0

        self.code = ""
        self.label_count = 1
        self.register_count = 1

    def print_code(self):
        print(";{}".format(self.symbol_table))
        print(";-----PRINTING CODE-----")
        for key in self.symbol_table.keys():
            if self.symbol_table[key] != "STRING": print("var {}".format(key))
        print(self.code)


    def indent(self):
        print(end=";")
        for _ in range(self.indentation): print(end="   ")

    def print_tree(self):
        print(";-----PRINTING TREE-----")
        self.node_prints = {str_ass:self.print_str, bin_op:self.print_bin, func_op:self.print_func, while_op:self.print_while, sys_op:self.print_sys, if_op:self.print_if}
        for item in self.tree:
            self.indent()
            self.node_prints[type(item)](item)
        self.code += "sys halt"

    def print_func(self, child):
        print("entering function {}".format(child.name))
        self.code += "label {}\n".format(child.name)
        self.indentation += 1
        for item in child.body:
            self.indent()
            self.node_prints[type(item)](item)
        self.indentation -= 1
        self.indent()
        print("exiting function {}".format(child.name))

    def print_if(self, child):
        # self.code += "jump {}{}{} label{}\n".format(child.cond.left.value, child.cond.op, child.cond.right.value, self.label_count)
        end_if_label = self.label_count
        self.label_count += 1
        print("if (", end="")
        self.print_comp(child.cond)
        self.indentation += 1
        for item in child.if_body:
            self.indent()
            self.node_prints[type(item)](item)
        if child.else_body:
            self.code += "jmp label{}\n".format(self.label_count)
            self.code += "label label{}\n".format(end_if_label)
            self.indent()
            print("entering else")
            for item in child.else_body:
                self.indent()
                self.node_prints[type(item)](item)
            self.indent()
            print("exiting else")
            self.code += "label label{}\n".format(self.label_count)
            self.label_count += 1
        else: self.code += "label label{}\n".format(end_if_label)
        self.indentation -= 1
        self.indent()
        print("exiting if")

    def print_while(self, child):
        self.code += "label label{}\n".format(self.label_count)
        end_label = "jmp label{}\nlabel label{}\n".format(self.label_count, self.label_count+1)
        # self.code += "jump {}{}{} label{}\n".format(child.cond.left.value, child.cond.op, child.cond.right.value, self.label_count+1)
        self.label_count += 2
        print("while (", end="")
        self.print_comp(child.cond)
        self.indentation += 1
        for item in child.body:
            self.indent()
            self.node_prints[type(item)](item)
        self.indentation -= 1
        self.indent()
        self.code += end_label
        print("exiting while loop")

    def print_str(self, child):
        print("{}:={}".format(child.name, child.value))
        self.code += "str {} {}\n".format(child.name, child.value)

    def print_comp(self, child):
        comp_dict = {"<":"jge", ">":"jle", "<=":"jgt", ">=":"jlt", "!=":"jeq", "=":"jne"}
        left, right = (child.left.value, child.right.value)
        if not child.left.value in self.symbol_table.keys():
            self.code += "move {} r{}\n".format(child.left.value, self.register_count)
            left = "r{}".format(self.register_count)
            self.register_count += 1
        if not child.right.value in self.symbol_table.keys():
            self.code += "move {} r{}\n".format(child.right.value, self.register_count)
            right = "r{}".format(self.register_count)
            self.register_count += 1
        self.code += "cmp{} {} {}\n".format(child.left.type[:1].lower() if child.left.type != "FLOAT" else "r", left, right)
        self.code += "{} label{}\n".format(comp_dict[child.op], self.label_count-1)
# jmp target             ; unconditional jump
# jgt target             ; jump if (op1 of the preceeding cmp was) greater (than op2)
# jlt target             ; jump if less than
# jge target             ; jump if greater of equal
# jle target             ; jump if less or equal
# jeq target             ; jump if equal
# jne target             ; jump if not equal

        self.recurse(child.left)
        print(child.op, end='')
        self.recurse(child.right)
        print(")")

    def print_sys(self, node):
        # print("PRINTG THROUGH PRINT_SYS")
        self.sys_recurse(node)
        print()

    def sys_recurse(self, node):
        if not node: return
        if type(node) is leaf:
            print(node.value, end=", ")
            self.code += "{} {}\n".format(node.type[:1].lower() if node.type != "FLOAT" else "r", node.value)
            return
        if type(node.left) is leaf:
            print(node.op, end=":")
            self.code += "sys {}".format(node.op.lower())
        self.sys_recurse(node.left)
        if type(node.right) is leaf:
            print(node.op, end=":")
            self.code += "sys {}".format(node.op.lower())
        self.sys_recurse(node.right)

    def print_bin(self, node):
        self.recurse(node)
        print()

    def print_ast(self):
        ''' Print out each tree conained within the roots list'''
        self.print_tree(self.tree)
        for root in self.roots:
            self.recurse(root)
            print()

    def recurse(self, node):
        ''' Print out a AST from the bottom leftmost node to the rightmost node. Parenthesizes expressions
            that are paired below an operation node'''
        if not node: return
        if type(node) is leaf:
            # print("[{}]".format(node.value), end="")
            # print("{}[{}]".format(node.value, node.type), end="")
            print(node.value, end="")
            return
        if node.left and node.op != ':=': print("(", end="")
        self.recurse(node.left)
        print(node.op, end="")
        self.recurse(node.right)
        if node.left and node.op != ':=': print(")", end="")



