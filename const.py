import ast
import traceback
import sys
from types import TracebackType


frame = sys._getframe(1)
while "importlib" in frame.f_code.co_filename:
    if frame.f_back is None:
        raise RuntimeError
    frame = frame.f_back


class Poo(ast.NodeVisitor):
    def __init__(self):
        self.seen = set()
        super().__init__()

    def visit_Assign(self, node):

        for ass in node.targets:
            ident = ass.id

            if ident.isupper():

                if ident in self.seen:
                    try:
                        tb = TracebackType(tb_next=None,
                                                    tb_frame=frame,
                                                    tb_lasti=0, # rekt
                                                    tb_lineno=node.lineno)
                        raise SyntaxError("get const'd lol").with_traceback(tb)

                    except:
                        traceback.print_exc(limit=2)
                        sys.exit(1)

                else:
                    self.seen.add(ident)



with open(frame.f_code.co_filename) as code:
    tree = ast.parse(code.read())
    visitor = Poo()
    for b in tree.body:
        visitor.visit(b)
