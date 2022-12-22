import json
import xmltodict

class SerializableObject:
    
    def to_dict(self):
        """
        Convert object to JSON
        """
        class_dict = {self.xml_mapping.get(k, k): v if not isinstance(v, SerializableObject) else v.to_dict() for k, v in self.__dict__.items()}
        return class_dict

    def to_xml(self):
        """
        Convert object to XML
        """
        if self.xml_mapping is None:
            raise NotImplementedError('xml_mapping is not defined')
        json_dict = {self.xml_mapping.get(k, k): v if not isinstance(v, SerializableObject) else v.to_dict() for k, v in self.__dict__.items()}
        # return json_dict
        # json_dict = json.dumps(json_dict)

        return xmltodict.unparse(json_dict, pretty=True, full_document=False)
