"""
JAVA interpreter
"""
from __future__ import print_function
import __future__
# clara lib imports
from .interpreter import Interpreter, addlanginter, RuntimeErr, UndefValue

class JavaInterpreter(Interpreter):

    # TODO
    pass

# Register JAVA interpreter
addlanginter('java', JavaInterpreter)
