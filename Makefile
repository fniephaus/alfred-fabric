all:
	cd src ; \
	zip ../Fabric-for-Alfred.alfredworkflow . -r --exclude=*.DS_Store*

clean:
	rm -f *.alfredworkflow