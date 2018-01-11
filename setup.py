import os

from setuptools import setup, find_packages

print('Please install pytest(https://docs.pytest.org/en/latest/contents.html) as test suite.')
DESCRIPTION = "A python module for rspmsg"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass


def get_version(version_tuple):
    version = '%s.%s' % (version_tuple[0], version_tuple[1])
    if version_tuple[2]:
        version = '%s.%s' % (version, version_tuple[2])
    return version


init = os.path.join(os.path.dirname(__file__), 'rspmsg', '__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
VERSION = get_version(eval(version_line.split('=')[-1]))
print('version: %s' % VERSION)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name='rspmsg',
      version=VERSION,
      packages=find_packages(),
      author='darkdarkfruit',
      author_email='darkdarkfruit@gmail.com',
      url='https://github.com/darkdarkfruit/rspmsg',
      license='MIT',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=CLASSIFIERS,
      install_requires=[],
      )
