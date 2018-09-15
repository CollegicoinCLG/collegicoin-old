from distutils.core import setup
setup(name='CLGspendfrom',
      version='1.0',
      description='Command-line utility for collegicoin "coin control"',
      author='Gavin Andresen',
      author_email='gavin@collegicoinfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
