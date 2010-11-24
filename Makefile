

UNITTEST_SVN_URL=http://svn.python.org/projects/python/branches/py3k/Lib/unittest
PATCH_FILE=unittest2-py3k.patch

LIB=unittest2-py3k/unittest2

$(LIB):
	svn co $(UNITTEST_SVN_URL)  $(LIB)
	$(MAKE) patch

patch: $(LIB)
	if [ -f $(LIB)/compatibility.py ]; then $(RM) $(LIB)/compatibility.py; fi
	touch $(LIB)/compatibility.py
	svn add $(LIB)/compatibility.py
	cat $(PATCH_FILE)|patch -p0

unittest:
	svn co $(UNITTEST_SVN_URL)

test: $(LIB)
	python3.1 discover.py -s unittest2-py3k
	python3.0 discover.py -s unittest2-py3k

revert-patch:
	svn revert -R $(LIB)

update-patch:
	svn diff $(LIB) > $(PATCH_FILE)

clean:
	$(RM) -r $(LIB)

