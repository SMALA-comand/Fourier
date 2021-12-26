"""
``fourierwavelet``
=====================
Библиотека, реализующая готовое преобразование Фурье и Вейвлет
Из полученного csv файла через библиотеки scipy.fft и pywt.
"""
from .fourierwavelet import fourier, wavelets_dwt, wavelets_cwt

__author__ = 'Марк Козлов, Вячеслав Есаков, Артём Радайкин, Александр Савостьянов, Лев Памбухчян'

__all__ = ['fourier', 'wavelets_dwt', 'wavelets_cwt']

__version__ = "0.0.6"