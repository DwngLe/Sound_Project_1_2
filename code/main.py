import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from signal_class import Signal
from modify_class import modify       

# Đọc hai đoạn âm thanh từ file
x, sample_rate1 = librosa.load('../sample_audio/au_02.wav')
y, sample_rate2 = librosa.load('../sample_audio/au_01.wav')

# Gắn 2 đoạn âm thanh vào Object
sound1 = Signal(x, sample_rate1)
sound2 = Signal(y, sample_rate2)

modify_sound = modify()

while(True):
    print("---------------------Menu-----------------")
    print("0. Thoát")
    print("1. Đảo ngược đoạn âm thanh 1")
    print("2. Dịch đoạn âm thanh 1 sang trái")
    print("3. Dịch đoạn âm thanh 1 sang phải")
    print("4. Cộng đoạn âm thanh 1 với đoạn âm thanh 2")
    print("5. Trừ đoạn âm thanh 1 với đoạn âm thanh 2")
    print("6. Nhân đoạn âm thanh 1 với đoạn âm thanh 2")
    print("7. Nhân đoạn âm thanh 1 với 1 số")
    print("8. Chia đoạn âm thanh 1 với đoạn âm thanh 2")
    print("9. Chia đoạn âm thanh 1 với 1 số")
    print("10. Nhân châp đoạn âm thanh 1 với đoạn âm thanh 2")
    print("11. Nhân tương quan đoạn âm thanh 1 với đoạn âm thanh 2")
    print("-------------------------------------------")
    print("Nhap lua chon:")

    lua_chon = int(input())

    print("-------------------------------------------")
    match lua_chon:
        case 0:
            break

        case 1:
            modify_sound.flip_signal(sound1)

        case 2:
            modify_sound.shift_sig_left(sound1)

        case 3:
            modify_sound.shift_sig_right(sound1)

        case 4:
           modify_sound.sig_add_sig(sound1, sound2)

        case 5:
            modify_sound.sig_sub_sig(sound1, sound2)

        case 6:
            modify_sound.sig_mul_sig(sound1, sound2)

        case 7:
           modify_sound.sig_mul_num(sound1)

        case 8:
            modify_sound.sig_divide_sig(sound1, sound2)

        case 9:
            modify_sound.sig_divide_num(sound1)

        case 10:
            modify_sound.sig_convolve(sound1, sound2)

        case 11:
          modify_sound.sig_correlate(sound1, sound2)


