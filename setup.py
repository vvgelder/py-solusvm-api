#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    print("py-solusvm-api needs setuptools in order to build. Install it using"
            " your package manager (usually python-setuptools) or via pip (pip"
            " install setuptools).")
    sys.exit(1)

setup(name='py-solusvm-api',
      version='0.1.0',
      description='Solusvm API',
      author='Vincent van Gelder',
      author_email='vincent@ixlhosting.nl',
      url='http://ixlhosting.nl/',
      license='Apache Software License',
      install_requires=['setuptools'],
      package_dir={ '': 'lib' },
      packages=find_packages('lib'),
      package_data={
         '': [],
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Installation/Setup',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities',
      ],
      scripts=[],
      data_files=[],
)
