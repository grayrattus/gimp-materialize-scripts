import gimpfu

class MaterialSize:
    min_width = 1920
    max_width = 4000
    window_name = "xlarge"
    columns = 12
    margins = 24

    def get_size_of_guideline(self):
        return (self.min_width/self.columns)-self.margins

    def get_margin(self):
        return self.margins/2;
        

class XLarge(MaterialSize):
    min_width = 1920
    max_width = 4000
    window_name = "xlarge"
    columns = 12
    margins = 24

class Large(MaterialSize):
    min_width = 1440
    max_width = 1919
    window_name = "large"
    columns = 12
    margins = 24

class Medium(MaterialSize):
    min_width = 1024
    max_width = 1439
    window_name = "medium"
    columns = 12
    margins = 24

class Small(MaterialSize):
    min_width = 600
    max_width = 1023
    window_name = "small"
    columns = 8
    margins = 24

class XSmall(MaterialSize):
    min_width = 480
    max_width = 599
    window_name = "xmall"
    columns = 4
    margins = 16

class MaterialSizeFactory:
    sizes=[XSmall(), Small(), Medium(), Large(), XLarge()]
    @staticmethod
    def createMaterialSize(input_width):
        for size in MaterialSizeFactory.sizes:
            if input_width < size.max_width:
                return size
        return MaterialSizeFactory.sizes[-1]

class GuidelinesFactory:
    @staticmethod
    def createGuidelines(width, height):
        defaultOpacity=100.0
        materialSize = MaterialSizeFactory.createMaterialSize(width)
        image = pdb.gimp_image_new(materialSize.min_width, height, 0)
        layer = pdb.gimp_layer_new(image, materialSize.min_width, height, 0, materialSize.window_name, defaultOpacity, 0)

        pdb.gimp_image_add_layer(image, layer, 0)
        pdb.gimp_display_new(image)

        current_guide_position=0
        for margin_and_guide_area_index in range(0,materialSize.columns):
            current_guide_position+=materialSize.get_margin()
            pdb.gimp_image_add_vguide(image, current_guide_position)
            pdb.gimp_image_add_vguide(image, current_guide_position)
            current_guide_position+=materialSize.get_size_of_guideline()
            pdb.gimp_image_add_vguide(image, current_guide_position)
            current_guide_position+=materialSize.get_margin()
