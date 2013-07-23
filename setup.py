from setuptools import setup, find_packages

from swx.common import __version__

setup(
    name='swx-common',
    version=__version__,
    long_description="""\
""",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    namespace_packages=['swx', 'swx.common'],
    zip_safe=False,
    author='Ross Jones',
    author_email='ross@mailbolt.com',
    license='AGPL',
    url='',
    description='Common code shared across SWX components',
    keywords='datastore scraping',
    install_requires=[
        "ConcurrentLogHandler==0.8.3"
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    package_data={'ckan': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
""",
    test_suite = 'nose.collector',
)
