import nbformat
from nbformat.v4 import new_notebook

def clean_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # Clean cells
    for cell in notebook.cells:
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'execution_count' in cell:
            cell['execution_count'] = None
        if 'metadata' in cell:
            cell['metadata'] = {}

    # Clean notebook metadata
    if 'metadata' in notebook:
        notebook['metadata'] = {}

    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)


if __name__ == "__main__":
    import os

    # Change this to the directory containing your notebooks
    notebook_dir = '../../'

    for root, dirs, files in os.walk(notebook_dir):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                clean_notebook(file_path)
                print(f'Cleaned {file_path}')
