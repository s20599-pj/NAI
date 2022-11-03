"""
Autorzy: Kamil Romiński i Artur Jankowski
Program za pomoca danych wejsciowych oblicza czy urzadzenie ma nawlizac powietrze w otoczeniu

Instrukcja uruchomienia:
 - zainstalowac pythona 3
 - zainstalowac skfuzzy - pip install -U scikit-fuzzy
 - zainstalowac numpy - pip install numpy
 - zainstalowac matplotlib - pip install -U matplotlib

"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
"""
Zmienna okreslajaca zakres wartosci nawilzenia powietrza
"""
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
"""
Zmiennna okreslajaca zakres wartosci temperatury otoczenia 
"""
water_level = ctrl.Antecedent(np.arange(0, 101, 1), 'water_level')
"""
Zmienna okreslajaca zakres wartosci poziomu wody w nawilzaczu
"""
humidity_out = ctrl.Consequent(np.arange(0, 5, 1), 'humidity_out')
"""
Zmienna okreslajaca zakres wartosci gdy ma byc nawilzane powietrze
"""
# automf do ilosci mozliwych wyjsc - jakosc
humidity.automf(3)
temperature.automf(3)
water_level.automf(3)

humidity_out['no'] = fuzz.trimf(humidity_out.universe, [0, 0, 2])
"""
Zakres wartosci w ktorych powietrze nie bedzie nawilzane
"""
humidity_out['yes'] = fuzz.trimf(humidity_out.universe, [2, 4, 4])
"""
Zakres wartosci w ktorych powietrze bedzie nawilzane
"""

rule1 = ctrl.Rule(humidity['poor'] & temperature['poor'] & water_level['poor'], humidity_out['no'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
rule2 = ctrl.Rule(humidity['poor'] & temperature['poor'] & water_level['good'], humidity_out['no'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
rule3 = ctrl.Rule(humidity['poor'] & temperature['good'] & water_level['good'], humidity_out['yes'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
rule4 = ctrl.Rule(humidity['average'] & temperature['poor'] & water_level['good'], humidity_out['no'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
rule5 = ctrl.Rule(humidity['good'] & temperature['poor'] & water_level['poor'], humidity_out['no'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
rule6 = ctrl.Rule(humidity['good'] & temperature['good'] & water_level['good'], humidity_out['no'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
rule7 = ctrl.Rule(humidity['poor'] & temperature['average'] & water_level['good'], humidity_out['yes'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
rule8 = ctrl.Rule(humidity['average'] & temperature['average'] & water_level['good'], humidity_out['yes'])
"""
Regula ustalajaca kiedy powietrze bedzie nawilzane
"""
humidity_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
"""
Kontroler nawilzania sprawdzajacy wartosci z regulami
"""

humi = ctrl.ControlSystemSimulation(humidity_ctrl)
"""
Zmienna stosujaca kontroler
"""

humi.input['humidity'] = 40
"""
Ustalanie nawilzenia otoczenia
"""
humi.input['temperature'] = 50
"""
Ustalanie temperatury otoczenia
"""
humi.input['water_level'] = 100
"""
Ustalanie poziomu wody nawilzacza
"""


humi.compute()
print(humi.output['humidity_out'])
humidity_out.view(sim=humi)
plt.show()
