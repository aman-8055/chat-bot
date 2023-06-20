from setuptools import setup, find_packages

setup(
    name='question-answering-chatbot',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
        'torch',
        'transformers'
    ],
)
