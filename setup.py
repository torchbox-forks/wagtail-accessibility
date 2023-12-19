#!/usr/bin/env python
"""
Install wagtail-accessibility using setuptools
"""

with open('README.rst', 'r') as f:
    readme = f.read()

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='wagtail-accessibility',
    version='1.0.0',
    description="A plugin to assist with accessibility when developing in Wagtail.",
    long_description=readme,
    author='Wagtail Nest contributors',
    author_email='hello@wagtail.org',
    url='https://github.com/takeflight/wagtail-accessibility',

    install_requires=[
        'wagtail>=1.0',
    ],
    zip_safe=False,
    license='BSD License',

    packages=find_packages(),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)
