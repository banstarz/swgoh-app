from abc import abstractmethod, ABC

class ReportBuilder(ABC):
    
    @abstractmethod
    def _extract_data(self, allycode):
        pass
    
    @abstractmethod
    def _flatten_report(self):
        pass
    
    @abstractmethod
    def get_record(self, allycode):
        pass

class DatabaseManager:

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def upload_data(self, table, rows):
        pass

    @abstractmethod
    def extract_data(self, table, rows):
        pass