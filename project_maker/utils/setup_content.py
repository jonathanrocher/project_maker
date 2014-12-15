setup_content = """
from setuptools import find_packages, setup

setup(
    name='%s',
    version='%s',
    author='Enthought Inc.',
    author_email='info@enthought.com',
    license='%s',
    url='http://www.enthought.com',
    description='%s',

    ext_modules=[],
    packages=find_packages(),
    requires=[],
    package_data={},
    cmdclass={},
    entry_points = {
        'console_scripts': [],
      },
    include_package_data = True,
)
"""
