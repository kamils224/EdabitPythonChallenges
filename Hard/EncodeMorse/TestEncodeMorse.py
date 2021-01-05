import unittest
from EncodeMorse import encode_morse


class TestEncodeMorse(unittest.TestCase):

    def test_encode_morse(self):
        self.assertEqual(encode_morse("EDABBIT CHALLENGE"), ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .", "Test 1")
        self.assertEqual(encode_morse("HELP ME !"), ".... . .-.. .--.   -- .   -.-.--", "Test 2")
        self.assertEqual(encode_morse("CHALLENGE"), "-.-. .... .- .-.. .-.. . -. --. .", "Test 3")
        self.assertEqual(encode_morse("1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."), ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-", "Test 4")
        self.assertEqual(encode_morse("did you got my mail ?"), "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--..", "Test 5")
        self.assertEqual(encode_morse("TWO THInGS TO KNOW : i FORGeT THeM :C"), "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-.", "Test 6")

if __name__ == '__main__':
    unittest.main()