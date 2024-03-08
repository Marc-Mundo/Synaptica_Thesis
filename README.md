# LaTeX thesis project: README.md

This is a LaTeX template for a thesis or dissertation. It is based on the [Radboud University (FNWI): Thesis template](https://www.overleaf.com/latex/templates/radboud-university-fnwi-thesis-template/wnzqzqjxjzjv) and the PhD dissertation of Arthogrul Ayashbali which is published on Github as a template at <https://github.com/suchow/Dissertate>.

## Overview of TeX files

The following is a brief overview of the files in this project:

- `thesis.tex`: Main file, includes all other files.
- `thesis.bib`: Bibliography file.
- `chapters/`: Folder containing all chapters.
- `images/`: Folder containing all figures.

## Compilation

The recipe is as follows: pdflatex -> biber -> pdflatex -> pdflatex

To compile the document and run the tex file, follow these steps:

```bash
```powershell
1. Install LaTeX distribution (e.g., TeX Live or MiKTeX).
2. Open a terminal or command prompt.
3. Navigate to the directory where `thesis.tex` is located.
4. Run the command `pdflatex thesis.tex` to generate the PDF output.
5. If there are any references, run `bibtex thesis` to generate the bibliography.
6. Run `pdflatex thesis.tex` again to update the references in the PDF.
7. Repeat steps 5 and 6 until all references are resolved.
8. The final portable document format output will be generated as `thesis.pdf` in the same directory.
```

## Ownership

This project was produced by [Marc J. Posthuma] Master's Student Neurobiology at the Radboud University, Nijmegen, The Netherlands (2023-2024).
