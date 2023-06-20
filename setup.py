from setuptools import setup, find_packages

setup(
    name='ka-chatbot',
    version='1.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='Chatbot using Streamlit',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'torch',
        'transformers'
    ],
)
