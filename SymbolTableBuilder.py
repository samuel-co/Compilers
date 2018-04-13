# Generated from /home/ubuntu/Little.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LittleParser import LittleParser
else:
    from LittleParser import LittleParser

# This class defines a complete listener for a parse tree produced by LittleParser.
class SymbolTableBuilder(ParseTreeListener):
    
    def __init__(self):
        self.symbol_table = {}
        self.current_scope = None
        self.scope_order = []
        self.closed_scopes = []
        self.block_count = 0

    # Enter a parse tree produced by LittleParser#empty.
    def enterEmpty(self, ctx:LittleParser.EmptyContext):
        pass

    # Exit a parse tree produced by LittleParser#empty.
    def exitEmpty(self, ctx:LittleParser.EmptyContext):
        pass
    
    def enter_scope(self, name):
        #print("entering scope {}".format(name))
        self.symbol_table[name] = []
        self.current_scope = name
        self.scope_order.append(self.current_scope)
        self.closed_scopes.append(0)
        
    def exit_scope(self):
        #print("closing scope {}".format(self.current_scope))
        #print(self.scope_order)
        # close the current scope (will always be the last open scope in the list)
        for i in reversed(range(len(self.closed_scopes))):
            #print(i)
            # if the scope is open, close it
            if self.closed_scopes[i] == 0:
                #print("closed scope {}".format(self.scope_order[i]))
                self.closed_scopes[i] = 1
                break
        # find the next open scope to return to
        for i in reversed(range(len(self.closed_scopes))):
            if self.closed_scopes[i] == 0:
                #print("entered scope {}".format(self.scope_order[i]))
                self.current_scope = self.scope_order[i]
                break
        
        
    def print_symbol_table(self):
        # check every scopes variable names
        for scope in self.scope_order:
            var_names = [self.symbol_table[scope][var][0] for var in range(len(self.symbol_table[scope]))]
            # check if we have a duplicate name
            if len(var_names) != len(set(var_names)):
                # create an ordered list of the duplicate names we see, then print the first one as an error and return
                duplicates = [n for i , n in enumerate(var_names) if n in var_names[i+1:] and n not in var_names[:i]][0]
                print("DECLARATION ERROR {}".format(duplicates[0]))
                return
        for scope in self.scope_order:
            print("Symbol table " + scope)
            for var in self.symbol_table[scope]:
                if var[2]: print("name {} type {} value {}".format(var[0], var[1], var[2]))
                else: print("name {} type {}".format(var[0], var[1]))
    
    #-------Entering a scope------------------------------------------------------------
    
    # Enter a parse tree produced by LittleParser#program.
    def enterProgram(self, ctx:LittleParser.ProgramContext):
        #print("entering program")
        self.enter_scope("GLOBAL")
        pass
    
    # Enter a parse tree produced by LittleParser#func_decl.
    def enterFunc_decl(self, ctx:LittleParser.Func_declContext):
        #print("entering function")
        self.enter_scope(ctx.ident().getText())
    
    # Enter a parse tree produced by LittleParser#if_stmt.
    def enterIf_stmt(self, ctx:LittleParser.If_stmtContext):
        #print("entering if")
        self.block_count += 1
        self.enter_scope("BLOCK " + (str) (self.block_count))

    # Enter a parse tree produced by LittleParser#else_part.
    def enterElse_part(self, ctx:LittleParser.Else_partContext):
        #print("entering else")
        #print(ctx.empty())
        if not ctx.empty():
            #print("found else")
            self.block_count += 1
            self.enter_scope("BLOCK " + (str) (self.block_count))
    
    # Enter a parse tree produced by LittleParser#while_stmt.
    def enterWhile_stmt(self, ctx:LittleParser.While_stmtContext):
        #print("entering while")
        self.block_count += 1
        self.enter_scope("BLOCK " + (str) (self.block_count))

    #----------End of Scope---------------------------------------------------------

    # Exit a parse tree produced by LittleParser#program.
    def exitProgram(self, ctx:LittleParser.ProgramContext):
        #print("exiting program")
        self.exit_scope()
        pass
    
     # Exit a parse tree produced by LittleParser#func_decl.
    def exitFunc_decl(self, ctx:LittleParser.Func_declContext):
        #print("exiting function")
        self.exit_scope()
        pass

    # Exit a parse tree produced by LittleParser#if_stmt.
    def exitIf_stmt(self, ctx:LittleParser.If_stmtContext):
        #print("exiting if")
        self.exit_scope()
        pass

    # Exit a parse tree produced by LittleParser#else_part.
    def exitElse_part(self, ctx:LittleParser.Else_partContext):
        #print("exiting else")
        if not ctx.empty():
            self.exit_scope()
        pass
    
    # Exit a parse tree produced by LittleParser#while_stmt.
    def exitWhile_stmt(self, ctx:LittleParser.While_stmtContext):
        #print("exiting while")
        self.exit_scope()
        pass
    
    #---------Variable Declarations----------------------------------------------------------
    
    # Enter a parse tree produced by LittleParser#string_decl.
    def enterString_decl(self, ctx:LittleParser.String_declContext):
        self.symbol_table[self.current_scope].append([ctx.ident().getText(), "STRING", ctx.strt().getText()])
        #print(self.symbol_table[self.current_scope][-1])

    # Exit a parse tree produced by LittleParser#string_decl.
    def exitString_decl(self, ctx:LittleParser.String_declContext):
        pass
    
    # Enter a parse tree produced by LittleParser#var_decl.
    def enterVar_decl(self, ctx:LittleParser.Var_declContext):
        #print("Making var")
        id_list = ctx.id_list().getText().split(',')
        for ident in id_list:
            self.symbol_table[self.current_scope].append([ident, ctx.var_type().getText(), None])
            #print(self.symbol_table[self.current_scope][-1])

    # Exit a parse tree produced by LittleParser#var_decl.
    def exitVar_decl(self, ctx:LittleParser.Var_declContext):
        pass
    
    # Enter a parse tree produced by LittleParser#param_decl.
    def enterParam_decl(self, ctx:LittleParser.Param_declContext):
        self.symbol_table[self.current_scope].append([ctx.ident().getText(), ctx.var_type().getText(), None])
        #print(self.symbol_table[self.current_scope][-1])
        pass

    # Exit a parse tree produced by LittleParser#param_decl.
    def exitParam_decl(self, ctx:LittleParser.Param_declContext):
        pass
    
    #---------Other----------------------------------------------------------
    
     # Enter a parse tree produced by LittleParser#var_type.
    def enterVar_type(self, ctx:LittleParser.Var_typeContext):
        pass

    # Exit a parse tree produced by LittleParser#var_type.
    def exitVar_type(self, ctx:LittleParser.Var_typeContext):
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


    # Enter a parse tree produced by LittleParser#stmt_list.
    def enterStmt_list(self, ctx:LittleParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by LittleParser#stmt_list.
    def exitStmt_list(self, ctx:LittleParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by LittleParser#stmt.
    def enterStmt(self, ctx:LittleParser.StmtContext):
        pass

    # Exit a parse tree produced by LittleParser#stmt.
    def exitStmt(self, ctx:LittleParser.StmtContext):
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


    # Enter a parse tree produced by LittleParser#assign_expr.
    def enterAssign_expr(self, ctx:LittleParser.Assign_exprContext):
        pass

    # Exit a parse tree produced by LittleParser#assign_expr.
    def exitAssign_expr(self, ctx:LittleParser.Assign_exprContext):
        pass


    # Enter a parse tree produced by LittleParser#read_stmt.
    def enterRead_stmt(self, ctx:LittleParser.Read_stmtContext):
        pass

    # Exit a parse tree produced by LittleParser#read_stmt.
    def exitRead_stmt(self, ctx:LittleParser.Read_stmtContext):
        pass


    # Enter a parse tree produced by LittleParser#write_stmt.
    def enterWrite_stmt(self, ctx:LittleParser.Write_stmtContext):
        pass

    # Exit a parse tree produced by LittleParser#write_stmt.
    def exitWrite_stmt(self, ctx:LittleParser.Write_stmtContext):
        pass


    # Enter a parse tree produced by LittleParser#return_stmt.
    def enterReturn_stmt(self, ctx:LittleParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by LittleParser#return_stmt.
    def exitReturn_stmt(self, ctx:LittleParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by LittleParser#expr.
    def enterExpr(self, ctx:LittleParser.ExprContext):
        pass

    # Exit a parse tree produced by LittleParser#expr.
    def exitExpr(self, ctx:LittleParser.ExprContext):
        pass


    # Enter a parse tree produced by LittleParser#expr_prefix.
    def enterExpr_prefix(self, ctx:LittleParser.Expr_prefixContext):
        pass

    # Exit a parse tree produced by LittleParser#expr_prefix.
    def exitExpr_prefix(self, ctx:LittleParser.Expr_prefixContext):
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


    # Enter a parse tree produced by LittleParser#addop.
    def enterAddop(self, ctx:LittleParser.AddopContext):
        pass

    # Exit a parse tree produced by LittleParser#addop.
    def exitAddop(self, ctx:LittleParser.AddopContext):
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

