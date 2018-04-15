from Node import *

class ast_walker:

    def __init__(self, tree, symbol_table):
        self.tree = tree
        self.symbol_table = symbol_table
        self.indentation = 0


    def indent(self):
        for _ in range(self.indentation): print(end="   ")

    def print_tree(self):

        print("-----PRINTING TREE-----")
        self.node_prints = {bin_op:self.print_bin, func_op:self.print_func, while_op:self.print_while, sys_op:self.print_sys, if_op:self.print_if}
        for item in self.tree:
            self.indent()
            self.node_prints[type(item)](item)

    def print_func(self, child):
        print("entering function {}".format(child.name))
        self.indentation += 1
        for item in child.body:
            self.indent()
            self.node_prints[type(item)](item)
        self.indentation -= 1
        self.indent()
        print("exiting function {}".format(child.name))

    def print_if(self, child):
        print("if (", end="")
        self.print_comp(child.cond)
        self.indentation += 1
        for item in child.if_body:
            self.indent()
            self.node_prints[type(item)](item)
        if child.else_body:
            self.indent()
            print("entering else")
            for item in child.else_body:
                self.indent()
                self.node_prints[type(item)](item)
            self.indent()
            print("exiting else")
        self.indentation -= 1
        self.indent()
        print("exiting if")

    def print_while(self, child):
        print("while (", end="")
        self.print_comp(child.cond)
        self.indentation += 1
        for item in child.body:
            self.indent()
            self.node_prints[type(item)](item)
        self.indentation -= 1
        self.indent()
        print("exiting while loop")

    def print_comp(self, child):
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
            return
        if type(node.left) is leaf: print(node.op, end=":")
        self.sys_recurse(node.left)
        if type(node.right) is leaf: print(node.op, end=":")
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



