
from pytestbed.TpcpUnitTest import TpcpTestCase, TpcpTestSuite
import unittest

# TODO: is there a way to automatically import scenario classes?

from pytestbed.tar_tests.ScenarioTarSpecialization import SpecializationScenario
from pytestbed.tar_tests.ScenarioTarStandard import StandardScenario
from pytestbed.tar_tests.ScenarioTarDisableCreateTarballs import disableCreatingTarballsScenario

def load_tests(path):
    suite = specializationScenario(path)
    #suite = standardScenario(path)
    #suite.addTest(disableCreatingTarballsScenario(path))
    return suite



