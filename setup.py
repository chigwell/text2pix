from setuptools import setup, find_packages

setup(
    name='text2pix',
    version='2025.05.100903',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='A library to generate images from text descriptions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/text2pix',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
