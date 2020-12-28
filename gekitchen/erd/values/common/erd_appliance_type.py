import enum

@enum.unique
class ErdApplianceType(enum.Enum):
    UNKNOWN = "FF"
    WATER_HEATER = "00"
    DRYER = "01"
    WASHER = "02"
    FRIDGE = "03"
    MICROWAVE = "04"
    ADVANTIUM = "05"
    DISH_WASHER = "06"
    OVEN = "07"
    ELECTRIC_RANGE = "08"
    GAS_RANGE = "09"
    AIR_CONDITIONER = "0a"
    ELECTRIC_COOKTOP = "0b"
    COOKTOP = "11"
    PIZZA_OVEN = "0c"
    GAS_COOKTOP = "0d"
    SPLIT_AIR_CONDITIONER = "0e"
    HOOD = "0f"
    POE_WATER_FILTER = "10"
    WATER_SOFTENER = "15"
    PORTABLE_AIR_CONDITIONER = "16"
    COMBINATION_WASHER_DRYER = "17"
    ZONELINE = "14"
    DELEVERY_BOX = "12"
    CAFE_COFFEE_MAKER = "1A"
