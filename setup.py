from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='acaeslanoticia.theme',
      version=version,
      description="Plone Theme for ACA es la Noticia.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone4 theme product acalanoticia website',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/acaeslanoticia/acaeslanoticia.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['acaeslanoticia'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
