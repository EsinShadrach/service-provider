# this one can be used to get which network provider a phone number uses its useful to an extent but you'll have to write the country code like Nigeria is +234
try:
    import phonenumbers

    num = input("enter number with correct country code: ")

    from phonenumbers import geocoder

    ch_number = phonenumbers.parse(num, "CH")
    print(geocoder.description_for_number(ch_number, "en"))

    from phonenumbers import carrier

    service_number = phonenumbers.parse(num, "RO")
    print(carrier.name_for_number(service_number, "en"))

except:
    print("invalid number or country code!")
