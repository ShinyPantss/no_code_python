import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
from supabase import create_client
import os


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


class DSpull:
    def __init__(self, api):
        self.url = api
        self.response = requests.get(api)

        
    def get(self, type = "dataset"):
      
        if self.response.status_code == 200:
            # Parse the response as JSON
            self.data = json.loads(self.response.text)
            df = pd.DataFrame(self.data["data"])
            
            columns = list(df.columns)
            indexes_of_id = [index for index, column in enumerate(columns) if "ID" in column]
            columns_filtered = [column for index, column in enumerate(columns) if index not in indexes_of_id]
            

            if type == "dataset":
                return df
            elif type == "columns":
                return columns_filtered
              
            return columns_filtered
          
        else:
            error = f"Request failed with status code {self.response.status_code}"
            return error
        
    def get_columns_updated_data(self);
        
        
        

    def update_columns_in_supabase(self, ):
        columns_filtered = self.get_columns()
        if isinstance(columns_filtered, list):
            
            response = supabase.table("DataSets").update({"dataColumnNames": columns_filtered}).eq("data_api", self.url).execute()
            return response.data, response.status_code
        else:
            return columns_filtered
        

# Example usage
def tester(url = "url"):
    # https://zircon.datausa.io/api/data?drilldowns=Year&measures=Average%20Wage&Workforce%20Status=true
    # Make a request to the API
    response = requests.get(url)

    # Ensure we got a valid response
    if response.status_code == 200:
        # Parse the response as JSON
        data = json.loads(response.text)
        
        # Extract the years and average wages
        years = [int(item['Year']) for item in data['data']]
        wages = [float(item['Average Wage']) for item in data['data']]
        
        # Create a line graph
        plt.plot(years, wages)
        plt.xlabel('Year')
        plt.ylabel('Average Wage')
        plt.title('Average Wage Over the Years')
        plt.show()
    else:
        print(f"Request failed with status code {response.status_code}")