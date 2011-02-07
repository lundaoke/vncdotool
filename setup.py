#!/usr/bin/env python

from distutils.core import setup

setup(
    name='vncdotool',
    version='0.1.0dev',
    description='Send keyboard and mouse events to a VNC server from the command line',
    install_requires=[
        'Twisted',
    ],
    test_requires=[
        'nose',
    ],
    url='http://github.com/sibson/vncdotool',
    author='Marc Sibson',
    author_email='sibson+vncdotool@gmail.com',
    download_url='',

    scripts=['scripts/vncdotool'],
    packages=['vncdotool'],

    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Framework :: Twisted',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Multimedia :: Graphics :: Viewers',
          'Topic :: Software Development :: Testing',
    ],

    long_description='',
)
