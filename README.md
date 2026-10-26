# subnet-calculator

Output:

Network         192.168.1.0
Mask            255.255.255.0
Wildcard        0.0.0.255
Broadcast       192.168.1.255
First host      192.168.1.1
Last host       192.168.1.254
Total addresses 256
Usable hosts    254


Test Output:
test_subnet.py::test_matches_ipaddress_module[192.168.1.10/24] PASSED                                          [  8%]
test_subnet.py::test_matches_ipaddress_module[10.0.0.0/8] PASSED                                               [ 16%]
test_subnet.py::test_matches_ipaddress_module[172.16.5.4/30] PASSED                                            [ 25%]
test_subnet.py::test_matches_ipaddress_module[8.8.8.8/32] PASSED                                               [ 33%]
test_subnet.py::test_matches_ipaddress_module[10.1.1.1/31] PASSED                                              [ 41%]
test_subnet.py::test_matches_ipaddress_module[0.0.0.0/0] PASSED                                                [ 50%]
test_subnet.py::test_usable_hosts_for_slash_24 PASSED                                                          [ 58%]
test_subnet.py::test_invalid_input_raises[192.168.1.10] PASSED                                                 [ 66%]
test_subnet.py::test_invalid_input_raises[300.1.1.1/24] PASSED                                                 [ 75%]
test_subnet.py::test_invalid_input_raises[10.0.0.0/33] PASSED                                                  [ 83%]
test_subnet.py::test_invalid_input_raises[abc/8] PASSED                                                        [ 91%]
test_subnet.py::test_invalid_input_raises[1.2.3/24] PASSED                                                     [100%]

================================================ 12 passed in 0.09s =================================================
