import coc
import creds

from discord.ext import commands

CLAN_TAG = creds.clan_tag
WAR_REPORT_CHANNEL_ID = creds.war_channel

REPORT_STYLE = """
{att.attacker.name} (No. {att.attacker.map_position}, TH{att.attacker.town_hall}) just {verb} {att.defender.name} 
(No. {att.defender.map_position}, TH{att.defender.town_hall}) for {att.stars} stars and {att.destruction}%.
"""


class WarReporter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.bot.coc.add_events(
            self.on_war_attack,
            self.on_war_state_change
        )
        self.bot.coc.add_war_updates(CLAN_TAG)

    def cog_unload(self):
        self.bot.coc.remove_events(
            self.on_war_attack,
            self.on_war_state_change
        )
        self.bot.coc.stop_updates("war")

    @property
    def report_channel(self):
        return self.bot.get_chanel(WAR_REPORT_CHANNEL_ID)

    @coc.WarEvents.war_attack()
    async def on_war_attack(self, attack, war):
        if attack.attacker.is_opponenet:
            verb = "defended"
        else:
            verb = "attacked"

        await self.report_channel.send(REPORT_STYLE.format(att=attack, verb=verb))

    @coc.WarEvents.state()
    async def on_war_state_change(self, current_state, war):
        await self.report_channel.send("{0.clan.name} just entered {1} state!".format(war, current_state))


def setup(bot):
    bot.add_cog(WarReporter(bot))
