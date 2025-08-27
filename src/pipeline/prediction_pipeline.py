import sys
from src.entity.config_entity import VehiclePredictionConfig
from src.entity.s3_estimator import VehicleInsuraceEstimator
from src.exception import MyException
from src.logger import logging
from pandas import DataFrame


class VehicleData:
    def __init__(self, Gender, Age, Driving_License, Region_Code, Previously_Insured, Annual_Premium, Policy_Sales_Channel, Vintage, Vehicle_Age_lt_1_Year, Vehicle_Age_gt_2_Years, Vehicle_Damage_Yes):
        
        try:
            self.Gender = Gender
            self.Age = Age
            self.Driving_License = Driving_License
            self.Region_Code = Region_Code
            self.Previously_Insured = Previously_Insured
            self.Annual_Premium = Annual_Premium
            self.Policy_Sales_Channel = Policy_Sales_Channel
            self.Vintage = Vintage
            self.Vehicle_Age_lt_1_Year = Vehicle_Age_lt_1_Year
            self.Vehicle_Age_gt_2_Years = Vehicle_Age_gt_2_Years
            self.Vehicle_Damage_Yes = Vehicle_Damage_Yes

        except Exception as e:
            raise MyException(e, sys) from e
        
    def get_vehicle_data_as_dict(self):

        logging.info("Entered get vehicle data as dict method in VehicleData class")

        try:
            input_data = {
                "Gender": [self.Gender],
                "Age": [self.Age],
                "Driving_License": [self.Driving_License],
                "Region_Code": [self.Region_Code],
                "Previously_Insured": [self.Previously_Insured],
                "Annual_Premium": [self.Annual_Premium],
                "Policy_Sales_Channel": [self.Policy_Sales_Channel],
                "Vintage": [self.Vintage],
                "Vehicle_Age_lt_1_Year": [self.Vehicle_Age_lt_1_Year],
                "Vehicle_Age_gt_2_Years": [self.Vehicle_Age_gt_2_Years],
                "Vehicle_Damage_Yes": [self.Vehicle_Damage_Yes]
            }

            logging.info("Created vehicle data dict")
            return input_data

        except Exception as e:
            raise MyException(e, sys) from e
    
    
    def get_vehicle_input_data_frame(self)-> DataFrame:

        try:
            vehicle_input_dict = self.get_vehicle_data_as_dict()
            return DataFrame(vehicle_input_dict)
        
        except Exception as e:
            raise MyException(e, sys) from e
    
class VehicleDataClassifier:

    def __init__(self, prediction_pipeline_config: VehiclePredictionConfig= VehiclePredictionConfig()) -> None:
        
        try:
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise MyException(e, sys) from e
        
    def predict(self, dataframe) -> str:

        try:
            logging.info("Entering predict method of VehicleDataClassifier class")

            model = VehicleInsuraceEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path
            )

            result = model.predict(dataframe)

            return result
        
        except Exception as e:
            raise MyException(e, sys) from e