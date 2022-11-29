import pytest
import itertools

from helper import *

# Parametrization of a few IPs to test
test_data = itertools.combinations(range(10), 4)
test_data = [i for i in test_data]


@pytest.mark.parametrize("ip1, ip2, ip3, ip4", test_data)
def test_validate_ip_address_string(ip1, ip2, ip3, ip4):
    # Arrange
    ip_string = "%s.%s.%s.%s" % (ip1, ip2, ip3, ip4)

    # Act
    result = validate_ip_address_string(ip_string)

    # Assert
    assert result
