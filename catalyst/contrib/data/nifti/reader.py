from typing import Optional
import nibabel as nib

class NiftiReader(IReader):
    """
    Nifti reader abstraction for NeuroImaging. Reads nifti images from
    a `csv` dataset.
    """

    def __init__(self, input_key: str, output_key: Optional[str], rootpath:
                 Optional[str] = None):
        """
        Args:
            input_key (str): key to use from annotation dict
            output_key (str): key to use to store the result
            rootpath (str): path to images dataset root directory
                (so your can use relative paths in annotations)
            coords (list): crop coordinaties
        """
        super().__init__(input_key, output_key)
        self.rootpath = rootpath

    def __call__(self, element):
        """Reads a row from your annotations dict with filename and
        transfer it to an image
        Args:
            element: elem in your dataset.
        Returns:
            np.ndarray: Image
        """
        image_name = str(element[self.input_key])
        img = nib.load(image_name)
        img = img.get_fdata()
        output = {self.output_key: img}
        return output
