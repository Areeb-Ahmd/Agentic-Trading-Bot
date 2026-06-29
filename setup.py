from setuptools import find_packages, setup

setup(
    name = "agentic-trading-bot",
    version = "0.0.1",
    author = "Syed Areeb Ahmad",
    author_email = "ahmad.syedareeb7@gmail.com",
    packages = find_packages(),
    install_requires = ['lancedb', 'langchain', 'langgraph', 'tavily-python', 'polygon']
)