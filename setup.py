from setuptools import setup, find_packages

setup(
    name='geospy_defender',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'Pillow',
        'PyQt5',
    ],
    entry_points={
        'console_scripts': [
            'geospy-defender = geospy_defender.__main__:main'
        ]
    }
)
