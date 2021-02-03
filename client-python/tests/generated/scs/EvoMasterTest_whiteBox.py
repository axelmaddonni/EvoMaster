import unittest
import json
import requests
import evomaster_benchmark.scs.em_handler


# This file was automatically generated by EvoMaster on 2021-02-03T15:37:56.809117-03:00[America/Argentina/Buenos_Aires]
#
# The generated test suite contains 7 tests
#
# Covered targets: 40
#
# Used time: 0h 0m 10s
#
# Needed budget for current results: 11%
#
# 
class EvoMasterTest(unittest.TestCase):

    
    controller = evomaster_benchmark.scs.em_handler.EMHandler()
    
    
    @classmethod
    def setUpClass(cls):
        cls.controller.setup_for_generated_test()
        cls.test_client = cls.controller.app().test_client()
    
    
    @classmethod
    def tearDownClass(cls):
        cls.controller.stop_sut()
    
    
    def setUp(self):
        self.controller.reset_state_of_sut()
    
    
    
    
    def test_0(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/calc/LNXMEEwkZau/0.4406341352487505/0.057729106127229146",
                    headers=headers)
        assert res_0.json == json.loads("0\n")
    
    
    def test_1(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/costfuns/704/JLYQNUU3Uw4k",
                    headers=headers)
        assert res_0.json == json.loads("4\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = self.test_client \
                .get("/api/calc/evomaster_16_input/-182722.55694951667/0.3",
                    headers=headers)
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = self.test_client \
                .get("/api/cookie/2hlO_PKXwcTkP_91/2oZ1D8/W5gZf_1Y8Nzu0bXL",
                    headers=headers)
        assert res_2.json == json.loads("0\n")
    
    
    def test_2(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/costfuns/533/c5",
                    headers=headers)
        assert res_0.json == json.loads("6\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = self.test_client \
                .get("/api/costfuns/704/JLYQNUU3Uw4k",
                    headers=headers)
        assert res_1.json == json.loads("4\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = self.test_client \
                .get("/api/calc/HIUnA2nSZrAIA/0.41151219952773577/0.33823757822920986",
                    headers=headers)
        assert res_2.json == json.loads("0\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_3 = self.test_client \
                .get("/api/cookie/2hlO_PKXwcTkP_91/2oZ1E8/W5gZf_1Y8Nzu0bXL",
                    headers=headers)
        assert res_3.json == json.loads("0\n")
    
    
    def test_3(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/cookie/LwPwTVEUatZ5LA/UjK39T7q4_V5O/26XEHym4COy55h7N",
                    headers=headers)
        assert res_0.json == json.loads("0\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = self.test_client \
                .get("/api/costfuns/71/mY",
                    headers=headers)
        assert res_1.json == json.loads("6\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = self.test_client \
                .get("/api/costfuns/580/8mPKGPk8j",
                    headers=headers)
        assert res_2.json == json.loads("5\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_3 = self.test_client \
                .get("/api/calc/gslqyBPqF/0.9281712331695725/0.712193775843933",
                    headers=headers)
        assert res_3.json == json.loads("0\n")
    
    
    def test_4(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/cookie/oVF8d3iy3QOcre0/XZ9THL30yyqAL/TEub0TL124DXm",
                    headers=headers)
        assert res_0.json == json.loads("0\n")
    
    
    def test_5(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/costfuns/838/SCy_miaS4o",
                    headers=headers)
        assert res_0.json == json.loads("4\n")
    
    
    def test_6(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/costfuns/-1047738/SCy_miaS4o",
                    headers=headers)
