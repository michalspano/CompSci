# *** RUN ALL ***

# Compile all selected programs
define COMPILE
	lua mail.lua
	python3 mail.py 
	python3 mail2.py
	make C/mail
	./C/mail src/data_set.csv dist/c-out.log
endef

# Open dist
define DIST
	open dist/
endef

all:
	$(call COMPILE)
	$(call DIST)
