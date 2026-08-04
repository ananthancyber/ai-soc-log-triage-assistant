from scripts.analyze_alert import extract_source_ip


def test_extract_source_ip_from_data():

    alert = {
        "data": {
            "srcip": "192.168.1.100"
        }
    }

    assert extract_source_ip(alert) == "192.168.1.100"


def test_extract_source_ip_top_level():

    alert = {
        "srcip": "10.0.0.5"
    }

    assert extract_source_ip(alert) == "10.0.0.5"


def test_extract_source_ip_missing():

    alert = {}

    assert extract_source_ip(alert) == "N/A"