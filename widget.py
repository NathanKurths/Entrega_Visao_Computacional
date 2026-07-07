import nbformat

arquivo = "../G2_notebook1_Visao_classica.ipynb"

nb = nbformat.read(arquivo, as_version=4)

nb.metadata.pop("widgets", None)

nbformat.write(nb, arquivo)

print("Concluído.")