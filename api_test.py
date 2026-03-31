import requests

def test_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url, timeout=5)
        
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("Success!")
            print("Response:", response.json())
        elif response.status_code == 404:
            print("Error: Resource not found")
        elif response.status_code == 500:
            print("Server Error")
        else:
            print("Unexpected status:", response.status_code)

    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed")
    except Exception as e:
        print("Unexpected error:", str(e))


if __name__ == "__main__":
    test_api()
