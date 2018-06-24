# This is an example file to demonstrate my pymorse package
from pymorse import MorseCode

print(MorseCode.char_sequence("e"))
print("-"*80)
print(MorseCode.sequence_char("dit"))
print("-"*80)
print(MorseCode.sequence_string(["dit dit dit", "dit dit", "dit"]))
print("-"*80)
print(MorseCode.string_sequence("string ting ting"))