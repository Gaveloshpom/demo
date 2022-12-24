from setuptools import setup, find_namespace_packages

setup(
    name='Demo',
    version='1.0',
    packages=find_namespace_packages(),
    #package_dir={'': 'pabot'},
    url='https://github.com/StasStryzhakov/GoIT-8.git',
    license='',
    author='GoIT Team-8',
    author_email='',
    description='',
    entry_points={'console_scripts': ['paboot = pabot.pabot:main']},
    include_package_data = True,
    zip_safe = True,

)
