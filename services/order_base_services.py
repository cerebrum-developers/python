from abc import ABC, abstractmethod


class OrderBaseService(ABC):

    @abstractmethod
    def get_all_order_shipments_list_with_pagination(self):
        pass

    @abstractmethod
    def get_order_shipments_list(self):
        pass

    

