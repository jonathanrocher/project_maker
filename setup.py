
from setuptools import find_packages, setup

setup(
    name='project_maker',
    version='0.1dev',
    author='Enthought Inc.',
    author_email='info@enthought.com',
    license='proprietary',
    url='http://www.enthought.com',
    description='Tool to create a project from scratch: tree structure, CI tools, environment tools, ...',

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
