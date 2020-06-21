
from pytestbed.TpcpUnitTest import TpcpTestCase, TpcpTestSuite
import unittest

# TODO: is there a way to automatically import scenario classes?

from pytestbed.tar_tests.TestSpecializedTarExtractFile import TestSpecializedTarExtractFile
from pytestbed.tar_tests.TestSpecializedTarGetFile import TestSpecializedTarGetFile
from pytestbed.tar_tests.TestSpecializedTarListFile import TestSpecializedTarListFile
# from pytestbed.tar_tests.TestSpecializedTarConcatFile import TestSpecializedTarConcatFile
from pytestbed.tar_tests.TestSpecializedTarCreateFile import TestSpecializedTarCreateFile
from pytestbed.tar_tests.TestSpecializedTarCreateDirFile import TestSpecializedTarCreateDirFile
from pytestbed.tar_tests.TestSpecializedTarUpdateFile import TestSpecializedTarUpdateFile
from pytestbed.tar_tests.TestSpecializedTarDeleteFile import TestSpecializedTarDeleteFile
from pytestbed.tar_tests.TestSpecializedTarCompareFile import TestSpecializedTarCompareFile

def SpecializationScenario(path):
    suite = TpcpTestSuite()
    suite.addTest(TestSpecializedTarExtractFile(succeeds=True, exe=path))
    suite.addTest(TestSpecializedTarGetFile(succeeds=True, exe=path))
    suite.addTest(TestSpecializedTarListFile(succeeds=True, exe=path))
#    suite.addTest(TestTarConcatFile(succeeds=True, exe=path))
    suite.addTest(TestSpecializedTarCreateFile(succeeds=True, exe=path))
    suite.addTest(TestSpecializedTarCreateDirFile(succeeds=True, exe=path))
    suite.addTest(TestSpecializedTarUpdateFile(succeeds=True, exe=path))
    suite.addTest(TestSpecializedTarDeleteFile(succeeds=True, exe=path))
    suite.addTest(TestSpecializedTarCompareFile(succeeds=True, exe=path))
    return suite 
