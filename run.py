import pytest
import time
import os

if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    os.system("allure generate --clean reports/temp -o reports/report")