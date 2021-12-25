from setuptools import setup, find_packages

setup(
    name="fourierwavelet",
    packages=find_packages(),
    version="0.0.1",
    description='Ready-made Fourier transform and Wavelet from a csv file',
    author="Artem Radaykin",
    author_email="radaykin.artem@mail.ru",
    url="https://github.com/SMALA-comand/Fourier",
    install_requires = ['matplotlib.pyplot','scipy.fft','csv','pywt','numpy'],
    zip_safe=False, 
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)