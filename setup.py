from setuptools import setup
import subprocess
import os

setup(
    name = "Pi20English",
    version = "1.0",
    author = "Andy Emre Kocak, Rana Taki, Yoel Kastro, Yasar Idikut",
    author_email = "emre.kocak@hisarschool.k12.tr, rana.taki@hisarschool.k12.tr, sarp.kastro@hisarschool.k12.tr, yasar.idikut@hisarschool.k12.tr",
    description = "Library that makes use of sensors, motors, and servos in the PiWars Turkey robot kit by HisarCS",
    packages = ["Pi20English"],
    classifiers=["Development Status :: 4 - Beta"],
    install_requires=[
        'picamera',
        'pygame',
        'RPi.GPIO',
        'wiringpi',
        'numpy',
        'opencv-contrib-python==4.2.0.32'
    ]

)
