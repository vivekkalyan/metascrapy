from setuptools import setup

setup(name='metascrapy',
      version='0.3',
      description='Scrapes meta data from a link with python',
      url='https://github.com/bowsplinter/metascrapy',
      author='Vivek Kalyan',
      author_email='vivekkalyansk@gmail.com',
      license='MIT',
      packages=['metascrapy'],
      install_requires=[
          'requests',
          'beautifulsoup4'
      ],
      zip_safe=False)