
def bpm_to_miliseconds(bpm: int):
    """bpm = beats / minute = beats / 60 seconds"""
    bps:float = bpm / 60.0
    """ms = 1000s"""
    bpms = bps / 1000

    '''bpms = x; b = 1; ms = 1/bpms'''
    return 1/bpms

bpm = int(input("Type the bpm: "))

full_note = bpm_to_miliseconds(bpm)
half_note = full_note / 2
quarter_note = half_note / 2
eighth_note = quarter_note / 2
sixteenth_note = eighth_note / 2

print(f"whole: {full_note} ms")
print(f"half: {half_note} ms")
print(f"quarter: {quarter_note} ms")
print(f"eighth: {eighth_note} ms")
print(f"sixteenth: {sixteenth_note} ms")