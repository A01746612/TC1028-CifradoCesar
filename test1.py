#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import cesar


class Testprueba (unittest.TestCase):

    def test_codificacion(self):
        self.assertEqual(cesar.codificacion_cesar(
            "Hola Mundo", 3), "Krod#Pxqgr")
        self.assertEqual(cesar.codificacion_cesar(
            "Hola Mundo", 4), "Lspe$Qyrhs")

    def test_decodificacion(self):
        self.assertEqual(cesar.decodificacion_cesar(
            "Krod#Pxqgr", 3), "Hola Mundo")
        self.assertEqual(cesar.decodificacion_cesar(
            "Lspe$Qyrhs", 4), "Hola Mundo")


if __name__ == '__main__':
    unittest.main()
