from LatLongServices import CSV, API, Mock

class LocationFactory:

    def getService(self,option):
        if option == 1:
            return CSV()
        elif option == 2:
            return API()
        elif option == 3:
            return Mock()
        else:
            return None