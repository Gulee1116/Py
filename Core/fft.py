file_path = "img.png"
img = cv2.imread(file_path)[:, :, ::-1]  # cv2默认是BGR通道顺序，这里调整到RGB
img = cv2.resize(img, (500, 500))

fre = np.fft.fft2(img, axes=(0, 1))  # 变换得到的频域图数据是复数组成的
fre_m = np.abs(fre)  # 幅度谱，求模得到
fre_p = np.angle(fre)  # 相位谱，求相角得到
# 把振幅设为常数
constant = fre_m.mean()
fre_ = constant * np.e ** (1j * fre_p)  # 把幅度谱和相位谱再合并为复数形式的频域图数据
img_onlyphase = np.abs(np.fft.ifft2(fre_, axes=(0, 1)))  # 还原为空间域图像
# 把相位设为常数
constant = fre_p.mean()
fre_ = fre_m * np.e ** (1j * constant)
img_onlymagnitude = np.abs(np.fft.ifft2(fre_, axes=(0, 1)))

plt.figure()
plt.imshow(img.astype("uint8"))
plt.show()
plt.figure()
plt.imshow(img_onlyphase.astype("uint8"))
plt.show()
plt.figure()
plt.imshow(img_onlymagnitude.astype("uint8"))
plt.show()
