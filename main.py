from events import find_all_events
from leagues import find_leagues

leagues = find_leagues()
events = find_all_events(leagues["link"][0])
for i in range(len(leagues["name"])):
    print(f'League:{leagues["name"][i]} link: {leagues["link"][i]}')
print("")
for i in range(len(events["home"])):
    print(f'{events["home"][i]} vs {events["away"][i]} link: {events["link"][i]}')
