import setuptools


setuptools.setup(
    name='developer-tools',
    version='0.0.1',

    author='Max Zheng',
    author_email='maxzheng.os@gmail.com',

    description='Useful tools for Python developers',
    long_description=open('README.rst').read(),

    url='https://github.com/maxzheng/developer-tools',

    install_requires=open('requirements.txt').read(),

    license='MIT',

    packages=setuptools.find_packages(),
    include_package_data=True,

    python_requires='>=3.6',
    setup_requires=['setuptools-git'],

    # entry_points={
    #    'console_scripts': [
    #        'script_name = package.module:entry_callable',
    #    ],
    # },

    # Standard classifiers at https://pypi.org/classifiers/
    classifiers=[
      'Development Status :: 5 - Production/Stable',

      'Intended Audience :: Developers',
      'Topic :: Software Development',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='<KEYWORDS>',
)
