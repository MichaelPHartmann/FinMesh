echo Creating new distributions...
python3 setup.py sdist bdist_wheel
echo Uploading new version to Pypi...
twine upload --repository testpypi dist/*

echo Upgrading FinMesh...
pip3 install --upgrade --force-reinstall --index-url https://test.pypi.org/simple/ FinMesh
sleep 2s
pip3 install --upgrade --force-reinstall --index-url https://test.pypi.org/simple/ FinMesh