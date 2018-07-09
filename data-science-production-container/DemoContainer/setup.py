from setuptools import find_packages, setup

setup(
    name='ds_prod',
    packages=find_packages(),
    version='0.0.1',
    description='Example usage of ds_prod_api.',
    author='Gerben Oostra',
    author_email='gerben.oostra@bigdatarepublic.nl',
    license='Apache-2.0',
    long_description="README.md",
    python_requires='>3.5',
    install_requires=[
                     "click",
                     "python-dotenv>=0.5.1",
                     "flask==0.12.2",
                     "numpy==1.13.1",
                     "scikit-learn==0.18.1",
                     "dill==0.2.6",
                     "pandas==0.20.3",
                     "scipy==0.19.1",
                     "ds_prod_api",
    ],
    dependency_links=[
                      "https://github.com/BigDataRepublic/ds-prod-api/tarball/master#egg=ds_prod_api-0.0.1",
    ],
    include_package_data=True,
    package_data={
                  'ds_prod': ['models/*.*'],
                 },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
