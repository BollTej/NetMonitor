from setuptools import setup, find_packages

setup(
    name='NetMonitor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'scapy',
        'pandas',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'network_analysis=NetMonitor.main:main'
        ]
    },
    author='NetMonitor',
    author_email='phanisaidivyatej@gmail.com',
    description='A package for network performance analysis and visualization',
    license='MIT',
    keywords='network analysis performance visualization',
    url='http://github.com/BollTej/NetMonitor',
)
