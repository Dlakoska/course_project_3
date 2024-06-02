from src.functions import mask_information, load_last_operations, load_operations


def test_load_operations():
    assert load_operations() == [{"id": "Операция №6", "state": "EXECUTED", "date": "2013-08-26T10:50:58.294041"},
                                 {"id": "Операция №3", "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
                                 {"id": "Операция №2", "state": "EXECUTED", "date": "2011-08-26T10:50:58.294041"},
                                 {"id": "Операция №1", "state": "EXECUTED", "date": "2020-08-26T10:50:58.294041"},
                                 {"id": "Операция №4", "state": "EXECUTED", "date": "2022-08-26T10:50:58.294041"}]


def test_load_last_operations():
    assert load_last_operations([{"id": 1, "date": "2013-08-26T10:50:58.294041"},
                                 {"id": 2, "date": "2019-08-26T10:50:58.294041"},
                                 {"id": 3, "date": "2011-08-26T10:50:58.294041"},
                                 {"id": 4, "date": "2020-08-26T10:50:58.294041"},
                                 {"id": 5, "date": "2023-08-26T10:50:58.294041"},
                                 {"id": 6, "date": "2022-08-26T10:50:58.294041"}]) != [{"id": 3, "date": "26.08.2011"},
                                                                                       {"id": 1, "date": "26.08.2013"},
                                                                                       {"id": 2, "date": "26.08.2019"},
                                                                                       {"id": 4, "date": "26.08.2020"},
                                                                                       {"id": 6, "date": "26.08.2022"}]


def test_mask_information():
    assert mask_information("Visa master 1234567899876543") == "Visa master 1234 56** **** 6543"
    assert mask_information("Visa gold 1234567899874568") == "Visa gold 1234 56** **** 4568"
    assert mask_information("Счет 12345678998765432112") == "Счет **2112"
