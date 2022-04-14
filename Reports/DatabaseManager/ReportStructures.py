class ReportStructures:
    GUILD_PLAYERS = {
        'guild_name': 'varvhar(255)',
        'name': 'varvhar(255)',
        'allyCode': 'int',
        'level': 'int',
        'gp': 'int',
        'gpChar': 'int',
        'gpShip': 'int',
        'datetime': 'date'
    }

    PLAYER_ROSTER = {
        'allycode': 'int',
        'player': 'varchar(255)',
        'character': 'varchar(255)',
        'level': 'int',
        'gp': 'int',
        'star': 'int',
        'gear': 'int',
        'relic': 'int',
        'zetas': 'int',
        'datetime': 'date'
    }

    SWGOH_CHARACTERS = {
        'game_name': 'varchar(255)',
        'base_name': 'varchar(255)',
        'datetime': 'date'
    }

    SWGOH_SHIPS = {
        'game_name': 'varchar(255)',
        'base_name': 'varchar(255)',
        'datetime': 'date'
    }