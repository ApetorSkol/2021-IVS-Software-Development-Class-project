PACK_NAME=xhnato00_xlanro00_xmacho12_xslivk03
PACK_DIR=../../$(PACK_NAME)
EXECUTABLE=../dist/calculator

# builds package using pyinstaller
# python does not compile, so at least it does something
all: $(EXECUTABLE)

$(EXECUTABLE): venv
	./build.sh

# makes the final package
pack: doc $(EXECUTABLE)
	# delete previous temporary files - if there are any
	rm -rf $(PACK_DIR)
	rm -rf $(PACK_DIR).zip

	mkdir $(PACK_DIR)
	mkdir $(PACK_DIR)/doc
	cp -rf html/ $(PACK_DIR)/doc

	mkdir $(PACK_DIR)/install
	cp -f $(EXECUTABLE) $(PACK_DIR)/install/ivscalculator
	cp -f calculator.desktop $(PACK_DIR)/install/ivscalculator.desktop
	cp -f install.sh $(PACK_DIR)/install/install
	cp -f icon.png $(PACK_DIR)/install/ivscalculator.png
	cp -f uninstall.sh $(PACK_DIR)/install/ivscalculator-uninstall

	make clean              # clean repository before zipping it
	mkdir $(PACK_DIR)/repo
	cp -rf .. $(PACK_DIR)/repo

	cd ../../ && zip -r $(PACK_NAME).zip $(PACK_NAME)

	rm -rf $(PACK_DIR) # remove the temporary directory

# removes all files, that should not be submitted
clean:
	rm -rf venv/ html/ latex/
	rm -rf ../dist/ ../build/
	rm -rf __pycache__

# runs the test for math library
test:
	. venv/bin/activate
	python3 -m unittest -v tests_math_library.py

# generates the documentation
doc:
	rm -rf html/
	doxygen Doxyfile
	
# runs the program
run:
	. venv/bin/activate
	python3 calculator.py

# should compile profiling program
profile:

venv:
	./venv-setup.sh
