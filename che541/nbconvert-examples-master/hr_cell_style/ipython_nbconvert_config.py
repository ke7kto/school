c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['*.ipynb']
c.NbConvertApp.export_format = 'latex'
c.NbConvertApp.postprocessor_class = 'PDF'

c.Exporter.template_file = 'my_output.tplx'
