grammar Little;

// First line of this file must be the grammar name.
// So, please keep the first line as it is provided.
// Please write your grammar below this line.

/* Parser Rules */

/* Program */
empty : ;
program: 'PROGRAM' ident 'BEGIN' pgm_body 'END' ;
ident: IDENTIFIER ;
pgm_body: decl func_declarations ;
decl: string_decl decl
    | var_decl decl
    | empty ;

/* Global String Declaration */
string_decl: 'STRING' ident ':=' strt ';' ;
strt: STRINGLITERAL ;

/* Variable Declaration */
var_decl: var_type id_list ';' ;
var_type: 'FLOAT'
    | 'INT' ;
any_type: var_type
    | 'VOID'  ;
id_list: ident id_tail ;
id_tail: ',' ident id_tail
    | empty ;

/* Function Paramater List */
param_decl_list: param_decl param_decl_tail
    | empty ;
param_decl: var_type ident ;
param_decl_tail: ',' param_decl param_decl_tail
    | empty ;

/* Function Declarations */
func_declarations: func_decl func_declarations
    | empty ;
func_decl: 'FUNCTION' any_type ident '(' param_decl_list ')' 'BEGIN' func_body 'END' ;
func_body: decl stmt_list  ;

/* Statement List */
stmt_list: stmt stmt_list
    | empty ;
stmt: base_stmt
    | if_stmt
    | while_stmt ;
base_stmt: assign_stmt
    | read_stmt
    | write_stmt
    | return_stmt ;

/* Basic Statements */
assign_stmt: assign_expr ';' ;
assign_expr: ident ':=' expr ;
read_stmt: 'READ' '(' id_list ')' ';' ;
write_stmt: 'WRITE' '(' id_list ')' ';' ;
return_stmt: 'RETURN' expr ';' ;

/* Expressions */
expr: expr_prefix factor ;
expr_prefix: expr_prefix factor addop
    | empty ;
factor: factor_prefix postfix_expr ;
factor_prefix: factor_prefix postfix_expr mulop
    | empty ;
postfix_expr: primary
    | call_expr ;
call_expr: ident '(' expr_list ')' ;
expr_list: expr expr_list_tail
    | empty ;
expr_list_tail: ',' expr expr_list_tail
    | empty ;
primary: '(' expr ')'
    | ident
    | INTLITERAL
    | FLOATLITERAL ;
addop: '+'
    | '-' ;
mulop: '*'
    | '/' ;

/* Complex Statements and Condition */
if_stmt: 'IF' '(' cond ')' decl stmt_list else_part 'ENDIF' ;
else_part: 'ELSE' decl stmt_list
    | empty ;
cond: expr compop expr ;
compop: '<'
    | '>'
    | '='
    | '!='
    | '<='
    | '>=' ;

/* While statements */
while_stmt: 'WHILE' '(' cond ')' decl stmt_list 'ENDWHILE' ;


/* Lexer Rules */

FLOATLITERAL:   [0-9]*'.'[0-9]+ ;

INTLITERAL  :   [0-9]+ ;

STRINGLITERAL:  '"'.*?'"' ;

COMMENT     :   ('--').*?('\n') -> skip;

OPERATOR    :   (':=' | '+' | '-' | '*' | '/' | '=' | '!=' | '<' | '>' | '(' | ')' | ';' | ',' | '<=' | '>=') ;

KEYWORD     :   ('PROGRAM' | 'BEGIN' | 'END' | 'FUNCTION' | 'READ' | 'WRITE' | 'IF' | 'ELSE' | 'FI' | 'FOR' | 'ROF' | 'RETURN' | 'INT' | 'VOID' | 'STRING' | 'FLOAT' | 'WHILE' | 'ENDIF' |  'ENDWHILE') ;

IDENTIFIER  :   [A-z]([A-z] | [0-9])* ;

WHITESPACE  :   [ \t\n]+ -> skip ;


