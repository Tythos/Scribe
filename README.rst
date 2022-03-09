Scribe
======

Scribe is a basic set of tools that facilitates the transcription of raw RST source into professionally-typset PDF documents.

While this pipeline focuses on the bare-bones transcription supported by docutils (compared to, for example, the fully fleshed-out feature set offered by Sphinx), this is still quite extensive and can give you a powerful array of tools. The "main.rst" file included in this repository endeavours to demonstrate a wide variety of supported features that are successfuly transcribed through TeX to PDF. A full list of docutils-supported RST features can be found here:

  https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

Pipeline
--------

This takes place in three stages, largely defined by the "build.bat" script:

#. First, a Python script ("rst2tex.py") is used to transform RST (from STDIN) into TEX (which is stored in the file "main.tex")

#. The "pdflatex" program is called on "main.tex", which results in a "main.pdf" file

#. This PDF file is then opened in "sumatrapdf" (which we assume is on the system path)

Scripts and Artifacts
---------------------

The "build.bat" script can be called from VS Code using a predefined build task (see ".vscode/tasks.json"). This can be invoked using the hotkeys CTRL+SHIFT+B.

The "clean.bat" script will delete all intermediate and final build artifacts from the working directory. This includs AUX, LOG, PDF, and TEX files, as well as a few others. Note that many of these formats are also included in the ".gitignore" patterns to avoid commiting them to version control.

Customization
-------------

While bare-bones, there are plenty of opportunities for customization:

* The "rst2tex.py" file can be modified to swap out a different document class (a4 article is used by default)

* The intermediate TEX file (main.tex) can be manually modified or loaded into a TEX editor, like TeXworks

* The typesetting calls in "build.bat" can be modified to support multiple passes, in the event that cross-references need to be resolved or other typesetting stages (like bibliography hooks) need to be integrated

* You can, of course, always point "build.bat" to a different RST file (it defaults to "main.rst")
