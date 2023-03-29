import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from signal_class import Signal

def dong_nhat(sound1, sound2):

        # Đồng nhất tần số lấy mẫu của hai tín hiệu âm thanh về cùng một giá trị
        if sound1.sample_rate != sound2.sample_rate:
            new_sample_rate = min(sound1.sample_rate,sound2.sample_rate)
            sound1.resample(new_sample_rate)
            sound2.resample(new_sample_rate)

        # Đồng nhất độ dài và gốc của 2 tín hiệu
        sound1.trim_signal(sound2)
        
        print("Đã đồng nhất")

class modify():

    def flip_signal(self, sound1):
        plt.figure(figsize=(8, 6))
        plt.subplot(2, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1 ban đầu")

        sound1.flipp_time()
        print("Đoạn âm thanh 1 đã được đảo")
        
        plt.subplot(2, 1, 2)
        sound1.plot_Signal("Đoạn âm thanh 1 sau khi đảo")
        plt.tight_layout()
        plt.show()

    def shift_sig_left(self, sound1):
        print("Nhập thời gian cần dịch:")
        time = float(input())
        plt.figure(figsize=(8, 6))
        plt.subplot(2, 1, 1)
        
        sound1.plot_Signal("Đoạn âm thanh 1 ban đầu")
        shifted_signal = sound1.shift_left(time)
        print("Đoạn âm thanh 1 đã được dịch sang trái " + str(time) + 's')
        print("-----------------------")

        plt.subplot(2, 1, 2)
        shifted_signal.plot_Signal("Đoạn âm thanh 1 sau khi dịch trái")
        plt.tight_layout()
        plt.show()

    def shift_sig_right(self, sound1):
        print("Nhập thời gian cần dịch:")
        time = float(input())
        plt.figure(figsize=(8,6))
        plt.subplot(2, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1 ban đầu")
        
        shifted_signal = sound1.shift_right(time)
        print("Đoạn âm thanh 1 đã được dịch sang phải " + str(time) + 's')

        plt.subplot(2, 1, 2)
        shifted_signal.plot_Signal("Đoạn âm thanh 1 sau khi dịch phải")
        plt.tight_layout()
        plt.show()

    def sig_add_sig(self, sound1, sound2):
        dong_nhat(sound1, sound2)
        new_signal = sound1.add_w_sig(sound2)
        print("Đoạn âm thanh 1 cộng đoạn âm thanh 2!")
        print("__________________________________")
        
        plt.figure(figsize=(8,6))
        plt.subplot(3, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")
    
        plt.subplot(3, 1, 2)
        sound2.plot_Signal("Đoạn âm thanh 2")

        plt.subplot(3, 1, 3)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()

    def sig_sub_sig(self, sound1, sound2):
        dong_nhat(sound1, sound2)
        new_signal = sound1.sub_w_sig(sound2)
        print("Đoạn âm thanh 1 trừ đoạn âm thanh 2!")
        print("__________________________________")

        plt.figure(figsize=(8,6))
        plt.subplot(3, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")
    
        plt.subplot(3, 1, 2)
        sound2.plot_Signal("Đoạn âm thanh 2")
        
        plt.subplot(3, 1, 3)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()

    def sig_mul_sig(self, sound1, sound2):
        dong_nhat(sound1, sound2)
        new_signal = sound1.mul_w_sig(sound2)
        print("Đoạn âm thanh 1 nhân đoạn âm thanh 2!")
        print("__________________________________")

        plt.figure(figsize=(8,6))
        plt.subplot(3, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")
    
        plt.subplot(3, 1, 2)
        sound2.plot_Signal("Đoạn âm thanh 2")

        plt.subplot(3, 1, 3)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()

    def sig_mul_num(self, sound1):
        print("Nhập hệ số")
        heso = int(input())
        new_signal = sound1.mul_w_num(heso)
    
        plt.figure(figsize=(8,6))
        plt.subplot(2, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")

        plt.subplot(2, 1, 2)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()
            
    def sig_divide_sig(self, sound1, sound2):
        dong_nhat(sound1, sound2)
        new_signal = sound1.divide_w_sig(sound2)
        print("Đoạn âm thanh 1 chia đoạn âm thanh 2!")
        print("__________________________________")

        plt.figure(figsize=(8,6))
        plt.subplot(3, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")
    
        plt.subplot(3, 1, 2)
        sound2.plot_Signal("Đoạn âm thanh 2")

        plt.subplot(3, 1, 3)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()

    def sig_divide_num(self, sound1):
        print("Nhập hệ số")
        heso = int(input())
        new_signal = sound1.divide_w_num(heso)
    
        plt.figure(figsize=(8,6))
        plt.subplot(2, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")

        plt.subplot(2, 1, 2)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()
        print("Done")

    def sig_convolve(self, sound1, sound2):
        dong_nhat(sound1, sound2)
        new_signal = sound1.convolve_signal(sound2)
        print("Đoạn âm thanh 1 nhân chập đoạn âm thanh 2!")
        print("__________________________________")

        plt.figure(figsize=(8,6))
        plt.subplot(3, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")
    
        plt.subplot(3, 1, 2)
        sound2.plot_Signal("Đoạn âm thanh 2")

        plt.subplot(3, 1, 3)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()

    def sig_correlate(self, sound1, sound2):
        dong_nhat(sound1, sound2)
        new_signal = sound1.correlate_signal(sound2)
        print("Đoạn âm thanh 1 nhân tương quan đoạn âm thanh 2!")
        print("__________________________________")

        plt.figure(figsize=(8,6))
        plt.subplot(3, 1, 1)
        sound1.plot_Signal("Đoạn âm thanh 1")
    
        plt.subplot(3, 1, 2)
        sound2.plot_Signal("Đoạn âm thanh 2")

        plt.subplot(3, 1, 3)
        new_signal.plot_Signal("Đoạn âm thanh mới")

        plt.tight_layout()
        plt.show()
            


