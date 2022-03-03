"""
This is a Python module that provides several functions to facilitate the inclusion of data produced in Python in a LaTex document

"""
__authors__ = "Sonja Stuedli"
__author_emails__ = "scythja@gmail.com"
__version__ = "0.0.4"

from .python_to_latex import fig2pgf, mat2lat, numeric_list_to_tabularx

__all__ = ["fig2pgf", "mat2lat", "numeric_list_to_tabularx"]
