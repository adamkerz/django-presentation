from setuptools import setup,find_packages


with open('django_presentation/version.py') as fin: exec(fin)

setup(
    name='django-presentation',
    version=__version__,

    packages=find_packages(exclude=['tests*']),
    
    # dependencies
    install_requires=['django'],
    
    # PyPI MetaData
    author='Adam Kerz',
    author_email='github@kerz.id.au',
    description='Adding some presentation functionality to the Python side of Django',
    license='BSD 3-Clause',
    keywords='django',
    url='http://github.com/adamkerz/django-presentation',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ),

    zip_safe=False
)
