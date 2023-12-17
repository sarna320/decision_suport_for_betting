from events import find_events_live_and_today, find_events_next
from leagues import find_leagues

leagues = find_leagues()
for i in range(len(leagues["name"])):
    print(f'{i}:{leagues["name"][i]} link: {leagues["link"][i]}')

print("")
print("Live and today events")
events_live_and_today = find_events_live_and_today(leagues["link"][0])
for i in events_live_and_today:
    print(i)

print("")
print("Future events:")
events_next = find_events_next(leagues["link"][0])
for i in events_next:
    print(i)
print("")
