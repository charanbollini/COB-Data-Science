import pandas as pd
import requests
def get_jokes(num_jokes=5):
  base_url="https://v2.jokeapi.dev/joke/Any"
  params={
      "type":"twopart",
      "amount":num_jokes
  }
  response=requests.get(base_url,params=params)
  data=response.json()
  if response.status_code==200:
    return data['jokes']
  else:
    print(f"error {response.status_code}:{data['error']}")
    return none

jokes_data=get_jokes()

if jokes_data:
  df=pd.DataFrame({
      'category':[joke['category']for joke in jokes_data],
       'setup':[joke['setup']for joke in jokes_data],
       'delivery':[joke['delivery']for joke in jokes_data],

  })
  df.to_csv('jokes_data.csv',index=False)
  print("csv dataset created successfully")
else:
  print("Failed to fetch jokes data")
