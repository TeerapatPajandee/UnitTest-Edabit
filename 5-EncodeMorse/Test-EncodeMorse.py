import unittest
import EncodeMorse

class TestEncodeMorse(unittest.TestCase):
    def test_EncodeMorse(self):
        message = [
            ["HELP ME !",".... . .-.. .--.   -- .   -.-.--"],
            ["EDABBIT CHALLENGE", ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."],
            ["CHALLENGE"  , "-.-. .... .- .-.. .-.. . -. --. ."],
            ["1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL...", ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-"],
            ["did you got my mail ?", "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--.."],
            ["TWO THInGS TO KNOW : i FORGeT THeM :C", "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-."]
        ]
        
        for msg in message:
            self.assertEqual(EncodeMorse.encode_morse(msg[0]), msg[1])
        
if __name__ == "__main__":
    unittest.main()