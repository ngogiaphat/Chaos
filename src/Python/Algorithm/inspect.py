import inspect
import ast
import astunparse
# get back the source code
astunparse.unparse(ast.parse(inspect.getsource(ast)))
# get a pretty-printed dump of the AST
astunparse.dump(ast.parse(inspect.getsource(ast)))