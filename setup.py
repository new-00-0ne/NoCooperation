from cx_Freeze import setup,Executable

includefiles = []
includes = []
excludes = []
packages = []

setup(
    name = 'myapp',
    version = '0.1',
    description = 'A general enhancement utility',
    author = 'lenin',
    author_email = 'le...@null.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('main.py', 'application.py', 'BigDict.py', 'entity.py', 'gui_manager.py', 'idevice.py', 'math2d.py', 'pane.py', 'soundDataBase.py', 'spriteDataBase.py', 'world.py')]
)
