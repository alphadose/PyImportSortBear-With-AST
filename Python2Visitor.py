# Generated from Python2.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python2Parser import Python2Parser
else:
    from Python2Parser import Python2Parser

# This class defines a complete generic visitor for a parse tree produced by Python2Parser.

class Python2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Python2Parser#single_input.
    def visitSingle_input(self, ctx:Python2Parser.Single_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#file_input.
    def visitFile_input(self, ctx:Python2Parser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#eval_input.
    def visitEval_input(self, ctx:Python2Parser.Eval_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#decorator.
    def visitDecorator(self, ctx:Python2Parser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#decorators.
    def visitDecorators(self, ctx:Python2Parser.DecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#decorated.
    def visitDecorated(self, ctx:Python2Parser.DecoratedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#funcdef.
    def visitFuncdef(self, ctx:Python2Parser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#parameters.
    def visitParameters(self, ctx:Python2Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#varargslist.
    def visitVarargslist(self, ctx:Python2Parser.VarargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#fpdef.
    def visitFpdef(self, ctx:Python2Parser.FpdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#fplist.
    def visitFplist(self, ctx:Python2Parser.FplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#stmt.
    def visitStmt(self, ctx:Python2Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#simple_stmt.
    def visitSimple_stmt(self, ctx:Python2Parser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#small_stmt.
    def visitSmall_stmt(self, ctx:Python2Parser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#expr_stmt.
    def visitExpr_stmt(self, ctx:Python2Parser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#augassign.
    def visitAugassign(self, ctx:Python2Parser.AugassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#print_stmt.
    def visitPrint_stmt(self, ctx:Python2Parser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#del_stmt.
    def visitDel_stmt(self, ctx:Python2Parser.Del_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#pass_stmt.
    def visitPass_stmt(self, ctx:Python2Parser.Pass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#flow_stmt.
    def visitFlow_stmt(self, ctx:Python2Parser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#break_stmt.
    def visitBreak_stmt(self, ctx:Python2Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:Python2Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#return_stmt.
    def visitReturn_stmt(self, ctx:Python2Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#yield_stmt.
    def visitYield_stmt(self, ctx:Python2Parser.Yield_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#raise_stmt.
    def visitRaise_stmt(self, ctx:Python2Parser.Raise_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#import_stmt.
    def visitImport_stmt(self, ctx:Python2Parser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#import_name.
    def visitImport_name(self, ctx:Python2Parser.Import_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#import_from.
    def visitImport_from(self, ctx:Python2Parser.Import_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#import_as_name.
    def visitImport_as_name(self, ctx:Python2Parser.Import_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#dotted_as_name.
    def visitDotted_as_name(self, ctx:Python2Parser.Dotted_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#import_as_names.
    def visitImport_as_names(self, ctx:Python2Parser.Import_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#dotted_as_names.
    def visitDotted_as_names(self, ctx:Python2Parser.Dotted_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#dotted_name.
    def visitDotted_name(self, ctx:Python2Parser.Dotted_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#global_stmt.
    def visitGlobal_stmt(self, ctx:Python2Parser.Global_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#exec_stmt.
    def visitExec_stmt(self, ctx:Python2Parser.Exec_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#assert_stmt.
    def visitAssert_stmt(self, ctx:Python2Parser.Assert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#compound_stmt.
    def visitCompound_stmt(self, ctx:Python2Parser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#if_stmt.
    def visitIf_stmt(self, ctx:Python2Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#while_stmt.
    def visitWhile_stmt(self, ctx:Python2Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#for_stmt.
    def visitFor_stmt(self, ctx:Python2Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#try_stmt.
    def visitTry_stmt(self, ctx:Python2Parser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#with_stmt.
    def visitWith_stmt(self, ctx:Python2Parser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#with_item.
    def visitWith_item(self, ctx:Python2Parser.With_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#except_clause.
    def visitExcept_clause(self, ctx:Python2Parser.Except_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#suite.
    def visitSuite(self, ctx:Python2Parser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#testlist_safe.
    def visitTestlist_safe(self, ctx:Python2Parser.Testlist_safeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#old_test.
    def visitOld_test(self, ctx:Python2Parser.Old_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#old_lambdef.
    def visitOld_lambdef(self, ctx:Python2Parser.Old_lambdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#test.
    def visitTest(self, ctx:Python2Parser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#or_test.
    def visitOr_test(self, ctx:Python2Parser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#and_test.
    def visitAnd_test(self, ctx:Python2Parser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#not_test.
    def visitNot_test(self, ctx:Python2Parser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#comparison.
    def visitComparison(self, ctx:Python2Parser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#comp_op.
    def visitComp_op(self, ctx:Python2Parser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#expr.
    def visitExpr(self, ctx:Python2Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#xor_expr.
    def visitXor_expr(self, ctx:Python2Parser.Xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#and_expr.
    def visitAnd_expr(self, ctx:Python2Parser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#shift_expr.
    def visitShift_expr(self, ctx:Python2Parser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#arith_expr.
    def visitArith_expr(self, ctx:Python2Parser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#term.
    def visitTerm(self, ctx:Python2Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#factor.
    def visitFactor(self, ctx:Python2Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#power.
    def visitPower(self, ctx:Python2Parser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#atom.
    def visitAtom(self, ctx:Python2Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#listmaker.
    def visitListmaker(self, ctx:Python2Parser.ListmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#testlist_comp.
    def visitTestlist_comp(self, ctx:Python2Parser.Testlist_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#lambdef.
    def visitLambdef(self, ctx:Python2Parser.LambdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#trailer.
    def visitTrailer(self, ctx:Python2Parser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#subscriptlist.
    def visitSubscriptlist(self, ctx:Python2Parser.SubscriptlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#subscript.
    def visitSubscript(self, ctx:Python2Parser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#sliceop.
    def visitSliceop(self, ctx:Python2Parser.SliceopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#exprlist.
    def visitExprlist(self, ctx:Python2Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#testlist.
    def visitTestlist(self, ctx:Python2Parser.TestlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx:Python2Parser.DictorsetmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#classdef.
    def visitClassdef(self, ctx:Python2Parser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#arglist.
    def visitArglist(self, ctx:Python2Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#argument.
    def visitArgument(self, ctx:Python2Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#list_iter.
    def visitList_iter(self, ctx:Python2Parser.List_iterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#list_for.
    def visitList_for(self, ctx:Python2Parser.List_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#list_if.
    def visitList_if(self, ctx:Python2Parser.List_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#comp_iter.
    def visitComp_iter(self, ctx:Python2Parser.Comp_iterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#comp_for.
    def visitComp_for(self, ctx:Python2Parser.Comp_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#comp_if.
    def visitComp_if(self, ctx:Python2Parser.Comp_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#testlist1.
    def visitTestlist1(self, ctx:Python2Parser.Testlist1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#encoding_decl.
    def visitEncoding_decl(self, ctx:Python2Parser.Encoding_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python2Parser#yield_expr.
    def visitYield_expr(self, ctx:Python2Parser.Yield_exprContext):
        return self.visitChildren(ctx)



del Python2Parser