from setuptools import setup


def get_version():
    with open("version.properties", "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("version="):
                return line.strip().split("=")[1]

    raise RuntimeError("version.properties não possui a chave version")


setup(
    version=get_version()
)