import sys, json
from datetime import datetime
# Do task_2 request body
b = """{
    "rangeEnd": "2020-09-06T00:00:00",
    "rangeStart": "2020-09-02T00:00:00",
    "graphs": [
        {
            "formula": "CPULoad5min*10"
        }
    ],
    "df": {
        "CPULoad5min": {
            "index": [
                "2020-09-02T00:01:49",
                "2020-09-02T00:06:37",
                "2020-09-02T00:11:36",
                "2020-09-02T00:16:54",
                "2020-09-02T00:21:35",
                "2020-09-02T00:26:32"
            ],
            "values": [
                123,
                112,
                78,
                111,
                111,
                95
            ]
        }
    }
}"""
data_input = json.loads(b) # загружаем запрос в объект
data_out = []
for item in data_input["df"]["CPULoad5min"]["index"]: 
	data = datetime.strptime(item, '%Y-%m-%dT%H:%M:%S') # читаем дату из строки в объект
	exec(list(data_input["df"])[0] + ' = datetime.timestamp(data)') # переводим в секунды
	item_sec = eval(data_input["graphs"][0]["formula"]) # и вычисляем по формуле
	data_out.append(datetime.isoformat(datetime.fromtimestamp(item_sec)))	# переводим обрратно в iso формат и добавляем в массив			
result = json.dumps(data_out)  # сохраняем в json
print(result)
