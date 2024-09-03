from items_test import country_city, city_population

def test_city_country() -> None:
    """Test whether names like Beijing , China works."""

    locate = country_city('moscow', 'russia')

    assert locate == 'Moscow, Russia'


def test_city_population():
    """Testing for city's population."""

    city_pop= city_population('berlin', 'german', '20M')
    assert city_pop == "Berlin German Population: 20M People"




