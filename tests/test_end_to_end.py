import unittest
import nibabel as nib
import numpy as np
import pandas as pd


class test_end_to_end(unittest.TestCase):

    def setUp(self):
        pass

    def test_prediction_liver(self):
        img_ref = nib.load("tests/reference_files/example_seg/liver.nii.gz").get_fdata()
        img_new = nib.load("tests/unittest_prediction/liver.nii.gz").get_fdata()
        images_equal = np.array_equal(img_ref, img_new)
        self.assertTrue(images_equal, "liver prediction not correct")

    def test_prediction_vertebrae(self):
        img_ref = nib.load("tests/reference_files/example_seg/vertebrae_L1.nii.gz").get_fdata()
        img_new = nib.load("tests/unittest_prediction/vertebrae_L1.nii.gz").get_fdata()
        images_equal = np.array_equal(img_ref, img_new)
        self.assertTrue(images_equal, "vertebrae prediction not correct")


if __name__ == '__main__':
    unittest.main()
