import docutils.parsers.rst.directives
import sphinx.util.compat
from docutils import nodes

class Comment(sphinx.util.compat.Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = True

    def run(self):
        return []

def setup(Sphinx):
    Sphinx.add_directive('comment', Comment)
