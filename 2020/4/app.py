from pprint import pprint
import re


def validate_passport(passport):
    try:
        if not re.search(r"^#(?:[0-9a-fA-F]{1,2}){3}", passport["hcl"]):
            print("hcl", passport["hcl"])
            # print("invalid")
            # print()
            return False
        # else:
        #     print(passport["hcl"])
        #     print("valid")
        #     print()
        height_unit = passport["hgt"][-2:]
        height = int(passport["hgt"][:-2])
        if height_unit == "cm":
            if height < 150 or height > 193:
                print("hgt", passport["hgt"])
                return False
        elif height_unit == "in":
            if height < 59 or height > 76:
                print("hgt", passport["hgt"])
                return False
        else:
            print("hgt", passport["hgt"])
            return False
        if (
            len(passport["byr"]) != 4
            or int(passport["byr"]) < 1920
            or int(passport["byr"]) > 2002
        ):
            print("byr", passport["byr"])
            return False
        if (
            len(passport["iyr"]) != 4
            or int(passport["iyr"]) < 2010
            or int(passport["iyr"]) > 2020
        ):
            print("iyr", passport["iyr"])
            return False
        if (
            len(passport["eyr"]) != 4
            or int(passport["eyr"]) < 2020
            or int(passport["iyr"]) > 2030
        ):
            print("eyr", passport["eyr"])
            return False
        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            print("ecl", passport["ecl"])
            return False
        if len(passport["pid"]) != 9:
            print("pid", passport["pid"])
            return False
        return True
    except:
        pprint(passport)
        return False


f = open("input", "r")
input = f.readlines()

valid_field = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
valid_field_with_cid = set(["byr", "iyr", "eyr", "hgt", "cid", "hcl", "ecl", "pid"])

passport = list()
passports = list()
for line in input:
    if line == "\n":
        passport = "".join(passport)
        passports.append(passport)
        passport = list()
    else:
        passport.append(line)
passports.append("".join(passport))

valid_pass_count = 0
dict_passports = list()
for passport in passports:
    passport = re.split(" |\n", passport)
    dict_passport = dict()
    # print(passport)
    contained_keys = set()
    for key in passport:
        if key != "":
            contained_keys.add(key.split(":")[0])
            dict_passport[key.split(":")[0]] = key.split(":")[1]
    if contained_keys == valid_field or contained_keys == valid_field_with_cid:
        dict_passports.append(dict_passport)
        is_valid = validate_passport(dict_passport)
        print()
        # print(is_valid)
        # pprint(dict_passport)
        # print()
        if is_valid:
            valid_pass_count += 1
# pprint(dict_passports)
print(valid_pass_count)
