import random

phones_list = ["Huawei U8230", "Honor 30 Lite", "Huawei P40 lite", "LG G3", "LG V30", "Meizu 16Xs", "Meizu Note 9",
               "Galaxy Nexus", "Moto X4", "Samsung Galaxy S4", "Samsung Galaxy S5", "Samsung Galaxy C5",
               "Samsung Galaxy Fold", "Samsung Galaxy A6s", "Redmi 8A", "Oppo Neo 5s"]

big_ver_list = ["7.1", "7.1.2", "8", "8.1", "9", "10", "11"]

operation_list = ["DIREKTLOGIN", "DIREKTOPEN", "DIREKTSENDMONEY", "DIREKTEFT", "DIREKTLOGOUT", "DIREKTCHANGEPASS"]

carrier_list = ["Turkcell", "Vodafone", "Turk Telekom"]


class Mobile:
    @classmethod
    def phone(cls, from_number=1, to_number=100, distinct=None) -> int:
        rand = random.randint(from_number, to_number - 1)

        if distinct:
            range1 = (to_number - from_number) // (distinct - 1)
            overflow = rand % range1
            rand = rand - overflow

        return rand

    @classmethod
    def imei(cls, from_number, to_number, distinct=None) -> str:
        rand = random.randint(from_number, to_number - 1) * 19

        if distinct:
            range1 = (to_number - from_number) // (distinct - 1)
            overflow = rand % range1
            rand = rand - overflow

        return str(rand)

    @classmethod
    def ip(cls, pool=255, distinct=None) -> str:
        o1 = random.randint(150, 180)
        o2 = random.randint(2, 250)
        o3 = random.randint(2, 250)
        o4 = random.randint(2, 250)

        return f"{o1}.{o2}.{o3}.{o4}"

    @classmethod
    def device_os(cls) -> str:
        os = "ANDROID"
        big_ver = random.choice(big_ver_list)
        ver = "V4.1.10"
        phones = random.choice(phones_list)

        return "|".join([os + ' ' + big_ver, ver, phones, "TR", str(random.randint(100000, 999999))])

    @classmethod
    def is_cracked(cls) -> int:
        return 0 if random.randint(1, 100) < 85 else 1

    @classmethod
    def connection_type(cls) -> str:
        return "WIFI" if random.randint(1, 100) < 50 else "GSM"

    @classmethod
    def carrier(cls) -> str:
        return random.choice(carrier_list)

    @classmethod
    def operation(cls) -> str:
        return random.choice(operation_list)
