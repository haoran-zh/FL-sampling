from setuptools import setup, find_packages

setup(
    name='Fl-sampling',
    version='0.1',
    packages=find_packages(),
    description='A Python package for client sampling in federated learning. The package supports multiple sampling methods. ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Haoran Zhang, Zejun Gong',
    author_email='haoranz5@andrew.cmu.edu, ',
    url='https://github.com/haoran-zh/FL-sampling',
    install_requires=[
        'numpy>=1.14.5',

    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)