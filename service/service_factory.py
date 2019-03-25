from service.implements.cpu_service_imply import CpuServiceImply
from service.item_service import CpuService
class ServiceFactory:
    
    csi = CpuServiceImply()

    @staticmethod
    def getItemService() -> CpuService:
        return ServiceFactory.csi