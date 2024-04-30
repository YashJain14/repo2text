from setuptools import setup, find_packages

setup(
    name='repo2text',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'repo2text=repo2text.repo2text:main',
        ],
    },
    author='Yash Jain',
    description='A simple utility to convert repository files to text including specific file extensions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YashJain14/repo2text',
    install_requires=[
        'gitpython>=3.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
