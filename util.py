import wookieforce
'''
All clans, All names, TH, Current location.
'''
async def get_full_roster(client):
	roster = {}
	clans = wookieforce.all_clans()
	for clan_name in clans:
		clan = await client.get_clan(clans[clan_name])
		print('Clan Name:',clan)
		members = await get_members(client,clan)
		roster.update([(clan_name, members)])
	return roster

'''
Get all Clan Members for a given clan
'''
async def get_members(client,clan):
	members = []
	async for member in clan.get_detailed_members():
		members.append(member)
	return members


'''
Building a table to display member data
'''
async def build_roster_table(client,roster):
	roster_data = 'PlayerTag,PlayerName,Attacks,Clan\n'
	for clan in roster:
		players = roster[clan]
		for i in range(len(players)):
			player = players[i]
			#TEST
			roster_data += str(player.tag) + ','
			roster_data += str(player.name) + ','
			roster_data += str(coc.ClanWar.members.attacks) + ','
            roster_data += str(war = await client.get_current_war('clan_tag')) + ','
            roster_data += str(member = war.get_member('player_tag')) + ','
			roster_data += str(player.clan) + '\n'
			#TEST

	return roster_data
