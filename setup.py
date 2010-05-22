from setuptools import setup, find_packages

setup(
    name='django-generic-flatblocks',
    version='0.9.1',
    description='A flatpages/flatblock application using generic relations to content models.',
    long_description=open('README').read(),
    author='Martin Mahner',
    author_email='martin@mahner.org',
    url='http://github.com/bartTC/django-generic-flatblocks/tree/master',
    packages=find_packages(exclude=['example_project', 'example_project.*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
