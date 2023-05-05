import json
import requests
import statistics

MeanSampleSize : int = 10
 
def loadRelicData() -> list[dict] :
	with open('relic_data.json') as json_file:
		data = json.load(json_file)
		return data
		
def keepResult(result : dict) -> bool :
	if result["visible"] == False:
		return False
	if result["user"]["status"] != "ingame":
		return False
	return True

def computeValue(rawResults : list[dict]) -> float :
	return

def computeItemValue(urlTemplate : str, itemString : str) -> float :
	response : dict =  requests.get(urlTemplate % itemString).json()
	rawResults : list[dict] = response["payload"]["orders"]
	filteredResults : list [dict] = [d for d in results if keepResult(d)]
	orderedResults : list[dict] = sorted(filteredResults, key = lambda d : d["platinum"])
	finalResults : list [dict] = orderedResults[0:MeanSampleSize]
	return statistics.mean(finalResults)


def main() -> None :
	relicData : list[dict] = loadRelicData()
	relics : list[str] = None
	marketUrl: str = "https://api.warframe.market/v1/items/%s/orders"
	print(computeItemValue(marketUrl, "abating_link"))
	return

if __name__ == "__main__":
	main()