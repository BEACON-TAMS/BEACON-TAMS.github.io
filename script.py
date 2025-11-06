import pandas as pd

events = pd.read_csv("events.csv")

cards = ""

for i in range(len(events)):
    print(events.loc[i])
    cards += f"""
    <div class="timeline-5 right-5">
		<div class="card">
			<div class="card-body p-4">
				<h5>{events.loc[i]["name"]}</h5>
				<span class="small text-muted"><i class="fas fa-clock me-1"></i>{events.loc[i]["date"]}, {events.loc[i]["time"]}, {events.loc[i]["place"]}</span>
				<p class="mt-2 mb-0">
					{events.loc[i]["desc"]}
				</p>
			</div>
		</div>
	</div>
    """

with open("timeline.html", "r") as f:
    html = f.read()
    f.close()
    
with open("timeline.html", "w") as f:
    loc = html.find("<!-- CARDS HERE -->")
    out = html[:loc] + cards + html[loc:]
    f.write(out)
    f.close()