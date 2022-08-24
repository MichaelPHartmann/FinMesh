python setup.py sdist bdist_wheel
pip install dist/FinMesh-2.2.3.tar.gz

# echo Creating new distributions...
# python3 setup.py sdist bdist_wheel
# echo Uploading new version to Pypi...
# twine upload --repository testpypi dist/*

# echo Upgrading FinMesh...
# pip install --force-reinstall --index-url https://test.pypi.org/simple/ FinMesh
# sleep 2s
# pip install --force-reinstall --index-url https://test.pypi.org/simple/ FinMesh
