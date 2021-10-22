#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 12:12:11 2021

@author: jeremias
"""

"""
 se puede notar que ninguna frecuencia en la imágen está en la lista, 
 entoces quiere decir que la frecuencia de muestreo no es el doble de la 
 maxima frecuencia en la señal
 las frecuencias mayores a la de muestreo se empiezan a sumar dentro de las 
 que estan debajos de ésta. Esto sucede por la convolución en frecuencia 
 (aliasing en frecuencia)
 
 por lo tanto es fm = 128 con f1 = 100 y f2 = 50 ya que 50 entra en 51 y 100 entra en 29
 además el valor del espectro de magnitud es la mitad de frecuncia es la mitad de la
frecuncia de muestreo 128 / 2 = 64, si esta multiplicado como con f2 entonce es
(128/2) * 4 = 256
"""


