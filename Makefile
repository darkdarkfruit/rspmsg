files = rspmsg/__init__.py rspmsg/rspmsg.py rspmsg/test_rspmsg.py
# file_pytest_genscript = rspmsg/test_rspmsg_pytest.py

default: test
	echo ''


test: ${files} 
	echo ''
	pytest rspmsg/


# make a source distribution in dist/
sdist: ${files}
	python setup.py sdist


# upload to pypi
upload: sdist
	twine upload dist/*


install : test
	python setup.py install


# git push to github
# do `git remote add origin https://github.com/darkdarkfruit/rspmsg.git` first
git_push_all:
	git push --a


# git push with tags
git_push_tags: git_push_all
	git push --tags
