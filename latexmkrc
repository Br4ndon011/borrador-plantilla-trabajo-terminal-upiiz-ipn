# ==============================================================================
# Configuración de latexmk para Plantilla Institucional Trabajo Terminal UPIIZ-IPN
# ==============================================================================

# Motor de compilación por defecto: XeLaTeX (modo 5) o LuaLaTeX (modo 4)
# Ambos motores soportan de forma nativa la tipografía institucional Arial y UTF-8.
$pdf_mode = 5;
$xelatex = 'xelatex -interaction=nonstopmode -synctex=1 %O %S';
$lualatex = 'lualatex -interaction=nonstopmode -synctex=1 %O %S';

# Procesador de bibliografía BibTeX
$bibtex = 'bibtex %O %B';

# Extensiones de archivos temporales que se limpian con `latexmk -c` o `latexmk -C`
$clean_ext = 'aux log out toc lof lot bbl blg fls fdb_latexmk synctex.gz run.xml bcf xdv nav snm vrb';
