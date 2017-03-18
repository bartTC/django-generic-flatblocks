from setuptools import setup, find_packages

long_description = u'\n\n'.join((
    open('README.rst').read(),
    open('CHANGELOG.rst').read()
))

setup(
    name='django-generic-flatblocks',
    version='1.1',
    description='A flatpages/flatblock application using generic relations to content models.',
    long_description=long_description,
    author='Martin Mahner',
    author_email='martin@mahner.org',
    url='http://github.com/bartTC/django-generic-flatblocks/',
    packages=find_packages(exclude=[
        'example_project',
        'example_project.*'
    ]),
    package_data={
        'django_generic_flatblocks': ['templates/*.*', 'contrib/gblocks/templates/*.*'],
        'docs': ['*'],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=[
        'django>=1.8',
    ],
)
