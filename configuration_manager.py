import json

class Configuration_Manager():
    
    with open('config.json', 'r') as f:
        config = json.load(f)

    @staticmethod
    def get_checking_interval():
        """
        Returns time interval when checker service will be called (seconds)
        """
        return Configuration_Manager.config['checking_interval']
    
    @staticmethod
    def get_unreleased_time():
        """
        Returns time interval when diploma has prerelease state (days)
        """
        return Configuration_Manager.config['unreleased_time']

    @staticmethod
    def get_experts_count():
        """
        Returns minimal count of experts for release diploma
        """
        return Configuration_Manager.config['experts_count']