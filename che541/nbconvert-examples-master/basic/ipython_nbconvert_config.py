c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['*.ipynb']

#Include dependency files
c.WriterBase.files = ['cats/mycat.jpg',
                      'cats/yourcat.jpg']