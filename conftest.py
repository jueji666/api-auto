import pytest
from tools.YamlUtil import Yamlutil

@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    Yamlutil("extract.yaml").clear_yaml()