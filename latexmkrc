# ==============================================================================
# Configuración de latexmk para Plantilla Institucional Trabajo Terminal UPIIZ-IPN
# ==============================================================================

# Motor de compilación oficial por defecto: LuaLaTeX (modo 4)
# Soporta de forma nativa la tipografía institucional Arial y codificación UTF-8.
$pdf_mode = 4;
$postscript_mode = $dvi_mode = 0;
$lualatex = 'lualatex -interaction=nonstopmode -synctex=1 %O %S';

# Procesador de bibliografía: solo ejecutar cuando se detecten citas en el .aux
$bibtex_use = 2;

# Extensiones de archivos temporales que se limpian con `latexmk -c` o `latexmk -C`
$clean_ext = 'aux log out toc lof lot bbl blg fls fdb_latexmk synctex.gz run.xml bcf xdv nav snm vrb';
