# *** RUN ALL ***

# Compile all selected programs
define COMPILE
	lua src/mail.lua
	python3 src/mail.py 
	python3 src/mail2.py
	make ./src/mail
	./src/mail in/data_set.csv dist/c-out.log
endef

# Open dist
define DIST
	open dist/
endef

all:
	$(call COMPILE)
	$(call DIST)
