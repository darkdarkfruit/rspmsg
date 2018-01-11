files = rspmsg/__init__.py rspmsg/rspmsg.py rspmsg/test_rspmsg.py
# file_pytest_genscript = rspmsg/test_rspmsg_pytest.py

default: test
	echo ''


test: ${files}
	echo ''
	pytest rspmsg/


# make a source distribution in dist/
sdist: ${files}
	rm dist/*
	python setup.py sdist


# upload to pypi
upload: sdist
	twine upload dist/*


install : test
	python setup.py install


docs: ${files}
	echo "Generating docs"
	# do sphinx-quickstart first
	# http://www.sphinx-doc.org/en/stable/tutorial.html
	# http://www.sphinx-doc.org/en/stable/invocation.html#invocation-apidoc
	rm docs/source/[^i]*.rst
	sphinx-apidoc -f -o docs/source rspmsg
	cd docs && make clean && make html



# git push to github
# do `git remote add origin https://github.com/darkdarkfruit/rspmsg.git` first
git_push_all:
	git push --all


# git push with tags
git_push_tags: git_push_all
	git push --tags

# github
git push --all
git push --tags
