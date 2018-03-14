from setuptools import setup, find_packages

setup(
    name='PyDreamScreen',
    version='0.0.5',
    packages=find_packages(),
    author='digitalhigh',
    author_email='donate.to.digitalhigh@gmail.com',
    description='Python device discovery and manipulation for DreamScreen HD, '
                '4K, and SideKick devices.',
    license='MIT',
    url='https://github.com/d8ahazard/pydreamscreen',
    long_description=open('README.rst').read(),
    include_package_data=True,
    install_requires=list(r.strip() for r in open('requirements.txt')),
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)