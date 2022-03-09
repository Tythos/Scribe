"""
Transcribes an .RST-formatted markup file from STDIN to a .TEX-formatted markup
file to STDOUT.
"""

import sys
from docutils import core

def main():
    """
    Reads raw RST content in from STDIN. It is then transformed, using
    docutils, into TEX markup, which is decoded and printed to STDOUT.
    """
    rawRst = sys.stdin.read()
    rawTex = core.publish_string(rawRst, writer_name="latex")
    print(rawTex.decode())

if __name__ == "__main__":
    main()
