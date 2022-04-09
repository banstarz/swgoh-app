class ViewDefinitions():
    
    def __init__(self):
        pass

    def guild_players_with_column_names():
        sql_query = '''
        SELECT 
            guild_name as 'Guild Name',
            name as Player,
            allyCode as 'Ally Code',
            level as Level,
            gp as 'Galactic Power',
            gpChar as 'GP Char',
            gpShip as 'GP Ship',
            datetime as 'Last Updated'
        FROM
            guild_players
        '''

    def player_characters_roster_proper():
        sql_query = '''
        SELECT
            pr.allycode as 'Ally Code',
            pr.player as Player,
            --pr.character as 'Base Name',
            sc.game_name as Character,
            pr.level as Level,
            pr.gp as GP,
            pr.star as Stars,
            pr.gear as Gear,
            replace(pr.relic-2, -2, '') as Relic,
            replace(pr.zetas, 0, '') as Zetas,
            pr.datetime as 'Last Updated'
        FROM
            player_roster pr
        INNER JOIN
            swgoh_characters sc
        on pr.character = sc.base_name
        '''

    def player_ships_roster_proper():
        sql_query = '''
        SELECT
            pr.allycode as 'Ally Code',
            pr.player as Player,
            --pr.character as 'Base Name',
            ss.game_name as Character,
            pr.level as Level,
            pr.gp as GP,
            pr.star as Stars,
            pr.datetime as 'Last Updated'
        FROM
            player_roster pr
        INNER JOIN
            swgoh_ships ss
        on pr.character = ss.base_name
        '''
