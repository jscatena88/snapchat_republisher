try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description='Snapchat Republisher',
    author='Jason Scatena',
    url='https://github.com/jscatena88/snapchat_republisher',
    author_email='jscatena88 [AT] gmail.com',
    version='0.01',
    install_requires=['pysnap'],
    name='snapchat_republisher',
    packages=['snapchat_republisher'],
    scripts=['bin/updateStory.py'],
    license=open('LICENSE').read()
)
