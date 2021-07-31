import coc
import util
import io 

coc_dev_email = "beyondboyplays@gmail.com"  # Clash of Clans Developer Account email
coc_dev_password = "Munna370"  # Clash of Clans Developer Account password
fname="fullroster.csv"

async def main():
	roster = await util.get_full_roster(client)
	roster_data = await util.build_roster_table(client,roster)

	with io.open(fname, "w", encoding="utf-8") as f:
		f.write(roster_data)
	
client = coc.login(coc_dev_email ,coc_dev_password)
client.loop.run_until_complete(main())
#client.close()

