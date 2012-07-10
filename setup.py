from setuptools import setup

requirements = [
]

setup(
    name="bigsignal",
    version='0.0.1',
    author="Robby Ranshous",
    author_email="rranshous@gmail.com",
    description="simple evented objects",
    keywords="event",
    url="https://github.com/rranshous/bigsignal",
    py_modules=["eventhook","eventable"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=requirements,
)
