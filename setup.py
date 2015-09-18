from distutils.core import setup

setup(
    name='flask-inliner',
    version='1.0.0',
    py_modules=['flask_inliner'],
    url='https://github.com/Code-ReaQtor/flask-inliner',
    download_url='https://github.com/Code-ReaQtor/flask-inliner/tarball/1.0.0',
    license='MIT',
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    long_description=open('README').read(),
    description='Flask-Inliner converts CSS <style> blocks to inline style attributes',
    keywords = [],
    install_requires=['Flask', 'Pynliner'],
    classifiers = ['Development Status :: 3 - Alpha',
                   'Framework :: Flask',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Programming Language :: Python'],
)
