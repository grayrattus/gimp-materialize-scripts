# gimp-materialize-scripts

# gimp-materialize-scripts

To use this script type in python gimp console:
execfile(path_to_gimp_rullers.py)

and then you can use GuidelinesFactory class to create guidelines with specified image width.
Image width is converted to size which is closest to https://material.io/design/layout/responsive-layout-grid.html#breakpoints

Which means if you use it like this: GuidelinesFactory.createGuidelines(width_of_image, height_of_image)

width_of_image, height_of_image : int

script will create image with layer which has the lowest breakpoint closest to 2000.

In example 2000 will create image with width 1920.

