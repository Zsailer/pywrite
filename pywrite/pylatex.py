import os, glob, subprocess

def assume_relpath():
    """ Decorator to catch path, make it absolute either way."""
    pass

def list_tex(path):
    """ List all latex files """
    tex_files = glob.glob(path + "*.tex")
    return tex_files

def preview_pdf(path):
    """ Preview a pdf with default pdf viewer. """
    command = ["open", path]
    subprocess.call(command)

def compile_latex(path, bib=False):
    """ Compile the latex files. """
    path, ext = os.path.splitext(path)

    # Compile PDF
    command1 = ["pdflatex", path + ext]
    code = subprocess.call(command1)

    # Compile bibliograph if given
    if bib:
        command2 = ["bibtex", path + ".bib"]
        subprocess.call(command2)

        # Call first command again to make sure bibliography
        # is properly added
        subprocess.call(command1)
        subprocess.call(command1)

def remove_aux(path):
    """ Remove the annoying latex files from compilation. """
    path, ext = os.path.splitext(path)

    # List of extensions.
    exts = [".aux", ".log", ".synctex.gz"]

    # Remove annoying files
    for e in exts:
        try:
            os.remove(path + e)
        except FileNotFoundError:
            pass
