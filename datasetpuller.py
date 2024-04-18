import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

class DSpull:
    def __init__(self, api):
        self.url = api
        self.response = requests.get(api)


    def get_columns(self):
        if self.response.status_code == 200:
            # Parse the response as JSON
            self.data = json.loads(self.response.text)
            df = pd.DataFrame(self.data["data"])
            # self.data includes the keys "data" and "source" so we need to access the "data" key to get the actual data

            columns = list(df.columns) # type of df.columns is pandas.core.indexes.base.Index, so we convert it to a list
            
            indexesOFID = [index for index in range(len(columns)) if "ID" in columns[index]]            
            # indexesOFID includes the indexes of the columns that have "ID" in their name  
                            
            columns_filtered = [columns[i] for i in range(len(columns)) if i not in indexesOFID]
            # above line removes the columns that have "ID" in their name from the list of columns
            
            return columns_filtered

        else:
            error = f"Request failed with status code {self.response.status_code}"
            
            return error

# Example usage
def tester(url = "https://zircon.datausa.io/api/data?drilldowns=Year&measures=Average%20Wage&Workforce%20Status=true"):
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