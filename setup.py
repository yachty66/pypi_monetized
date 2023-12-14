from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'stripe',
        'supabase',
        'heroku',
    ],
    entry_points={
        'console_scripts': [
            'test.hello_world = hello_world.hello_world:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple python package which can be pip installed and used with an API key. Uses Supabase as database, Stripe for payment, and Heroku for hosting.',
    keywords='hello_world python package api stripe supabase heroku',
    url='https://github.com/yourusername/hello_world',  # use the URL to the github repo
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
