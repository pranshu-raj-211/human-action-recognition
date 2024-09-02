import yaml

column_names = [
    "MILLISEC",
    "Accelerometer RKN^ accX",
    "Accelerometer RKN^ accY",
    "Accelerometer RKN^ accZ",
    "Accelerometer HIP accX",
    "Accelerometer HIP accY",
    "Accelerometer HIP accZ",
    "Accelerometer LUA^ accX",
    "Accelerometer LUA^ accY",
    "Accelerometer LUA^ accZ",
    "Accelerometer RUA_ accX",
    "Accelerometer RUA_ accY",
    "Accelerometer RUA_ accZ",
    "Accelerometer LH accX",
    "Accelerometer LH accY",
    "Accelerometer LH accZ",
    "Accelerometer BACK accX",
    "Accelerometer BACK accY",
    "Accelerometer BACK accZ",
    "Accelerometer RKN_ accX",
    "Accelerometer RKN_ accY",
    "Accelerometer RKN_ accZ",
    "Accelerometer RWR accX",
    "Accelerometer RWR accY",
    "Accelerometer RWR accZ",
    "Accelerometer RUA^ accX",
    "Accelerometer RUA^ accY",
    "Accelerometer RUA^ accZ",
    "Accelerometer LUA_ accX",
    "Accelerometer LUA_ accY",
    "Accelerometer LUA_ accZ",
    "Accelerometer LWR accX",
    "Accelerometer LWR accY",
    "Accelerometer LWR accZ",
    "Accelerometer RH accX",
    "Accelerometer RH accY",
    "Accelerometer RH accZ",
    "InertialMeasurementUnit BACK accX",
    "InertialMeasurementUnit BACK accY",
    "InertialMeasurementUnit BACK accZ",
    "InertialMeasurementUnit BACK gyroX",
    "InertialMeasurementUnit BACK gyroY",
    "InertialMeasurementUnit BACK gyroZ",
    "InertialMeasurementUnit BACK magneticX",
    "InertialMeasurementUnit BACK magneticY",
    "InertialMeasurementUnit BACK magneticZ",
    "InertialMeasurementUnit BACK Quaternion1",
    "InertialMeasurementUnit BACK Quaternion2",
    "InertialMeasurementUnit BACK Quaternion3",
    "InertialMeasurementUnit BACK Quaternion4",
    "InertialMeasurementUnit RUA accX",
    "InertialMeasurementUnit RUA accY",
    "InertialMeasurementUnit RUA accZ",
    "InertialMeasurementUnit RUA gyroX",
    "InertialMeasurementUnit RUA gyroY",
    "InertialMeasurementUnit RUA gyroZ",
    "InertialMeasurementUnit RUA magneticX",
    "InertialMeasurementUnit RUA magneticY",
    "InertialMeasurementUnit RUA magneticZ",
    "InertialMeasurementUnit RUA Quaternion1",
    "InertialMeasurementUnit RUA Quaternion2",
    "InertialMeasurementUnit RUA Quaternion3",
    "InertialMeasurementUnit RUA Quaternion4",
    "InertialMeasurementUnit RLA accX",
    "InertialMeasurementUnit RLA accY",
    "InertialMeasurementUnit RLA accZ",
    "InertialMeasurementUnit RLA gyroX",
    "InertialMeasurementUnit RLA gyroY",
    "InertialMeasurementUnit RLA gyroZ",
    "InertialMeasurementUnit RLA magneticX",
    "InertialMeasurementUnit RLA magneticY",
    "InertialMeasurementUnit RLA magneticZ",
    "InertialMeasurementUnit RLA Quaternion1",
    "InertialMeasurementUnit RLA Quaternion2",
    "InertialMeasurementUnit RLA Quaternion3",
    "InertialMeasurementUnit RLA Quaternion4",
    "InertialMeasurementUnit LUA accX",
    "InertialMeasurementUnit LUA accY",
    "InertialMeasurementUnit LUA accZ",
    "InertialMeasurementUnit LUA gyroX",
    "InertialMeasurementUnit LUA gyroY",
    "InertialMeasurementUnit LUA gyroZ",
    "InertialMeasurementUnit LUA magneticX",
    "InertialMeasurementUnit LUA magneticY",
    "InertialMeasurementUnit LUA magneticZ",
    "InertialMeasurementUnit LUA Quaternion1",
    "InertialMeasurementUnit LUA Quaternion2",
    "InertialMeasurementUnit LUA Quaternion3",
    "InertialMeasurementUnit LUA Quaternion4",
    "InertialMeasurementUnit LLA accX",
    "InertialMeasurementUnit LLA accY",
    "InertialMeasurementUnit LLA accZ",
    "InertialMeasurementUnit LLA gyroX",
    "InertialMeasurementUnit LLA gyroY",
    "InertialMeasurementUnit LLA gyroZ",
    "InertialMeasurementUnit LLA magneticX",
    "InertialMeasurementUnit LLA magneticY",
    "InertialMeasurementUnit LLA magneticZ",
    "InertialMeasurementUnit LLA Quaternion1",
    "InertialMeasurementUnit LLA Quaternion2",
    "InertialMeasurementUnit LLA Quaternion3",
    "InertialMeasurementUnit LLA Quaternion4",
    "InertialMeasurementUnit L-SHOE EuX",
    "InertialMeasurementUnit L-SHOE EuY",
    "InertialMeasurementUnit L-SHOE EuZ",
    "InertialMeasurementUnit L-SHOE Nav_Ax",
    "InertialMeasurementUnit L-SHOE Nav_Ay",
    "InertialMeasurementUnit L-SHOE Nav_Az",
    "InertialMeasurementUnit L-SHOE Body_Ax",
    "InertialMeasurementUnit L-SHOE Body_Ay",
    "InertialMeasurementUnit L-SHOE Body_Az",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameX",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameY",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameZ",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameX",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameY",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameZ",
    "InertialMeasurementUnit L-SHOE Compass",
    "InertialMeasurementUnit R-SHOE EuX",
    "InertialMeasurementUnit R-SHOE EuY",
    "InertialMeasurementUnit R-SHOE EuZ",
    "InertialMeasurementUnit R-SHOE Nav_Ax",
    "InertialMeasurementUnit R-SHOE Nav_Ay",
    "InertialMeasurementUnit R-SHOE Nav_Az",
    "InertialMeasurementUnit R-SHOE Body_Ax",
    "InertialMeasurementUnit R-SHOE Body_Ay",
    "InertialMeasurementUnit R-SHOE Body_Az",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameX",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameY",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameZ",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameX",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameY",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameZ",
    "InertialMeasurementUnit R-SHOE Compass",
    "Accelerometer CUP accX",
    "Accelerometer CUP accY",
    "Accelerometer CUP accZ",
    "Accelerometer CUP gyroX",
    "Accelerometer CUP gyroY",
    "Accelerometer SALAMI accX",
    "Accelerometer SALAMI accY",
    "Accelerometer SALAMI accZ",
    "Accelerometer SALAMI gyroX",
    "Accelerometer SALAMI gyroY",
    "Accelerometer WATER accX",
    "Accelerometer WATER accY",
    "Accelerometer WATER accZ",
    "Accelerometer WATER gyroX",
    "Accelerometer WATER gyroY",
    "Accelerometer CHEESE accX",
    "Accelerometer CHEESE accY",
    "Accelerometer CHEESE accZ",
    "Accelerometer CHEESE gyroX",
    "Accelerometer CHEESE gyroY",
    "Accelerometer BREAD accX",
    "Accelerometer BREAD accY",
    "Accelerometer BREAD accZ",
    "Accelerometer BREAD gyroX",
    "Accelerometer BREAD gyroY",
    "Accelerometer KNIFE1 accX",
    "Accelerometer KNIFE1 accY",
    "Accelerometer KNIFE1 accZ",
    "Accelerometer KNIFE1 gyroX",
    "Accelerometer KNIFE1 gyroY",
    "Accelerometer MILK accX",
    "Accelerometer MILK accY",
    "Accelerometer MILK accZ",
    "Accelerometer MILK gyroX",
    "Accelerometer MILK gyroY",
    "Accelerometer SPOON accX",
    "Accelerometer SPOON accY",
    "Accelerometer SPOON accZ",
    "Accelerometer SPOON gyroX",
    "Accelerometer SPOON gyroY",
    "Accelerometer SUGAR accX",
    "Accelerometer SUGAR accY",
    "Accelerometer SUGAR accZ",
    "Accelerometer SUGAR gyroX",
    "Accelerometer SUGAR gyroY",
    "Accelerometer KNIFE2 accX",
    "Accelerometer KNIFE2 accY",
    "Accelerometer KNIFE2 accZ",
    "Accelerometer KNIFE2 gyroX",
    "Accelerometer KNIFE2 gyroY",
    "Accelerometer PLATE accX",
    "Accelerometer PLATE accY",
    "Accelerometer PLATE accZ",
    "Accelerometer PLATE gyroX",
    "Accelerometer PLATE gyroY",
    "Accelerometer GLASS accX",
    "Accelerometer GLASS accY",
    "Accelerometer GLASS accZ",
    "Accelerometer GLASS gyroX",
    "Accelerometer GLASS gyroY",
    "REED SWITCH DISHWASHER S1",
    "REED SWITCH FRIDGE S3",
    "REED SWITCH FRIDGE S2",
    "REED SWITCH FRIDGE S1",
    "REED SWITCH MIDDLEDRAWER S1",
    "REED SWITCH MIDDLEDRAWER S2",
    "REED SWITCH MIDDLEDRAWER S3",
    "REED SWITCH LOWERDRAWER S3",
    "REED SWITCH LOWERDRAWER S2",
    "REED SWITCH UPPERDRAWER",
    "REED SWITCH DISHWASHER S3",
    "REED SWITCH LOWERDRAWER S1",
    "REED SWITCH DISHWASHER S2",
    "Accelerometer DOOR1 accX",
    "Accelerometer DOOR1 accY",
    "Accelerometer DOOR1 accZ",
    "Accelerometer LAZYCHAIR accX",
    "Accelerometer LAZYCHAIR accY",
    "Accelerometer LAZYCHAIR accZ",
    "Accelerometer DOOR2 accX",
    "Accelerometer DOOR2 accY",
    "Accelerometer DOOR2 accZ",
    "Accelerometer DISHWASHER accX",
    "Accelerometer DISHWASHER accY",
    "Accelerometer DISHWASHER accZ",
    "Accelerometer UPPERDRAWER accX",
    "Accelerometer UPPERDRAWER accY",
    "Accelerometer UPPERDRAWER accZ",
    "Accelerometer LOWERDRAWER accX",
    "Accelerometer LOWERDRAWER accY",
    "Accelerometer LOWERDRAWER accZ",
    "Accelerometer MIDDLEDRAWER accX",
    "Accelerometer MIDDLEDRAWER accY",
    "Accelerometer MIDDLEDRAWER accZ",
    "Accelerometer FRIDGE accX",
    "Accelerometer FRIDGE accY",
    "Accelerometer FRIDGE accZ",
    "LOCATION TAG1 X",
    "LOCATION TAG1 Y",
    "LOCATION TAG1 Z",
    "LOCATION TAG2 X",
    "LOCATION TAG2 Y",
    "LOCATION TAG2 Z",
    "LOCATION TAG3 X",
    "LOCATION TAG3 Y",
    "LOCATION TAG3 Z",
    "LOCATION TAG4 X",
    "LOCATION TAG4 Y",
    "LOCATION TAG4 Z",
    "Locomotion",
    "HL_Activity",
    "LL_Left_Arm",
    "LL_Left_Arm_Object",
    "LL_Right_Arm",
    "LL_Right_Arm_Object",
    "ML_Both_Arms",
]
# misnomer really, contains the locomotion target variable as well
feature_columns = [
    "InertialMeasurementUnit BACK accX",
    "InertialMeasurementUnit BACK accY",
    "InertialMeasurementUnit BACK accZ",
    "InertialMeasurementUnit BACK gyroX",
    "InertialMeasurementUnit BACK gyroY",
    "InertialMeasurementUnit BACK gyroZ",
    "InertialMeasurementUnit BACK magneticX",
    "InertialMeasurementUnit BACK magneticY",
    "InertialMeasurementUnit BACK magneticZ",
    "InertialMeasurementUnit RUA accX",
    "InertialMeasurementUnit RUA accY",
    "InertialMeasurementUnit RUA accZ",
    "InertialMeasurementUnit RUA gyroX",
    "InertialMeasurementUnit RUA gyroY",
    "InertialMeasurementUnit RUA gyroZ",
    "InertialMeasurementUnit RUA magneticX",
    "InertialMeasurementUnit RUA magneticY",
    "InertialMeasurementUnit RUA magneticZ",
    "InertialMeasurementUnit RLA accX",
    "InertialMeasurementUnit RLA accY",
    "InertialMeasurementUnit RLA accZ",
    "InertialMeasurementUnit RLA gyroX",
    "InertialMeasurementUnit RLA gyroY",
    "InertialMeasurementUnit RLA gyroZ",
    "InertialMeasurementUnit RLA magneticX",
    "InertialMeasurementUnit RLA magneticY",
    "InertialMeasurementUnit RLA magneticZ",
    "InertialMeasurementUnit LUA accX",
    "InertialMeasurementUnit LUA accY",
    "InertialMeasurementUnit LUA accZ",
    "InertialMeasurementUnit LUA gyroX",
    "InertialMeasurementUnit LUA gyroY",
    "InertialMeasurementUnit LUA gyroZ",
    "InertialMeasurementUnit LUA magneticX",
    "InertialMeasurementUnit LUA magneticY",
    "InertialMeasurementUnit LUA magneticZ",
    "InertialMeasurementUnit LLA accX",
    "InertialMeasurementUnit LLA accY",
    "InertialMeasurementUnit LLA accZ",
    "InertialMeasurementUnit LLA gyroX",
    "InertialMeasurementUnit LLA gyroY",
    "InertialMeasurementUnit LLA gyroZ",
    "InertialMeasurementUnit LLA magneticX",
    "InertialMeasurementUnit LLA magneticY",
    "InertialMeasurementUnit LLA magneticZ",
    "InertialMeasurementUnit L-SHOE EuX",
    "InertialMeasurementUnit L-SHOE EuY",
    "InertialMeasurementUnit L-SHOE EuZ",
    "InertialMeasurementUnit L-SHOE Nav_Ax",
    "InertialMeasurementUnit L-SHOE Nav_Ay",
    "InertialMeasurementUnit L-SHOE Nav_Az",
    "InertialMeasurementUnit L-SHOE Body_Ax",
    "InertialMeasurementUnit L-SHOE Body_Ay",
    "InertialMeasurementUnit L-SHOE Body_Az",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameX",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameY",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameZ",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameX",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameY",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameZ",
    "InertialMeasurementUnit L-SHOE Compass",
    "InertialMeasurementUnit R-SHOE EuX",
    "InertialMeasurementUnit R-SHOE EuY",
    "InertialMeasurementUnit R-SHOE EuZ",
    "InertialMeasurementUnit R-SHOE Nav_Ax",
    "InertialMeasurementUnit R-SHOE Nav_Ay",
    "InertialMeasurementUnit R-SHOE Nav_Az",
    "InertialMeasurementUnit R-SHOE Body_Ax",
    "InertialMeasurementUnit R-SHOE Body_Ay",
    "InertialMeasurementUnit R-SHOE Body_Az",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameX",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameY",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameZ",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameX",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameY",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameZ",
    "InertialMeasurementUnit R-SHOE Compass",
    "Locomotion",
]

# this one is comprised entirely of features
body_features_raw = [
    "InertialMeasurementUnit BACK accX",
    "InertialMeasurementUnit BACK accY",
    "InertialMeasurementUnit BACK accZ",
    "InertialMeasurementUnit BACK gyroX",
    "InertialMeasurementUnit BACK gyroY",
    "InertialMeasurementUnit BACK gyroZ",
    "InertialMeasurementUnit BACK magneticX",
    "InertialMeasurementUnit BACK magneticY",
    "InertialMeasurementUnit BACK magneticZ",
    "InertialMeasurementUnit RUA accX",
    "InertialMeasurementUnit RUA accY",
    "InertialMeasurementUnit RUA accZ",
    "InertialMeasurementUnit RUA gyroX",
    "InertialMeasurementUnit RUA gyroY",
    "InertialMeasurementUnit RUA gyroZ",
    "InertialMeasurementUnit RUA magneticX",
    "InertialMeasurementUnit RUA magneticY",
    "InertialMeasurementUnit RUA magneticZ",
    "InertialMeasurementUnit RLA accX",
    "InertialMeasurementUnit RLA accY",
    "InertialMeasurementUnit RLA accZ",
    "InertialMeasurementUnit RLA gyroX",
    "InertialMeasurementUnit RLA gyroY",
    "InertialMeasurementUnit RLA gyroZ",
    "InertialMeasurementUnit RLA magneticX",
    "InertialMeasurementUnit RLA magneticY",
    "InertialMeasurementUnit RLA magneticZ",
    "InertialMeasurementUnit LUA accX",
    "InertialMeasurementUnit LUA accY",
    "InertialMeasurementUnit LUA accZ",
    "InertialMeasurementUnit LUA gyroX",
    "InertialMeasurementUnit LUA gyroY",
    "InertialMeasurementUnit LUA gyroZ",
    "InertialMeasurementUnit LUA magneticX",
    "InertialMeasurementUnit LUA magneticY",
    "InertialMeasurementUnit LUA magneticZ",
    "InertialMeasurementUnit LLA accX",
    "InertialMeasurementUnit LLA accY",
    "InertialMeasurementUnit LLA accZ",
    "InertialMeasurementUnit LLA gyroX",
    "InertialMeasurementUnit LLA gyroY",
    "InertialMeasurementUnit LLA gyroZ",
    "InertialMeasurementUnit LLA magneticX",
    "InertialMeasurementUnit LLA magneticY",
    "InertialMeasurementUnit LLA magneticZ",
    "InertialMeasurementUnit L-SHOE EuX",
    "InertialMeasurementUnit L-SHOE EuY",
    "InertialMeasurementUnit L-SHOE EuZ",
    "InertialMeasurementUnit L-SHOE Nav_Ax",
    "InertialMeasurementUnit L-SHOE Nav_Ay",
    "InertialMeasurementUnit L-SHOE Nav_Az",
    "InertialMeasurementUnit L-SHOE Body_Ax",
    "InertialMeasurementUnit L-SHOE Body_Ay",
    "InertialMeasurementUnit L-SHOE Body_Az",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameX",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameY",
    "InertialMeasurementUnit L-SHOE AngVelBodyFrameZ",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameX",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameY",
    "InertialMeasurementUnit L-SHOE AngVelNavFrameZ",
    "InertialMeasurementUnit L-SHOE Compass",
    "InertialMeasurementUnit R-SHOE EuX",
    "InertialMeasurementUnit R-SHOE EuY",
    "InertialMeasurementUnit R-SHOE EuZ",
    "InertialMeasurementUnit R-SHOE Nav_Ax",
    "InertialMeasurementUnit R-SHOE Nav_Ay",
    "InertialMeasurementUnit R-SHOE Nav_Az",
    "InertialMeasurementUnit R-SHOE Body_Ax",
    "InertialMeasurementUnit R-SHOE Body_Ay",
    "InertialMeasurementUnit R-SHOE Body_Az",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameX",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameY",
    "InertialMeasurementUnit R-SHOE AngVelBodyFrameZ",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameX",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameY",
    "InertialMeasurementUnit R-SHOE AngVelNavFrameZ",
    "InertialMeasurementUnit R-SHOE Compass",
]


def dump_to_yaml_file(data, filename: str) -> None:
    with open(filename, "w") as file:
        yaml.dump(data, file, sort_keys=False)


dump_to_yaml_file(column_names, "unique_column_names.yaml")
dump_to_yaml_file(feature_columns, "locomotion_set.yaml")
dump_to_yaml_file(body_features_raw, "body_features.yaml")
