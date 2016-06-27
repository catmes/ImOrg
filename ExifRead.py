import PhoOrg

# Subclass of PhoOrg that handles select image exif data and
# outputs specific exif data via class method.
class ExifRead(PhoOrg.SngIm):
 
    def __init__(self, image_path):
        # Inherenting file path from parent SngIm class.
        super(ExifRead, self).__init__(image_path)
 
    # gets keys from returned dictionary of PhoOrg.SngIm.get_exif()
    # and returns list exif_keys.
    def get_exif_keys(self):
        exif_keys = []
 
 
        exif = super(ExifRead, self).get_exif()
        for key in exif.keys():
            exif_keys.append(key)
 
        exif_keys.sort()
        return exif_keys
 
    def get_name(self):
        return self.image_path
 
    # Methods below loop through list exif_keys for specific
    # key and return value from PhoOrg.SngIm.get_exif() dictionary.
    def get_date(self):
        for k in self.get_exif().keys():
            if k == "DateTime":
                return self.get_exif().get(k)
 
    # Note: returns two values of height and width
    def get_resolution(self):
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
 
    # Convenient method that packs all exif data returned above (from methods) into dicionary.
    def get_stats(self):
        stats = {
            "Name": self.get_name(), "Date": self.get_date(), "Resolution": self.get_resolution(),
            "Model": self.get_model(), "Aperture": self.get_aperture(), "Shutter Speed": self.get_shutter_speed(),
            "ISO": self.get_iso()
        }
 
        return stats