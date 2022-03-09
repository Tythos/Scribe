@echo off
REM builds the contents of main.rst into a PDF
python rst2tex.py < main.rst > main.tex
pdflatex main.tex
sumatrapdf main.pdf
