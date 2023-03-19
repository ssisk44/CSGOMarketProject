import Tools.TradeUpAnalysis as TradeUpAnalysis

def main():
    testWearCountSections()

def testWearCountSections():
    wearCountSections = TradeUpAnalysis.wearCountSections
    for wearSection in wearCountSections:
        for entry in wearSection:
            assert sum(entry[0]) == 10
            assert sum(entry[1]) == 10

main()