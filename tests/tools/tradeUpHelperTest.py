import tools.tradeUpHelper as tUH

revContainer = [[1, 'Revolution Case', 'Temukau', 'M4A4', 'Factory New', 0.0, 0.8, '5', 1, 0, 944.0], [2, 'Revolution Case', 'Temukau', 'M4A4', 'Minimal Wear', 0.0, 0.8, '5', 1, 0, 382.62], [3, 'Revolution Case', 'Temukau', 'M4A4', 'Field-Tested', 0.0, 0.8, '5', 1, 0, 90.0], [4, 'Revolution Case', 'Temukau', 'M4A4', 'Well-Worn', 0.0, 0.8, '5', 1, 0, 91.08], [5, 'Revolution Case', 'Temukau', 'M4A4', 'Battle-Scarred', 0.0, 0.8, '5', 1, 0, 48.9], [6, 'Revolution Case', 'Temukau', 'M4A4', 'Factory New', 0.0, 0.8, '5', 0, 0, 484.87], [7, 'Revolution Case', 'Temukau', 'M4A4', 'Minimal Wear', 0.0, 0.8, '5', 0, 0, 199.61], [8, 'Revolution Case', 'Temukau', 'M4A4', 'Field-Tested', 0.0, 0.8, '5', 0, 0, 55.84], [9, 'Revolution Case', 'Temukau', 'M4A4', 'Well-Worn', 0.0, 0.8, '5', 0, 0, 53.68], [10, 'Revolution Case', 'Temukau', 'M4A4', 'Battle-Scarred', 0.0, 0.8, '5', 0, 0, 24.8], [11, 'Revolution Case', 'Head Shot', 'AK-47', 'Factory New', 0.0, 1.0, '5', 1, 0, 700.0], [12, 'Revolution Case', 'Head Shot', 'AK-47', 'Minimal Wear', 0.0, 1.0, '5', 1, 0, 305.0], [13, 'Revolution Case', 'Head Shot', 'AK-47', 'Field-Tested', 0.0, 1.0, '5', 1, 0, 162.22], [14, 'Revolution Case', 'Head Shot', 'AK-47', 'Well-Worn', 0.0, 1.0, '5', 1, 0, 90.0], [15, 'Revolution Case', 'Head Shot', 'AK-47', 'Battle-Scarred', 0.0, 1.0, '5', 1, 0, 64.28], [16, 'Revolution Case', 'Head Shot', 'AK-47', 'Factory New', 0.0, 1.0, '5', 0, 0, 305.99], [17, 'Revolution Case', 'Head Shot', 'AK-47', 'Minimal Wear', 0.0, 1.0, '5', 0, 0, 139.72], [18, 'Revolution Case', 'Head Shot', 'AK-47', 'Field-Tested', 0.0, 1.0, '5', 0, 0, 84.58], [19, 'Revolution Case', 'Head Shot', 'AK-47', 'Well-Worn', 0.0, 1.0, '5', 0, 0, 49.03], [20, 'Revolution Case', 'Head Shot', 'AK-47', 'Battle-Scarred', 0.0, 1.0, '5', 0, 0, 29.68], [21, 'Revolution Case', 'Duality', 'AWP', 'Factory New', 0.0, 0.7, '4', 1, 0, 139.68], [22, 'Revolution Case', 'Duality', 'AWP', 'Minimal Wear', 0.0, 0.7, '4', 1, 0, 70.89], [23, 'Revolution Case', 'Duality', 'AWP', 'Field-Tested', 0.0, 0.7, '4', 1, 0, 33.66], [24, 'Revolution Case', 'Duality', 'AWP', 'Well-Worn', 0.0, 0.7, '4', 1, 0, 42.8], [25, 'Revolution Case', 'Duality', 'AWP', 'Battle-Scarred', 0.0, 0.7, '4', 1, 0, 29.3], [26, 'Revolution Case', 'Duality', 'AWP', 'Factory New', 0.0, 0.7, '4', 0, 0, 58.94], [27, 'Revolution Case', 'Duality', 'AWP', 'Minimal Wear', 0.0, 0.7, '4', 0, 0, 31.7], [28, 'Revolution Case', 'Duality', 'AWP', 'Field-Tested', 0.0, 0.7, '4', 0, 0, 17.02], [29, 'Revolution Case', 'Duality', 'AWP', 'Well-Worn', 0.0, 0.7, '4', 0, 0, 19.2], [30, 'Revolution Case', 'Duality', 'AWP', 'Battle-Scarred', 0.0, 0.7, '4', 0, 0, 13.53], [31, 'Revolution Case', 'Wicked Sick', 'P2000', 'Factory New', 0.0, 1.0, '4', 1, 0, 83.5], [32, 'Revolution Case', 'Wicked Sick', 'P2000', 'Minimal Wear', 0.0, 1.0, '4', 1, 0, 34.47], [33, 'Revolution Case', 'Wicked Sick', 'P2000', 'Field-Tested', 0.0, 1.0, '4', 1, 0, 14.5], [34, 'Revolution Case', 'Wicked Sick', 'P2000', 'Well-Worn', 0.0, 1.0, '4', 1, 0, 10.14], [35, 'Revolution Case', 'Wicked Sick', 'P2000', 'Battle-Scarred', 0.0, 1.0, '4', 1, 0, 10.06], [36, 'Revolution Case', 'Wicked Sick', 'P2000', 'Factory New', 0.0, 1.0, '4', 0, 0, 41.49], [37, 'Revolution Case', 'Wicked Sick', 'P2000', 'Minimal Wear', 0.0, 1.0, '4', 0, 0, 22.1], [38, 'Revolution Case', 'Wicked Sick', 'P2000', 'Field-Tested', 0.0, 1.0, '4', 0, 0, 10.24], [39, 'Revolution Case', 'Wicked Sick', 'P2000', 'Well-Worn', 0.0, 1.0, '4', 0, 0, 6.79], [40, 'Revolution Case', 'Wicked Sick', 'P2000', 'Battle-Scarred', 0.0, 1.0, '4', 0, 0, 6.1], [41, 'Revolution Case', 'Wild Child', 'UMP-45', 'Factory New', 0.0, 1.0, '4', 1, 0, 76.5], [42, 'Revolution Case', 'Wild Child', 'UMP-45', 'Minimal Wear', 0.0, 1.0, '4', 1, 0, 35.6], [43, 'Revolution Case', 'Wild Child', 'UMP-45', 'Field-Tested', 0.0, 1.0, '4', 1, 0, 14.35], [44, 'Revolution Case', 'Wild Child', 'UMP-45', 'Well-Worn', 0.0, 1.0, '4', 1, 0, 10.25], [45, 'Revolution Case', 'Wild Child', 'UMP-45', 'Battle-Scarred', 0.0, 1.0, '4', 1, 0, 10.12], [46, 'Revolution Case', 'Wild Child', 'UMP-45', 'Factory New', 0.0, 1.0, '4', 0, 0, 42.12], [47, 'Revolution Case', 'Wild Child', 'UMP-45', 'Minimal Wear', 0.0, 1.0, '4', 0, 0, 22.17], [48, 'Revolution Case', 'Wild Child', 'UMP-45', 'Field-Tested', 0.0, 1.0, '4', 0, 0, 10.26], [49, 'Revolution Case', 'Wild Child', 'UMP-45', 'Well-Worn', 0.0, 1.0, '4', 0, 0, 6.85], [50, 'Revolution Case', 'Wild Child', 'UMP-45', 'Battle-Scarred', 0.0, 1.0, '4', 0, 0, 5.78], [51, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Factory New', 0.0, 0.8, '3', 1, 0, 28.58], [52, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Minimal Wear', 0.0, 0.8, '3', 1, 0, 11.77], [53, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Field-Tested', 0.0, 0.8, '3', 1, 0, 5.67], [54, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Well-Worn', 0.0, 0.8, '3', 1, 0, 8.6], [55, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Battle-Scarred', 0.0, 0.8, '3', 1, 0, 5.11], [56, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Factory New', 0.0, 0.8, '3', 0, 0, 9.33], [57, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Minimal Wear', 0.0, 0.8, '3', 0, 0, 4.53], [58, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Field-Tested', 0.0, 0.8, '3', 0, 0, 2.19], [59, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Well-Worn', 0.0, 0.8, '3', 0, 0, 3.17], [60, 'Revolution Case', 'Emphorosaur-S', 'M4A1-S', 'Battle-Scarred', 0.0, 0.8, '3', 0, 0, 2.02], [61, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Factory New', 0.0, 0.75, '3', 1, 0, 14.2], [62, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Minimal Wear', 0.0, 0.75, '3', 1, 0, 7.54], [63, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Field-Tested', 0.0, 0.75, '3', 1, 0, 2.94], [64, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Well-Worn', 0.0, 0.75, '3', 1, 0, 3.3], [65, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Battle-Scarred', 0.0, 0.75, '3', 1, 0, 2.11], [66, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Factory New', 0.0, 0.75, '3', 0, 0, 5.08], [67, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Minimal Wear', 0.0, 0.75, '3', 0, 0, 3.56], [68, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Field-Tested', 0.0, 0.75, '3', 0, 0, 1.63], [69, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Well-Worn', 0.0, 0.75, '3', 0, 0, 1.62], [70, 'Revolution Case', 'Umbral Rabbit', 'Glock-18', 'Battle-Scarred', 0.0, 0.75, '3', 0, 0, 1.01], [71, 'Revolution Case', 'Neoqueen', 'P90', 'Factory New', 0.0, 0.6, '3', 1, 0, 9.7], [72, 'Revolution Case', 'Neoqueen', 'P90', 'Minimal Wear', 0.0, 0.6, '3', 1, 0, 5.61], [73, 'Revolution Case', 'Neoqueen', 'P90', 'Field-Tested', 0.0, 0.6, '3', 1, 0, 3.05], [74, 'Revolution Case', 'Neoqueen', 'P90', 'Well-Worn', 0.0, 0.6, '3', 1, 0, 3.53], [75, 'Revolution Case', 'Neoqueen', 'P90', 'Battle-Scarred', 0.0, 0.6, '3', 1, 0, 7.24], [76, 'Revolution Case', 'Neoqueen', 'P90', 'Factory New', 0.0, 0.6, '3', 0, 0, 4.98], [77, 'Revolution Case', 'Neoqueen', 'P90', 'Minimal Wear', 0.0, 0.6, '3', 0, 0, 2.9], [78, 'Revolution Case', 'Neoqueen', 'P90', 'Field-Tested', 0.0, 0.6, '3', 0, 0, 1.55], [79, 'Revolution Case', 'Neoqueen', 'P90', 'Well-Worn', 0.0, 0.6, '3', 0, 0, 1.44], [80, 'Revolution Case', 'Neoqueen', 'P90', 'Battle-Scarred', 0.0, 0.6, '3', 0, 0, 2.81], [81, 'Revolution Case', 'Sakkaku', 'MAC-10', 'Field-Tested', 0.21, 0.79, '3', 1, 0, 8.56], [82, 'Revolution Case', 'Sakkaku', 'MAC-10', 'Well-Worn', 0.21, 0.79, '3', 1, 0, 4.0], [83, 'Revolution Case', 'Sakkaku', 'MAC-10', 'Battle-Scarred', 0.21, 0.79, '3', 1, 0, 2.11], [84, 'Revolution Case', 'Sakkaku', 'MAC-10', 'Field-Tested', 0.21, 0.79, '3', 0, 0, 4.63], [85, 'Revolution Case', 'Sakkaku', 'MAC-10', 'Well-Worn', 0.21, 0.79, '3', 0, 0, 2.27], [86, 'Revolution Case', 'Sakkaku', 'MAC-10', 'Battle-Scarred', 0.21, 0.79, '3', 0, 0, 1.03], [87, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Factory New', 0.0, 1.0, '3', 1, 0, 14.03], [88, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Minimal Wear', 0.0, 1.0, '3', 1, 0, 5.35], [89, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Field-Tested', 0.0, 1.0, '3', 1, 0, 2.22], [90, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Well-Worn', 0.0, 1.0, '3', 1, 0, 2.0], [91, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Battle-Scarred', 0.0, 1.0, '3', 1, 0, 1.95], [92, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Factory New', 0.0, 1.0, '3', 0, 0, 4.96], [93, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Minimal Wear', 0.0, 1.0, '3', 0, 0, 2.92], [94, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Field-Tested', 0.0, 1.0, '3', 0, 0, 1.5], [95, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Well-Worn', 0.0, 1.0, '3', 0, 0, 1.17], [96, 'Revolution Case', 'Banana Cannon', 'R8 Revolver', 'Battle-Scarred', 0.0, 1.0, '3', 0, 0, 0.88], [97, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Factory New', 0.0, 1.0, '2', 1, 0, 4.4], [98, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Minimal Wear', 0.0, 1.0, '2', 1, 0, 0.99], [99, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Field-Tested', 0.0, 1.0, '2', 1, 0, 0.46], [100, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Well-Worn', 0.0, 1.0, '2', 1, 0, 0.32], [101, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Battle-Scarred', 0.0, 1.0, '2', 1, 0, 0.3], [102, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Factory New', 0.0, 1.0, '2', 0, 0, 0.82], [103, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Minimal Wear', 0.0, 1.0, '2', 0, 0, 0.36], [104, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Field-Tested', 0.0, 1.0, '2', 0, 0, 0.23], [105, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Well-Worn', 0.0, 1.0, '2', 0, 0, 0.17], [106, 'Revolution Case', 'Liquidation', 'MP5-SD', 'Battle-Scarred', 0.0, 1.0, '2', 0, 0, 0.15], [107, 'Revolution Case', 'Featherweight', 'MP9', 'Factory New', 0.0, 1.0, '2', 1, 0, 3.15], [108, 'Revolution Case', 'Featherweight', 'MP9', 'Minimal Wear', 0.0, 1.0, '2', 1, 0, 0.93], [109, 'Revolution Case', 'Featherweight', 'MP9', 'Field-Tested', 0.0, 1.0, '2', 1, 0, 0.51], [110, 'Revolution Case', 'Featherweight', 'MP9', 'Well-Worn', 0.0, 1.0, '2', 1, 0, 0.31], [111, 'Revolution Case', 'Featherweight', 'MP9', 'Battle-Scarred', 0.0, 1.0, '2', 1, 0, 0.31], [112, 'Revolution Case', 'Featherweight', 'MP9', 'Factory New', 0.0, 1.0, '2', 0, 0, 0.82], [113, 'Revolution Case', 'Featherweight', 'MP9', 'Minimal Wear', 0.0, 1.0, '2', 0, 0, 0.39], [114, 'Revolution Case', 'Featherweight', 'MP9', 'Field-Tested', 0.0, 1.0, '2', 0, 0, 0.24], [115, 'Revolution Case', 'Featherweight', 'MP9', 'Well-Worn', 0.0, 1.0, '2', 0, 0, 0.18], [116, 'Revolution Case', 'Featherweight', 'MP9', 'Battle-Scarred', 0.0, 1.0, '2', 0, 0, 0.16], [117, 'Revolution Case', 'Cyberforce', 'SG 553', 'Factory New', 0.0, 0.9, '2', 1, 0, 3.17], [118, 'Revolution Case', 'Cyberforce', 'SG 553', 'Minimal Wear', 0.0, 0.9, '2', 1, 0, 0.92], [119, 'Revolution Case', 'Cyberforce', 'SG 553', 'Field-Tested', 0.0, 0.9, '2', 1, 0, 0.39], [120, 'Revolution Case', 'Cyberforce', 'SG 553', 'Well-Worn', 0.0, 0.9, '2', 1, 0, 0.35], [121, 'Revolution Case', 'Cyberforce', 'SG 553', 'Battle-Scarred', 0.0, 0.9, '2', 1, 0, 0.28], [122, 'Revolution Case', 'Cyberforce', 'SG 553', 'Factory New', 0.0, 0.9, '2', 0, 0, 0.82], [123, 'Revolution Case', 'Cyberforce', 'SG 553', 'Minimal Wear', 0.0, 0.9, '2', 0, 0, 0.37], [124, 'Revolution Case', 'Cyberforce', 'SG 553', 'Field-Tested', 0.0, 0.9, '2', 0, 0, 0.23], [125, 'Revolution Case', 'Cyberforce', 'SG 553', 'Well-Worn', 0.0, 0.9, '2', 0, 0, 0.18], [126, 'Revolution Case', 'Cyberforce', 'SG 553', 'Battle-Scarred', 0.0, 0.9, '2', 0, 0, 0.15], [127, 'Revolution Case', 'Insomnia', 'MAG-7', 'Factory New', 0.0, 1.0, '2', 1, 0, 2.7], [128, 'Revolution Case', 'Insomnia', 'MAG-7', 'Minimal Wear', 0.0, 1.0, '2', 1, 0, 0.86], [129, 'Revolution Case', 'Insomnia', 'MAG-7', 'Field-Tested', 0.0, 1.0, '2', 1, 0, 0.42], [130, 'Revolution Case', 'Insomnia', 'MAG-7', 'Well-Worn', 0.0, 1.0, '2', 1, 0, 0.31], [131, 'Revolution Case', 'Insomnia', 'MAG-7', 'Battle-Scarred', 0.0, 1.0, '2', 1, 0, 0.31], [132, 'Revolution Case', 'Insomnia', 'MAG-7', 'Factory New', 0.0, 1.0, '2', 0, 0, 0.86], [133, 'Revolution Case', 'Insomnia', 'MAG-7', 'Minimal Wear', 0.0, 1.0, '2', 0, 0, 0.37], [134, 'Revolution Case', 'Insomnia', 'MAG-7', 'Field-Tested', 0.0, 1.0, '2', 0, 0, 0.23], [135, 'Revolution Case', 'Insomnia', 'MAG-7', 'Well-Worn', 0.0, 1.0, '2', 0, 0, 0.17], [136, 'Revolution Case', 'Insomnia', 'MAG-7', 'Battle-Scarred', 0.0, 1.0, '2', 0, 0, 0.17], [137, 'Revolution Case', 'Re.built', 'P250', 'Factory New', 0.0, 0.9, '2', 1, 0, 2.38], [138, 'Revolution Case', 'Re.built', 'P250', 'Minimal Wear', 0.0, 0.9, '2', 1, 0, 0.95], [139, 'Revolution Case', 'Re.built', 'P250', 'Field-Tested', 0.0, 0.9, '2', 1, 0, 0.39], [140, 'Revolution Case', 'Re.built', 'P250', 'Well-Worn', 0.0, 0.9, '2', 1, 0, 0.35], [141, 'Revolution Case', 'Re.built', 'P250', 'Battle-Scarred', 0.0, 0.9, '2', 1, 0, 0.3], [142, 'Revolution Case', 'Re.built', 'P250', 'Factory New', 0.0, 0.9, '2', 0, 0, 0.8], [143, 'Revolution Case', 'Re.built', 'P250', 'Minimal Wear', 0.0, 0.9, '2', 0, 0, 0.38], [144, 'Revolution Case', 'Re.built', 'P250', 'Field-Tested', 0.0, 0.9, '2', 0, 0, 0.23], [145, 'Revolution Case', 'Re.built', 'P250', 'Well-Worn', 0.0, 0.9, '2', 0, 0, 0.18], [146, 'Revolution Case', 'Re.built', 'P250', 'Battle-Scarred', 0.0, 0.9, '2', 0, 0, 0.17], [147, 'Revolution Case', 'Rebel', 'Tec-9', 'Factory New', 0.0, 1.0, '2', 1, 0, 2.21], [148, 'Revolution Case', 'Rebel', 'Tec-9', 'Minimal Wear', 0.0, 1.0, '2', 1, 0, 0.88], [149, 'Revolution Case', 'Rebel', 'Tec-9', 'Field-Tested', 0.0, 1.0, '2', 1, 0, 0.41], [150, 'Revolution Case', 'Rebel', 'Tec-9', 'Well-Worn', 0.0, 1.0, '2', 1, 0, 0.34], [151, 'Revolution Case', 'Rebel', 'Tec-9', 'Battle-Scarred', 0.0, 1.0, '2', 1, 0, 0.31], [152, 'Revolution Case', 'Rebel', 'Tec-9', 'Factory New', 0.0, 1.0, '2', 0, 0, 0.81], [153, 'Revolution Case', 'Rebel', 'Tec-9', 'Minimal Wear', 0.0, 1.0, '2', 0, 0, 0.37], [154, 'Revolution Case', 'Rebel', 'Tec-9', 'Field-Tested', 0.0, 1.0, '2', 0, 0, 0.23], [155, 'Revolution Case', 'Rebel', 'Tec-9', 'Well-Worn', 0.0, 1.0, '2', 0, 0, 0.16], [156, 'Revolution Case', 'Rebel', 'Tec-9', 'Battle-Scarred', 0.0, 1.0, '2', 0, 0, 0.17], [157, 'Revolution Case', 'Fragments', 'SCAR-20', 'Factory New', 0.0, 0.78, '2', 1, 0, 1.95], [158, 'Revolution Case', 'Fragments', 'SCAR-20', 'Minimal Wear', 0.0, 0.78, '2', 1, 0, 0.93], [159, 'Revolution Case', 'Fragments', 'SCAR-20', 'Field-Tested', 0.0, 0.78, '2', 1, 0, 0.39], [160, 'Revolution Case', 'Fragments', 'SCAR-20', 'Well-Worn', 0.0, 0.78, '2', 1, 0, 0.4], [161, 'Revolution Case', 'Fragments', 'SCAR-20', 'Battle-Scarred', 0.0, 0.78, '2', 1, 0, 0.3], [162, 'Revolution Case', 'Fragments', 'SCAR-20', 'Factory New', 0.0, 0.78, '2', 0, 0, 0.72], [163, 'Revolution Case', 'Fragments', 'SCAR-20', 'Minimal Wear', 0.0, 0.78, '2', 0, 0, 0.4], [164, 'Revolution Case', 'Fragments', 'SCAR-20', 'Field-Tested', 0.0, 0.78, '2', 0, 0, 0.23], [165, 'Revolution Case', 'Fragments', 'SCAR-20', 'Well-Worn', 0.0, 0.78, '2', 0, 0, 0.18], [166, 'Revolution Case', 'Fragments', 'SCAR-20', 'Battle-Scarred', 0.0, 0.78, '2', 0, 0, 0.15]]
response = tUH.getNextRarityLevelAveragePrice(revContainer, 4, 'Minimal Wear', False, 1)
print(response)