import database.query as Query
rarityArray = [
    "Consumer",
    "Industrial",
    "Mil-Spec",
    "Restricted",
    "Classified",
    "Covert"
]

rarityMap = {
    "Consumer": 0,
    "Industrial": 1,
    "Mil-Spec": 2,
    "Restricted": 3,
    "Classified": 4,
    "Covert": 5
}

reverseRarityMap = {
    0: "Consumer",
    1: "Industrial",
    2: "Mil-Spec",
    3: "Restricted",
    4: "Classified",
    5: "Covert"
}


def getRarityNameByRarityID(rarityID: int):
    return reverseRarityMap[rarityID]


def getRarityIDByRarityName(rarityName: str):
    return rarityMap[rarityName]


def getNextRarityNameByRarityName(rarityName: str):
    return reverseRarityMap[rarityMap[rarityName] + 1]
