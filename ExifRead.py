import PhoOrg


class ExifRead(PhoOrg.SngIm):
    """ Subclass of PhoOrg that handles select image exif data and
        outputs specific EXIF data via class method.

        ExifRead is an important class that allows the user to obtain EXIF data
        on the image(s) they wish to manipulate. ExifRead retrieves the EXIF data
        by using the method get_exif_keys. The keys retrieved are then manipulated by
        methods within in ExifRead to present tailored information to the user.

        Attributes:
            image_path - the image file path inherited from class SngIm

        Important Methods:
            get_exif_keys - returns a list of common EXIF tags
            get_stats - convenient method that packs all exif data returned into dictionary.

        """
    def __init__(self, image_path):
        # Inheriting file path from parent SngIm class.
        super(ExifRead, self).__init__(image_path)

    def get_exif_keys(self):
        """  Gets keys from returned dictionary of PhoOrg.SngIm.get_exif()
             and returns list exif_keys.

        It may seem strange to be retrieving a dictionary of EXIF data from
        the method get_exif of class SngIm when this class itself is named ExifRead,
        but the intended purpose of class ExifRead is only to read EXIF data provided,
        not provide EXIF data (that was SngIm is for :)).
        """


        exif_keys = []

        exif = super(ExifRead, self).get_exif()
        for key in exif.keys():
            exif_keys.append(key)
 
        sorted(exif_keys)
        return exif_keys
 
    def get_name(self):
        return self.image_path
 
    # Methods below loop through list exif_keys for specific
    # key and return value from PhoOrg.SngIm.get_exif() dictionary.
    def get_date(self):
        for k in self.get_exif().keys():
            if k == "DateTime":
                return self.get_exif().get(k)

    def get_resolution(self):
        """Returns two integers of height and width respectively. """
        for k in self.get_exif().keys():
            if k == "ExifImageHeight":
                height = self.get_exif().get(k)
 
        for k in self.get_exif().keys():
            if k == "ExifImageWidth":
                width = self.get_exif().get(k)
 
        return height, width
 
    def get_model(self):
        for k in self.get_exif().keys():
            if k == "Model":
                return self.get_exif().get(k)
 
    def get_aperture(self):
        for k in self.get_exif().keys():
            if k == "FNumber":
                return self.get_exif().get(k)
 
    def get_shutter_speed(self):
        for k in self.get_exif().keys():
            if k == "ExposureTime":
                return self.get_exif().get(k)
 
    def get_iso(self):
        for k in self.get_exif().keys():
            if k == "ISOSpeedRatings":
                return self.get_exif().get(k)

    def get_stats(self):
        """ A function that packs commonly used EXIF data into a handy dictionary.
        NOTE: Use function split_data in main.py to improve readability.
        """
        stats = {
            "Name": self.get_name(), "Date": self.get_date(), "Resolution": self.get_resolution(),
            "Model": self.get_model(), "Aperture": self.get_aperture(), "Shutter Speed": self.get_shutter_speed(),
            "ISO": self.get_iso()
        }
 
        return stats
