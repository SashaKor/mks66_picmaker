run:
	make clean
	python 00.py
	convert img.txt img.png
	
clean:
	rm *.png
	rm *.txt
