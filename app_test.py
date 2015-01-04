import unittest
import tests.controller as tc

def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(tc.ControllerTest))
    
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
