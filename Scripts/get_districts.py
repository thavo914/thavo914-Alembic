import requests
import json

def get_districts():
    url = "https://vn-public-apis.fpo.vn/districts/getAll?limit=-1"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Navigate through the nested structure
            if data['exitcode'] == 1 and 'data' in data:
                districts = data['data']['data']
                print(f"Found {len(districts)} districts:")
                for district in districts:
                    print("\nDistrict Details:")
                    for key, value in district.items():
                        print(f"{key}: {value}")
                    print("-" * 50)
                
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_districts()