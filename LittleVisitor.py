# Generated from /home/ubuntu/Little.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LittleParser import LittleParser
else:
    from LittleParser import LittleParser

# This class defines a complete generic visitor for a parse tree produced by LittleParser.

class LittleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LittleParser#empty.
    def visitEmpty(self, ctx:LittleParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#program.
    def visitProgram(self, ctx:LittleParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#ident.
    def visitIdent(self, ctx:LittleParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#pgm_body.
    def visitPgm_body(self, ctx:LittleParser.Pgm_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#decl.
    def visitDecl(self, ctx:LittleParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#string_decl.
    def visitString_decl(self, ctx:LittleParser.String_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#strt.
    def visitStrt(self, ctx:LittleParser.StrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#var_decl.
    def visitVar_decl(self, ctx:LittleParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#var_type.
    def visitVar_type(self, ctx:LittleParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#any_type.
    def visitAny_type(self, ctx:LittleParser.Any_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#id_list.
    def visitId_list(self, ctx:LittleParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#id_tail.
    def visitId_tail(self, ctx:LittleParser.Id_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#param_decl_list.
    def visitParam_decl_list(self, ctx:LittleParser.Param_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#param_decl.
    def visitParam_decl(self, ctx:LittleParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#param_decl_tail.
    def visitParam_decl_tail(self, ctx:LittleParser.Param_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#func_declarations.
    def visitFunc_declarations(self, ctx:LittleParser.Func_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#func_decl.
    def visitFunc_decl(self, ctx:LittleParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#func_body.
    def visitFunc_body(self, ctx:LittleParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#stmt_list.
    def visitStmt_list(self, ctx:LittleParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#stmt.
    def visitStmt(self, ctx:LittleParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#base_stmt.
    def visitBase_stmt(self, ctx:LittleParser.Base_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#assign_stmt.
    def visitAssign_stmt(self, ctx:LittleParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#assign_expr.
    def visitAssign_expr(self, ctx:LittleParser.Assign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#read_stmt.
    def visitRead_stmt(self, ctx:LittleParser.Read_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#write_stmt.
    def visitWrite_stmt(self, ctx:LittleParser.Write_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#return_stmt.
    def visitReturn_stmt(self, ctx:LittleParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#expr.
    def visitExpr(self, ctx:LittleParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#expr_prefix.
    def visitExpr_prefix(self, ctx:LittleParser.Expr_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#factor.
    def visitFactor(self, ctx:LittleParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#factor_prefix.
    def visitFactor_prefix(self, ctx:LittleParser.Factor_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#postfix_expr.
    def visitPostfix_expr(self, ctx:LittleParser.Postfix_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#call_expr.
    def visitCall_expr(self, ctx:LittleParser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#expr_list.
    def visitExpr_list(self, ctx:LittleParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#expr_list_tail.
    def visitExpr_list_tail(self, ctx:LittleParser.Expr_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#primary.
    def visitPrimary(self, ctx:LittleParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#addop.
    def visitAddop(self, ctx:LittleParser.AddopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#mulop.
    def visitMulop(self, ctx:LittleParser.MulopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#if_stmt.
    def visitIf_stmt(self, ctx:LittleParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#else_part.
    def visitElse_part(self, ctx:LittleParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#cond.
    def visitCond(self, ctx:LittleParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#compop.
    def visitCompop(self, ctx:LittleParser.CompopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleParser#while_stmt.
    def visitWhile_stmt(self, ctx:LittleParser.While_stmtContext):
        return self.visitChildren(ctx)



del LittleParser
