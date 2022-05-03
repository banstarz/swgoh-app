from .ReportBuilders.GuildPlayers import GuildPlayersReportBuilder
from .ReportBuilders.PlayerRoster import PlayerRosterReportBuilder
from .ReportBuilders.SwgohCharacters import SwgohCharactersReportBuilder
from .ReportBuilders.SwgohShips import SwgohShipsReportBuilder


class ReportBuildersManager:
    
    def __init__(self, report_name, cred = []):
        self.BUILDER_BY_REPORT = {
            'guild_players': GuildPlayersReportBuilder,
            'player_roster': PlayerRosterReportBuilder,
            'swgoh_characters': SwgohCharactersReportBuilder,
            'swgoh_ships': SwgohShipsReportBuilder
        }
        self.report_builder = self.BUILDER_BY_REPORT.get(report_name)(cred)
        self.tablename = self.report_builder.TABLE_NAME

    def get_api_name(self):
        return self.report_builder.client.api_name

    def refresh_access_token(self):
        return self.report_builder.client.auth()

    def get_flattened_data_iterator(self):
        return self.report_builder.get_record

    def report_structure(self):
        return self.report_builder.report_structure()
    
