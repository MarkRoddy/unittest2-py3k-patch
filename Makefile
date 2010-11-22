

UNITTEST_SVN_URL=http://svn.python.org/projects/python/branches/py3k/Lib/unittest
PATCH_FILE=unittest2-py3k.patch

unittest2: unittest $(PATCH_FILE)
	cp -r unittest unittest2
	cd unittest2 && cat ../$(PATCH_FILE)|patch -p0

unittest:
	svn co $(UNITTEST_SVN_URL)

test: unittest2
	tox

update-patch:
	svn diff unittest2 > $(UNITTEST_SVN_URL)

clean:
	$(RM) -r unittest2

