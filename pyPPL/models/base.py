import json
import xmltodict

class SerializableObject:
    
    def to_xml(self):
        """
        Convert object to XML
        """
        if self.xml_mapping is None:
            raise NotImplementedError('xml_mapping is not implemented')
        json_dict = json.dumps({self.xml_mapping.get(k, k): v for k, v in self.__dict__.items()})
        return xmltodict.unparse(json_dict, pretty=True, full_document=False)
