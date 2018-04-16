# Generated from /home/ubuntu/Little.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LittleParser import LittleParser
else:
    from LittleParser import LittleParser

from Node import *

# This class defines a complete listener for a parse tree produced by LittleParser.
class AST(ParseTreeListener):

    def __init__(self, symbol_table):
        self.symbol_table = self.parse_symbol_table(symbol_table)
        self.roots = []
        self.root = None
        self.tree = []
        self.current_list = self.tree
        self.control_q = stack()
        self.head = None

    def parse_symbol_table(self, symbol_table):
        return {symbol_table["GLOBAL"][var][0]:symbol_table["GLOBAL"][var][1] for var in range(len(symbol_table["GLOBAL"]))}

    def add_root(self):
        if type(self.root) is bin_op or type(self.root) is sys_op:
            self.roots.append(self.root)
        self.current_list.append(self.root)

    def visit_expr(self, child):
        ''' Loop for handling the possible cases of an expression  node'''
        if child.expr_prefix().empty(): return self.visit_factor(child.factor())

        node = bin_op()
        node.op = child.expr_prefix().addop().getText()
        if child.expr_prefix().expr_prefix().empty():
            node.left = self.visit_factor(child.expr_prefix().factor())
            node.right = self.visit_factor(child.factor())
        else:
            node.left = self.visit_expr_prefix(child.expr_prefix())
            node.right = self.visit_factor(child.factor())

        # print("left: {}".format(node.left))
        # print("op: {}".format(node.op))
        # print("right: {}".format(node.right))

        return node

    def visit_factor(self, child):
        ''' Loop for handling the possible cases of a factor node'''
        if self.is_end(child): return self.visit_primary(child.postfix_expr().primary())

        node = bin_op()
        node.op = child.factor_prefix().mulop().getText()
        if child.factor_prefix().factor_prefix().empty():
            node.left = self.visit_primary(child.factor_prefix().postfix_expr().primary())
            node.right = self.visit_primary(child.postfix_expr().primary())
        else:
            node.left = self.visit_factor_prefix(child.factor_prefix())
            node.right = self.visit_primary(child.postfix_expr().primary())

        # print("left: {}".format(node.left))
        # print("op: {}".format(node.op))
        # print("right: {}".format(node.right))

        return node

    def visit_factor_prefix(self, child):
        ''' Loop for handling the possible cases of a factor_prefix node'''
        # if self.is_end(child): return leaf(value=child.getText())

        node = bin_op()
        node.op = child.factor_prefix().mulop().getText()
        if child.factor_prefix().factor_prefix().empty():
            node.left = self.visit_primary(child.factor_prefix().postfix_expr().primary())
            node.right = self.visit_primary(child.postfix_expr().primary())
        else:
            node.left = self.visit_factor_prefix(child.factor_prefix())
            node.right = self.visit_primary(child.postfix_expr().primary())

        # print("left: {}".format(node.left))
        # print("op: {}".format(node.op))
        # print("right: {}".format(node.right))

        return node


    def visit_expr_prefix(self, child):
        ''' Loop for handling the possible cases of a expr_prefix node'''
        # if self.is_end(child):return leaf(value=child.getText())

        node = bin_op()
        node.op = child.expr_prefix().addop().getText()
        if child.expr_prefix().expr_prefix().empty():
            node.left = self.visit_primary(child.expr_prefix().factor().postfix_expr().primary())
            node.right = self.visit_factor(child.factor())
        else:
            node.left = self.visit_expr_prefix(child.expr_prefix())
            node.right = self.visit_factor(child.factor())

        # print("left: {}".format(node.left))
        # print("op: {}".format(node.op))
        # print("right: {}".format(node.right))

        return node

    def visit_primary(self, child):
        ''' Checks if our value is a node, or is a parenthesized expression. Returns the releveant construct.'''
        if type(child) is LittleParser.PrimaryContext and child.expr():
            return self.visit_expr(child.expr())
        else:
            return leaf(value=child.getText(), in_type=self.symbol_table[child.getText()] if child.getText() in self.symbol_table.keys() else "FLOAT" if '.'\
                    in child.getText() else "INT")

    def is_end(self, child):
        ''' Check if the current node is the last node in its branch. Returns true if so. '''
        # if child.getChildCount() == 0:
        #     return True
        real_children = 0
        for i in range(0, child.getChildCount()):
            if child.getChild(i).getText() != '': real_children += 1
        if real_children == 1:return True
        return False

    def visit_id_list(self, child, op):
        if child.id_tail().empty():
            return leaf(value=child.ident().getText(), in_type=self.symbol_table[child.ident().getText()])
        node = sys_op(op=op)
        node.left = leaf(value=child.ident().getText(), in_type=self.symbol_table[child.ident().getText()])
        node.right = self.visit_id_list(child.id_tail(), op)
        return node

    def visit_cond(self, child):
        node = comp_op(op=child.compop().getText())
        node.left = self.visit_expr(child.getChild(0))
        node.right = self.visit_expr(child.getChild(2))
        return node

#------------------------------LISTENER FUNCTIONS----------------------------------------------

    # Enter a parse tree produced by LittleParser#empty.
    def enterEmpty(self, ctx:LittleParser.EmptyContext):
        pass

    # Exit a parse tree produced by LittleParser#empty.
    def exitEmpty(self, ctx:LittleParser.EmptyContext):
        pass

    # Enter a parse tree produced by LittleParser#stmt_list.
    def enterStmt_list(self, ctx:LittleParser.Stmt_listContext):
        # print("enter stmt_list")
        pass

    # Enter a parse tree produced by LittleParser#func_decl.
    def enterFunc_decl(self, ctx:LittleParser.Func_declContext):
        # print("enter func")
        self.root = func_op(name="main")
        self.add_root()
        self.control_q.put(self.current_list)
        self.current_list = self.root.body
        pass

    # Exit a parse tree produced by LittleParser#func_decl.
    def exitFunc_decl(self, ctx:LittleParser.Func_declContext):
        # print("exit func")
        self.current_list = self.control_q.get()
        pass

    # Exit a parse tree produced by LittleParser#stmt_list.
    def exitStmt_list(self, ctx:LittleParser.Stmt_listContext):
        # print("exit stmt_list")
        pass

    # Enter a parse tree produced by LittleParser#stmt.
    def enterStmt(self, ctx:LittleParser.StmtContext):
        # print("enter stmt")
        pass

    # Exit a parse tree produced by LittleParser#stmt.
    def exitStmt(self, ctx:LittleParser.StmtContext):
        # print("exit stmt")
        pass

    # Enter a parse tree produced by LittleParser#if_stmt.
    def enterIf_stmt(self, ctx:LittleParser.If_stmtContext):
        self.root = if_op()
        self.root.cond = self.visit_cond(ctx.cond())
        self.head = self.root
        self.add_root()
        self.control_q.put(self.current_list)
        self.current_list = self.root.if_body
        # print("enter if")
        pass

    # Exit a parse tree produced by LittleParser#if_stmt.
    def exitIf_stmt(self, ctx:LittleParser.If_stmtContext):
        self.current_list = self.control_q.get()
        # print("exit if")
        pass

    # Enter a parse tree produced by LittleParser#else_part.
    def enterElse_part(self, ctx:LittleParser.Else_partContext):
        self.control_q.put(self.current_list)
        self.current_list = self.head.else_body
        # print("enter else")
        pass

    # Exit a parse tree produced by LittleParser#else_part.
    def exitElse_part(self, ctx:LittleParser.Else_partContext):
        self.current_list = self.control_q.get()
        # print("exit else")
        pass

    # Enter a parse tree produced by LittleParser#while_stmt.
    def enterWhile_stmt(self, ctx:LittleParser.While_stmtContext):
        # print("enter while")
        self.root = while_op()
        self.root.cond = self.visit_cond(ctx.cond())
        self.add_root()
        self.control_q.put(self.current_list)
        self.current_list = self.root.body
        pass

    # Exit a parse tree produced by LittleParser#while_stmt.
    def exitWhile_stmt(self, ctx:LittleParser.While_stmtContext):
        # print("exit while")
        self.current_list = self.control_q.get()
        pass

     # Enter a parse tree produced by LittleParser#expr.
    def enterExpr(self, ctx:LittleParser.ExprContext):
        pass

    # Exit a parse tree produced by LittleParser#expr.
    def exitExpr(self, ctx:LittleParser.ExprContext):
        # print("exiting expr")
        pass

    # Enter a parse tree produced by LittleParser#assign_expr.
    def enterAssign_expr(self, ctx:LittleParser.Assign_exprContext):
        self.root = bin_op()
        self.root.op = ':='
        # self.root.left = leaf(value=ctx.ident().getText())
        self.root.left = self.visit_primary(ctx.ident())
        # print("assigning to var {}".format(self.root.left))
        self.root.right = self.visit_expr(ctx.getChild(2))
        # print("root right {}".format(self.root.right))

    # Exit a parse tree produced by LittleParser#assign_expr.
    def exitAssign_expr(self, ctx:LittleParser.Assign_exprContext):
        self.add_root()

    # Enter a parse tree produced by LittleParser#string_decl.
    def enterString_decl(self, ctx:LittleParser.String_declContext):
        # return
        # self.root = bin_op()
        # self.root.op = ':='
        # self.root.left = leaf(value=ctx.ident().getText(), in_type="STRING")
        # self.root.right = leaf(value=ctx.strt().getText(), in_type="STRING")
        self.root = str_ass(name=ctx.ident().getText(), value=ctx.strt().getText())

    # Exit a parse tree produced by LittleParser#string_decl.
    def exitString_decl(self, ctx:LittleParser.String_declContext):
        # return
        self.add_root()

        # Enter a parse tree produced by LittleParser#read_stmt.
    def enterRead_stmt(self, ctx:LittleParser.Read_stmtContext):
        self.root = sys_op(op="READ", left=leaf(value=ctx.id_list().ident().getText(), in_type=self.symbol_table[ctx.id_list().ident().getText()]))
        if not ctx.id_list().id_tail().empty(): self.root.right = self.visit_id_list(ctx.id_list().id_tail(), "READ")

    # Exit a parse tree produced by LittleParser#read_stmt.
    def exitRead_stmt(self, ctx:LittleParser.Read_stmtContext):
        self.add_root()

    # Enter a parse tree produced by LittleParser#write_stmt.
    def enterWrite_stmt(self, ctx:LittleParser.Write_stmtContext):
        self.root = sys_op(op="WRITE", left=leaf(value=ctx.id_list().ident().getText(), in_type=self.symbol_table[ctx.id_list().ident().getText()]))
        if not ctx.id_list().id_tail().empty(): self.root.right = self.visit_id_list(ctx.id_list().id_tail(), "WRITE")

    # Exit a parse tree produced by LittleParser#write_stmt.
    def exitWrite_stmt(self, ctx:LittleParser.Write_stmtContext):
        self.add_root()
        pass

    # Enter a parse tree produced by LittleParser#expr_prefix.
    def enterExpr_prefix(self, ctx:LittleParser.Expr_prefixContext):
        # print("entered")
        return

    # Exit a parse tree produced by LittleParser#expr_prefix.
    def exitExpr_prefix(self, ctx:LittleParser.Expr_prefixContext):
        pass

    # Enter a parse tree produced by LittleParser#addop.
    def enterAddop(self, ctx:LittleParser.AddopContext):
        pass

    # Exit a parse tree produced by LittleParser#addop.
    def exitAddop(self, ctx:LittleParser.AddopContext):
        pass

    # Enter a parse tree produced by LittleParser#program.
    def enterProgram(self, ctx:LittleParser.ProgramContext):
        pass

    # Exit a parse tree produced by LittleParser#program.
    def exitProgram(self, ctx:LittleParser.ProgramContext):
        pass


    # Enter a parse tree produced by LittleParser#ident.
    def enterIdent(self, ctx:LittleParser.IdentContext):
        pass

    # Exit a parse tree produced by LittleParser#ident.
    def exitIdent(self, ctx:LittleParser.IdentContext):
        pass


    # Enter a parse tree produced by LittleParser#pgm_body.
    def enterPgm_body(self, ctx:LittleParser.Pgm_bodyContext):
        pass

    # Exit a parse tree produced by LittleParser#pgm_body.
    def exitPgm_body(self, ctx:LittleParser.Pgm_bodyContext):
        pass


    # Enter a parse tree produced by LittleParser#decl.
    def enterDecl(self, ctx:LittleParser.DeclContext):
        pass

    # Exit a parse tree produced by LittleParser#decl.
    def exitDecl(self, ctx:LittleParser.DeclContext):
        pass


    # Enter a parse tree produced by LittleParser#strt.
    def enterStrt(self, ctx:LittleParser.StrtContext):
        pass

    # Exit a parse tree produced by LittleParser#strt.
    def exitStrt(self, ctx:LittleParser.StrtContext):
        pass


    # Enter a parse tree produced by LittleParser#var_decl.
    def enterVar_decl(self, ctx:LittleParser.Var_declContext):
        pass

    # Exit a parse tree produced by LittleParser#var_decl.
    def exitVar_decl(self, ctx:LittleParser.Var_declContext):
        pass


    # Enter a parse tree produced by LittleParser#var_type.
    def enterVar_type(self, ctx:LittleParser.Var_typeContext):
        pass

    # Exit a parse tree produced by LittleParser#var_type.
    def exitVar_type(self, ctx:LittleParser.Var_typeContext):
        pass


    # Enter a parse tree produced by LittleParser#any_type.
    def enterAny_type(self, ctx:LittleParser.Any_typeContext):
        pass

    # Exit a parse tree produced by LittleParser#any_type.
    def exitAny_type(self, ctx:LittleParser.Any_typeContext):
        pass


    # Enter a parse tree produced by LittleParser#id_list.
    def enterId_list(self, ctx:LittleParser.Id_listContext):
        pass

    # Exit a parse tree produced by LittleParser#id_list.
    def exitId_list(self, ctx:LittleParser.Id_listContext):
        pass


    # Enter a parse tree produced by LittleParser#id_tail.
    def enterId_tail(self, ctx:LittleParser.Id_tailContext):
        pass

    # Exit a parse tree produced by LittleParser#id_tail.
    def exitId_tail(self, ctx:LittleParser.Id_tailContext):
        pass


    # Enter a parse tree produced by LittleParser#param_decl_list.
    def enterParam_decl_list(self, ctx:LittleParser.Param_decl_listContext):
        pass

    # Exit a parse tree produced by LittleParser#param_decl_list.
    def exitParam_decl_list(self, ctx:LittleParser.Param_decl_listContext):
        pass


    # Enter a parse tree produced by LittleParser#param_decl.
    def enterParam_decl(self, ctx:LittleParser.Param_declContext):
        pass

    # Exit a parse tree produced by LittleParser#param_decl.
    def exitParam_decl(self, ctx:LittleParser.Param_declContext):
        pass


    # Enter a parse tree produced by LittleParser#param_decl_tail.
    def enterParam_decl_tail(self, ctx:LittleParser.Param_decl_tailContext):
        pass

    # Exit a parse tree produced by LittleParser#param_decl_tail.
    def exitParam_decl_tail(self, ctx:LittleParser.Param_decl_tailContext):
        pass


    # Enter a parse tree produced by LittleParser#func_declarations.
    def enterFunc_declarations(self, ctx:LittleParser.Func_declarationsContext):
        pass

    # Exit a parse tree produced by LittleParser#func_declarations.
    def exitFunc_declarations(self, ctx:LittleParser.Func_declarationsContext):
        pass

    # Enter a parse tree produced by LittleParser#func_body.
    def enterFunc_body(self, ctx:LittleParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by LittleParser#func_body.
    def exitFunc_body(self, ctx:LittleParser.Func_bodyContext):
        pass
    # Enter a parse tree produced by LittleParser#base_stmt.
    def enterBase_stmt(self, ctx:LittleParser.Base_stmtContext):
        pass

    # Exit a parse tree produced by LittleParser#base_stmt.
    def exitBase_stmt(self, ctx:LittleParser.Base_stmtContext):
        pass


    # Enter a parse tree produced by LittleParser#assign_stmt.
    def enterAssign_stmt(self, ctx:LittleParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by LittleParser#assign_stmt.
    def exitAssign_stmt(self, ctx:LittleParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by LittleParser#return_stmt.
    def enterReturn_stmt(self, ctx:LittleParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by LittleParser#return_stmt.
    def exitReturn_stmt(self, ctx:LittleParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by LittleParser#factor.
    def enterFactor(self, ctx:LittleParser.FactorContext):
        pass

    # Exit a parse tree produced by LittleParser#factor.
    def exitFactor(self, ctx:LittleParser.FactorContext):
        pass


    # Enter a parse tree produced by LittleParser#factor_prefix.
    def enterFactor_prefix(self, ctx:LittleParser.Factor_prefixContext):
        pass

    # Exit a parse tree produced by LittleParser#factor_prefix.
    def exitFactor_prefix(self, ctx:LittleParser.Factor_prefixContext):
        pass


    # Enter a parse tree produced by LittleParser#postfix_expr.
    def enterPostfix_expr(self, ctx:LittleParser.Postfix_exprContext):
        pass

    # Exit a parse tree produced by LittleParser#postfix_expr.
    def exitPostfix_expr(self, ctx:LittleParser.Postfix_exprContext):
        pass


    # Enter a parse tree produced by LittleParser#call_expr.
    def enterCall_expr(self, ctx:LittleParser.Call_exprContext):
        pass

    # Exit a parse tree produced by LittleParser#call_expr.
    def exitCall_expr(self, ctx:LittleParser.Call_exprContext):
        pass


    # Enter a parse tree produced by LittleParser#expr_list.
    def enterExpr_list(self, ctx:LittleParser.Expr_listContext):
        pass

    # Exit a parse tree produced by LittleParser#expr_list.
    def exitExpr_list(self, ctx:LittleParser.Expr_listContext):
        pass


    # Enter a parse tree produced by LittleParser#expr_list_tail.
    def enterExpr_list_tail(self, ctx:LittleParser.Expr_list_tailContext):
        pass

    # Exit a parse tree produced by LittleParser#expr_list_tail.
    def exitExpr_list_tail(self, ctx:LittleParser.Expr_list_tailContext):
        pass


    # Enter a parse tree produced by LittleParser#primary.
    def enterPrimary(self, ctx:LittleParser.PrimaryContext):
        pass

    # Exit a parse tree produced by LittleParser#primary.
    def exitPrimary(self, ctx:LittleParser.PrimaryContext):
        pass


    # Enter a parse tree produced by LittleParser#mulop.
    def enterMulop(self, ctx:LittleParser.MulopContext):
        pass

    # Exit a parse tree produced by LittleParser#mulop.
    def exitMulop(self, ctx:LittleParser.MulopContext):
        pass
    # Enter a parse tree produced by LittleParser#cond.
    def enterCond(self, ctx:LittleParser.CondContext):
        pass

    # Exit a parse tree produced by LittleParser#cond.
    def exitCond(self, ctx:LittleParser.CondContext):
        pass


    # Enter a parse tree produced by LittleParser#compop.
    def enterCompop(self, ctx:LittleParser.CompopContext):
        pass

    # Exit a parse tree produced by LittleParser#compop.
    def exitCompop(self, ctx:LittleParser.CompopContext):
        pass

