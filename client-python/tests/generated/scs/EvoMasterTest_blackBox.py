import unittest
import json
import requests


# This file was automatically generated by EvoMaster on 2021-02-03T15:46:05.326998-03:00[America/Argentina/Buenos_Aires]
#
# The generated test suite contains 5 tests
#
# Covered targets: 5
#
# Used time: 0h 0m 10s
#
# Needed budget for current results: 92%
#
# 
class EvoMasterTest(unittest.TestCase):

    
    baseUrlOfSut = "http://localhost:8080/"
    
    
    @classmethod
    def setUpClass(cls):
        pass
    
    
    
    
    
    
    
    
    def test_0(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = requests \
                .get(self.baseUrlOfSut + "/api/costfuns/382/bazrqt",
                    headers=headers)
        assert res_0.json() == json.loads("6\n")
    
    
    def test_1(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = requests \
                .get(self.baseUrlOfSut + "/api/calc/eefW/0.48233035064421526/0.6617995460125885",
                    headers=headers)
        assert res_0.json() == json.loads("0\n")
    
    
    def test_2(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = requests \
                .get(self.baseUrlOfSut + "/api/cookie/rl4kjGIJIm/sNJ4lKk/mKYXRXGb4O",
                    headers=headers)
        assert res_0.json() == json.loads("0\n")
    
    
    def test_3(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = requests \
                .get(self.baseUrlOfSut + "/api/calc/jijIIv6VQixff/0.25243821208269945/0.7776655951240661",
                    headers=headers)
        assert res_0.json() == json.loads("0\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = requests \
                .get(self.baseUrlOfSut + "/api/cookie/1D6q4/c/gj7AngJXUj",
                    headers=headers)
        assert res_1.json() == json.loads("0\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = requests \
                .get(self.baseUrlOfSut + "/api/calc/bJ2VJJO/0.31005276517672165/7.66757228848225E-4",
                    headers=headers)
        
        headers = {}
        headers['Accept'] = "*/*"
        res_3 = requests \
                .get(self.baseUrlOfSut + "/api/cookie/fD43tPz8/L_KQmFYyRjie/_J_oem9z",
                    headers=headers)
        assert res_3.json() == json.loads("0\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_4 = requests \
                .get(self.baseUrlOfSut + "/api/calc/1giSNW/0.6752877855917465/0.6814808988640791",
                    headers=headers)
        assert res_4.json() == json.loads("0\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_5 = requests \
                .get(self.baseUrlOfSut + "/api/cookie/f/BExyMt8oFBAipQ3/_iu",
                    headers=headers)
        assert res_5.json() == json.loads("0\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_6 = requests \
                .get(self.baseUrlOfSut + "/api/cookie/ufRsE/6yfi/Gjzsfh2mZPZ",
                    headers=headers)
        assert res_6.json() == json.loads("0\n")
    
    
    def test_4(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = requests \
                .get(self.baseUrlOfSut + "/api/costfuns/-719720067/CAa05hf",
                    headers=headers)
