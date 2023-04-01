import ast
import sys
import traceback
from types import TracebackType


frame = sys._getframe(1)
while "importlib" in frame.f_code.co_filename:
    if frame.f_back is None:
        raise RuntimeError
    frame = frame.f_back


class ConstHunter(ast.NodeVisitor):
    def __init__(self):
        self.seen = set()
        super().__init__()


    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store) and node.id.isupper():
            if node.id in self.seen:
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
                self.seen.add(node.id)


with open(frame.f_code.co_filename) as code:
    tree = ast.parse(code.read())
    visitor = ConstHunter()

    for node in tree.body:
        visitor.visit(node)
