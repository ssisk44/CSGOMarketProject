class createDBAssets:
    def getCreateStaticSchemaScript(self):
        # create schema static_data
        sql = "CREATE DATABASE `static_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;"
        return sql

    def getCreateDynamicSchemaScript(self):
       # create schema static_data
       sql = "CREATE DATABASE `dynamic_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;"
       return sql


    # def getCreateItemsTableScript(self):
    #     # show create table static_data.items
    #     sql = "CREATE TABLE `static_data.items` ( \
    #         `itemID` int NOT NULL, \
    #         `itemType` varchar(14) NOT NULL, \
    #         `itemMarketName` varchar(64) NOT NULL, \
    #         `itemMedianPrice` varchar(8) DEFAULT NULL, \
    #         `itemIsStatrak` tinyint DEFAULT '0', \
    #         `itemWearValue` varchar(16) DEFAULT NULL, \
    #         PRIMARY KEY (`itemID`), \
    #         UNIQUE KEY `itemID_UNIQUE` (`itemID`) \
    #       ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
    #     return sql

    def getCreateWearTableScript(self):
        """"rarityID","rarityName"
            0,"Covert"
            1,"Classified"
            2,"Restricted"
            3,"Mil-Spec"
            4,"Industrial Grade"
            5,"Consumer Grade"

            "wearID","wearName","wearFloatMin","wearFloatMax"
            0,"Factory New",0.0,0.07
            1,"Minimal Wear",0.07,0.15
            2,"Field-Tested",0.15,0.38
            3,"Well-Worn",0.38,0.45
            4,"Battle-Scarred",0.45,1.0
        """
        sql = "CREATE TABLE `wear` ( \
           `w_id` int NOT NULL, \
           `w_name` varchar(16) NOT NULL, \
           `w_float_min` float NOT NULL, \
           `w_float_max` float NOT NULL, \
           PRIMARY KEY (`wearID`) \
         ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
        return sql

    def populateItemsTableScript(self):
        sql = "INSERT INTO static_data.wear (w_id, w_name, w_float_min, w_float_max) VALUES"
        # do this later... waste of time



