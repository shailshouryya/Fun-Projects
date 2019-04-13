import setuptools 

setuptools.setup( 
    name='caesar', 
    version='1.0', 
    author='Shail Shouryya', 
    author_email='sshouryy@ucsc.edu', 
    description='Hides a message with a Caesar cipher', 
    packages=setuptools.find_packages(), 
    entry_points={ 
        'console_scripts': [ 
            'caesar = caesar.caesar:main' 
        ]# Here we are configuring the command caesar to be related to our main function in our caesar.py script file. Now when we execute our setup.py file it should build and install our script and allow us to access it using the caesar command.
    }, 
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)