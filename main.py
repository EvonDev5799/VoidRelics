import json
 
def loadRelicData() -> list[dict] :
	with open('relic_data.json') as json_file:
		data = json.load(json_file)
		return data
	
def computeItemValue(urlTemplate : str, itemString) -> float :
	return
	
def main() -> None :
	relicData : list[dict] = loadRelicData()
	relics : list[str] = None
	marketUrl: str = "https://api.warframe.market/v1/items/%s/orders"
	return

if __name__ == "__main__":
	main()