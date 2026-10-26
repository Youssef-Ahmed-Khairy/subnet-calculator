import ipaddress
import pytest
from subnet import calculate

CASES = [
    "192.168.1.10/24",
    "10.0.0.0/8",
    "172.16.5.4/30",
    "8.8.8.8/32",
    "10.1.1.1/31",
    "0.0.0.0/0",
]


@pytest.mark.parametrize("cidr", CASES)
def test_matches_ipaddress_module(cidr):
    result = calculate(cidr)
    net = ipaddress.ip_network(cidr, strict=False)
    assert result["network"] == str(net.network_address)
    assert result["broadcast"] == str(net.broadcast_address)
    assert result["mask"] == str(net.netmask)
    assert result["total"] == net.num_addresses


def test_usable_hosts_for_slash_24():
    assert calculate("192.168.1.10/24")["usable"] == 254


@pytest.mark.parametrize(
    "bad", ["192.168.1.10", "300.1.1.1/24", "10.0.0.0/33", "abc/8", "1.2.3/24"]
)
def test_invalid_input_raises(bad):
    with pytest.raises(ValueError):
        calculate(bad)
