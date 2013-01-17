from distutils.core import setup

setup(
    name='django-dynsettings',
    version='0.1.0',
    author='Igor Campbell',
    author_email='igorcamp@gmail.com',
    packages=['dynsettings', ],
    license='LICENSE.txt',
    description='Django Dynamic Settings',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.1",
    ],
)