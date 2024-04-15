import requests
import json
import matplotlib.pyplot as plt

class DSpull:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.data = json.loads(self.response.text)
        

    

    def get_data(self):
        if self.response.status_code == 200:
            # Parse the response as JSON
            self.data = json.loads(self.response.text)
            
            # Extract the years and average wages
            years = [int(item['Year']) for item in self.data['data']]
            wages = [float(item['Average Wage']) for item in self.data['data']]
            
            return self.data
        
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