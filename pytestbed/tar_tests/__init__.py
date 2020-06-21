
from pytestbed.TpcpUnitTest import TpcpTestCase, TpcpTestSuite
import unittest

# TODO: is there a way to automatically import scenario classes?

from pytestbed.tar_tests.ScenarioTarStandard import standardScenario
from pytestbed.tar_tests.ScenarioTarDisableCreateTarballs import disableCreatingTarballsScenario
from pytestbed.tar_tests.ScenarioTarSpecialization import specializationScenario

def load_tests(path):
    #suite = standardScenario(path)
    #suite.addTest(disableCreatingTarballsScenario(path))
    suite = specializationScenario(path)
    return suite



