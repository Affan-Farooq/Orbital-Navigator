from project import get_geolocation, iss_in_vicinity, valid_time


# It is imperative to note that these tests are dependant upon variable factors such as time, location, etc.


def test_get_geolocation():
    # The following tests are dependant upon geolocation of publicly displayed IP address.
    assert get_geolocation() == (44.2983, -76.4323)
    assert get_geolocation() != (33.1111, 66.4444)


def test_iss_in_vicinity():
    assert iss_in_vicinity(50.5432, 21.3234, 44.2983, -76.4323) == False
    assert iss_in_vicinity(47.5476, -73.8743, 44.2983, -76.4323) == True
    assert iss_in_vicinity(49.6748, -76.4323, 44.2983, -76.4323) == False
    assert iss_in_vicinity(39.6890, -81.2457, 44.2983, -76.4323) == True
    assert iss_in_vicinity(00.0000, 99.9999, 44.2983, -76.4323) == False


def test_valid_time():
    assert valid_time(44.2983, -76.4323) == True  # Currently after sunset and before sunrise
    assert valid_time(44.2983, -76.4323) != False  # Currently not before sunset and not after sunrise

    # Following tests are to be executed when testing the function during daytime (after sunrise and before sunset)
    # assert valid_time(44.2983, -76.4323) == False  # Currently before sunset and after sunrise
    # assert valid_time(44.2983, -76.4323) != True  # Currently not after sunset and not before sunrise
