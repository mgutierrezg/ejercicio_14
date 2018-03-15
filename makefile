fecha_manchas.pdf: fecha_manchas.dat grafica.py
	python grafica.py 

fecha_manchas.dat: monthrg.dat procesa.py
	python procesa.py

monthrg.dat:
	wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/solar/monthrg.dat
