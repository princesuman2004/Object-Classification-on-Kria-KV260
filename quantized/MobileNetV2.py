# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class MobileNetV2(torch.nn.Module):
    def __init__(self):
        super(MobileNetV2, self).__init__()
        self.module_0 = py_nndct.nn.Input() #MobileNetV2::input_0
        self.module_1 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/ConvNormActivation[0]/Conv2d[0]/input.3
        self.module_2 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/ConvNormActivation[0]/ReLU[2]/input.7
        self.module_3 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[1]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.9
        self.module_4 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[1]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.13
        self.module_5 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[1]/Sequential[conv]/Conv2d[1]/input.15
        self.module_6 = py_nndct.nn.Conv2d(in_channels=16, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.19
        self.module_7 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.23
        self.module_8 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=96, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.25
        self.module_9 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.29
        self.module_10 = py_nndct.nn.Conv2d(in_channels=96, out_channels=24, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/Conv2d[2]/input.31
        self.module_11 = py_nndct.nn.Conv2d(in_channels=24, out_channels=144, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.35
        self.module_12 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.39
        self.module_13 = py_nndct.nn.Conv2d(in_channels=144, out_channels=144, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=144, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.41
        self.module_14 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.45
        self.module_15 = py_nndct.nn.Conv2d(in_channels=144, out_channels=24, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/Conv2d[2]/input.47
        self.module_16 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/input.49
        self.module_17 = py_nndct.nn.Conv2d(in_channels=24, out_channels=144, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.51
        self.module_18 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.55
        self.module_19 = py_nndct.nn.Conv2d(in_channels=144, out_channels=144, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=144, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.57
        self.module_20 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.61
        self.module_21 = py_nndct.nn.Conv2d(in_channels=144, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/Conv2d[2]/input.63
        self.module_22 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.67
        self.module_23 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.71
        self.module_24 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.73
        self.module_25 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.77
        self.module_26 = py_nndct.nn.Conv2d(in_channels=192, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/Conv2d[2]/input.79
        self.module_27 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/input.81
        self.module_28 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.83
        self.module_29 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.87
        self.module_30 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.89
        self.module_31 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.93
        self.module_32 = py_nndct.nn.Conv2d(in_channels=192, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/Conv2d[2]/input.95
        self.module_33 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/input.97
        self.module_34 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.99
        self.module_35 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.103
        self.module_36 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.105
        self.module_37 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.109
        self.module_38 = py_nndct.nn.Conv2d(in_channels=192, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/Conv2d[2]/input.111
        self.module_39 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.115
        self.module_40 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.119
        self.module_41 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.121
        self.module_42 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.125
        self.module_43 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/Conv2d[2]/input.127
        self.module_44 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/input.129
        self.module_45 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.131
        self.module_46 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.135
        self.module_47 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.137
        self.module_48 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.141
        self.module_49 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/Conv2d[2]/input.143
        self.module_50 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/input.145
        self.module_51 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.147
        self.module_52 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.151
        self.module_53 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.153
        self.module_54 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.157
        self.module_55 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/Conv2d[2]/input.159
        self.module_56 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/input.161
        self.module_57 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.163
        self.module_58 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.167
        self.module_59 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.169
        self.module_60 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.173
        self.module_61 = py_nndct.nn.Conv2d(in_channels=384, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/Conv2d[2]/input.175
        self.module_62 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.179
        self.module_63 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.183
        self.module_64 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.185
        self.module_65 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.189
        self.module_66 = py_nndct.nn.Conv2d(in_channels=576, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/Conv2d[2]/input.191
        self.module_67 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/input.193
        self.module_68 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.195
        self.module_69 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.199
        self.module_70 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.201
        self.module_71 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.205
        self.module_72 = py_nndct.nn.Conv2d(in_channels=576, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/Conv2d[2]/input.207
        self.module_73 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/input.209
        self.module_74 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.211
        self.module_75 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.215
        self.module_76 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.217
        self.module_77 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.221
        self.module_78 = py_nndct.nn.Conv2d(in_channels=576, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/Conv2d[2]/input.223
        self.module_79 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.227
        self.module_80 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.231
        self.module_81 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.233
        self.module_82 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.237
        self.module_83 = py_nndct.nn.Conv2d(in_channels=960, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/Conv2d[2]/input.239
        self.module_84 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/input.241
        self.module_85 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.243
        self.module_86 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.247
        self.module_87 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.249
        self.module_88 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.253
        self.module_89 = py_nndct.nn.Conv2d(in_channels=960, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/Conv2d[2]/input.255
        self.module_90 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/input.257
        self.module_91 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.259
        self.module_92 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.263
        self.module_93 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.265
        self.module_94 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.269
        self.module_95 = py_nndct.nn.Conv2d(in_channels=960, out_channels=320, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/Conv2d[2]/input.271
        self.module_96 = py_nndct.nn.Conv2d(in_channels=320, out_channels=1280, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/ConvNormActivation[18]/Conv2d[0]/input.275
        self.module_97 = py_nndct.nn.ReLU(inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/ConvNormActivation[18]/ReLU[2]/x
        self.module_98 = py_nndct.nn.AdaptiveAvgPool2d(output_size=1) #MobileNetV2::MobileNetV2/10100
        self.module_99 = py_nndct.nn.Module('flatten') #MobileNetV2::MobileNetV2/input.279
        self.module_100 = py_nndct.nn.Linear(in_features=1280, out_features=80, bias=True) #MobileNetV2::MobileNetV2/Sequential[classifier]/Linear[1]/10107

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_3(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_0 = self.module_6(output_module_0)
        output_module_0 = self.module_7(output_module_0)
        output_module_0 = self.module_8(output_module_0)
        output_module_0 = self.module_9(output_module_0)
        output_module_0 = self.module_10(output_module_0)
        output_module_11 = self.module_11(output_module_0)
        output_module_11 = self.module_12(output_module_11)
        output_module_11 = self.module_13(output_module_11)
        output_module_11 = self.module_14(output_module_11)
        output_module_11 = self.module_15(output_module_11)
        output_module_16 = self.module_16(input=output_module_0, other=output_module_11, alpha=1)
        output_module_16 = self.module_17(output_module_16)
        output_module_16 = self.module_18(output_module_16)
        output_module_16 = self.module_19(output_module_16)
        output_module_16 = self.module_20(output_module_16)
        output_module_16 = self.module_21(output_module_16)
        output_module_22 = self.module_22(output_module_16)
        output_module_22 = self.module_23(output_module_22)
        output_module_22 = self.module_24(output_module_22)
        output_module_22 = self.module_25(output_module_22)
        output_module_22 = self.module_26(output_module_22)
        output_module_27 = self.module_27(input=output_module_16, other=output_module_22, alpha=1)
        output_module_28 = self.module_28(output_module_27)
        output_module_28 = self.module_29(output_module_28)
        output_module_28 = self.module_30(output_module_28)
        output_module_28 = self.module_31(output_module_28)
        output_module_28 = self.module_32(output_module_28)
        output_module_33 = self.module_33(input=output_module_27, other=output_module_28, alpha=1)
        output_module_33 = self.module_34(output_module_33)
        output_module_33 = self.module_35(output_module_33)
        output_module_33 = self.module_36(output_module_33)
        output_module_33 = self.module_37(output_module_33)
        output_module_33 = self.module_38(output_module_33)
        output_module_39 = self.module_39(output_module_33)
        output_module_39 = self.module_40(output_module_39)
        output_module_39 = self.module_41(output_module_39)
        output_module_39 = self.module_42(output_module_39)
        output_module_39 = self.module_43(output_module_39)
        output_module_44 = self.module_44(input=output_module_33, other=output_module_39, alpha=1)
        output_module_45 = self.module_45(output_module_44)
        output_module_45 = self.module_46(output_module_45)
        output_module_45 = self.module_47(output_module_45)
        output_module_45 = self.module_48(output_module_45)
        output_module_45 = self.module_49(output_module_45)
        output_module_50 = self.module_50(input=output_module_44, other=output_module_45, alpha=1)
        output_module_51 = self.module_51(output_module_50)
        output_module_51 = self.module_52(output_module_51)
        output_module_51 = self.module_53(output_module_51)
        output_module_51 = self.module_54(output_module_51)
        output_module_51 = self.module_55(output_module_51)
        output_module_56 = self.module_56(input=output_module_50, other=output_module_51, alpha=1)
        output_module_56 = self.module_57(output_module_56)
        output_module_56 = self.module_58(output_module_56)
        output_module_56 = self.module_59(output_module_56)
        output_module_56 = self.module_60(output_module_56)
        output_module_56 = self.module_61(output_module_56)
        output_module_62 = self.module_62(output_module_56)
        output_module_62 = self.module_63(output_module_62)
        output_module_62 = self.module_64(output_module_62)
        output_module_62 = self.module_65(output_module_62)
        output_module_62 = self.module_66(output_module_62)
        output_module_67 = self.module_67(input=output_module_56, other=output_module_62, alpha=1)
        output_module_68 = self.module_68(output_module_67)
        output_module_68 = self.module_69(output_module_68)
        output_module_68 = self.module_70(output_module_68)
        output_module_68 = self.module_71(output_module_68)
        output_module_68 = self.module_72(output_module_68)
        output_module_73 = self.module_73(input=output_module_67, other=output_module_68, alpha=1)
        output_module_73 = self.module_74(output_module_73)
        output_module_73 = self.module_75(output_module_73)
        output_module_73 = self.module_76(output_module_73)
        output_module_73 = self.module_77(output_module_73)
        output_module_73 = self.module_78(output_module_73)
        output_module_79 = self.module_79(output_module_73)
        output_module_79 = self.module_80(output_module_79)
        output_module_79 = self.module_81(output_module_79)
        output_module_79 = self.module_82(output_module_79)
        output_module_79 = self.module_83(output_module_79)
        output_module_84 = self.module_84(input=output_module_73, other=output_module_79, alpha=1)
        output_module_85 = self.module_85(output_module_84)
        output_module_85 = self.module_86(output_module_85)
        output_module_85 = self.module_87(output_module_85)
        output_module_85 = self.module_88(output_module_85)
        output_module_85 = self.module_89(output_module_85)
        output_module_90 = self.module_90(input=output_module_84, other=output_module_85, alpha=1)
        output_module_90 = self.module_91(output_module_90)
        output_module_90 = self.module_92(output_module_90)
        output_module_90 = self.module_93(output_module_90)
        output_module_90 = self.module_94(output_module_90)
        output_module_90 = self.module_95(output_module_90)
        output_module_90 = self.module_96(output_module_90)
        output_module_90 = self.module_97(output_module_90)
        output_module_90 = self.module_98(output_module_90)
        output_module_90 = self.module_99(input=output_module_90, start_dim=1, end_dim=3)
        output_module_90 = self.module_100(output_module_90)
        return output_module_90
