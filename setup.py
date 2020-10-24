from setuptools import setup


setup(name='fixer-demo',
      version='0.2',
      description='Fixer service demo package',
      url='https://gitlab.com/7learn-py-web/fixer-demo',
      author='Hosein',
      author_email='hosein@inprobes.com',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)