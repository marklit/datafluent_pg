import os
from   setuptools import setup


dir_path = os.path.dirname(os.path.realpath(__file__))

_read = lambda filename: open(os.path.join(dir_path, filename)).read()

setup(name='datafluent',
      version=_read('VERSION'),
      description='Build a better understanding of your data in PostgreSQL.',
      long_description=_read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/marklit/datafluent_pg',
      project_urls={
        "Bug Tracker": "https://github.com/marklit/datafluent_pg/issues",
        "Documentation": "https://datafluent.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/marklit/datafluent_pg",
      },
      author='Mark Litwintschik',
      author_email='mark@marksblogg.com',
      license='MIT',
      packages=['datafluent'],
      scripts=['bin/datafluent',],
      install_requires=[
        "humanfriendly",
        "Pandas",
        "psycopg2-binary",
        "SQLAlchemy",
        "typer",
        "xlsxwriter",
      ],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Topic :: Scientific/Engineering :: Information Analysis',
        ],
      zip_safe=False)
