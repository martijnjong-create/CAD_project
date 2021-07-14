import shutil
import os


count = 0
suspended = ['amc_1008_wle_imagecap_eac_na_na_5.png',
'amc_1014_wle_image_eac_na_na_3.png',
'amc_1014_wle_image_eac_na_na_4.png',
'amc_1014_wle_image_eac_na_na_6.png',
'amc_1014_wle_image_eac_na_na_7.png',
'amc_108_wle_image_hgd_na_na_9.png',
'amc_110_wle_imagecap_hgd_na_na_2.png',
'amc_110_wle_imagecap_hgd_na_na_5.png',
'amc_122_wle_image_eac_superclean_na_3.png',
'amc_47_wle_retroimage_hgd_na_na_7.png',
'amc_47_wle_retroimage_hgd_na_na_9.png',
'amc_49_wle_image_eac_superclean_na_4.png',
'amc_568_wle_image_eac_na_na_1.bmp',
'amc_568_wle_image_eac_na_na_3.bmp',
'amc_568_wle_image_eac_na_na_4.bmp',
'amc_568_wle_image_eac_na_na_5.bmp',
'amc_581_wle_image_eac_na_na_31.png',
'amc_584_wle_image_eac_na_na_17.png',
'amc_594_wle_image_eac_na_na_25.png',
'amc_612_wle_focusimagecap_eac_na_na_7.png',
'amc_624_wle_image_eac_na_na_2.png',
'amc_649_wle_image_eac_na_na_19.png',
'amc_657_wle_image_eac_na_na_5.png',
'amc_657_wle_image_eac_na_na_9.png',
'amc_670_wle_image_eac_na_na_5.png',
'amc_672_wle_image_eac_na_na_19.png',
'amc_679_wle_image_eac_na_na_6.png',
'amc_682_wle_image_eac_na_na_8.png',
'amc_684_wle_image_eac_na_na_3.png',
'amc_684_wle_image_eac_na_na_5.png',
'amc_840_wle_image_eac_na_na_9.png',
'amc_840_wle_imagecap_eac_na_na_2.png',
'amc_840_wle_imagecap_eac_na_na_4.png',
'amc_841_wle_image_eac_na_na_3.png',
'amc_844_wle_imagecap_eac_na_na_12.png',
'amc_844_wle_imagecap_eac_na_na_15.png',
'amc_853_wle_retroimage_eac_na_na_7.png',
'amc_859_wle_retroimagecap_eac_na_na_1.png',
'amc_860_wle_image_eac_na_na_6.png',
'amc_860_wle_image_eac_na_na_7.png',
'amc_862_wle_retroimage_eac_na_na_3.png',
'amc_862_wle_retroimage_eac_na_na_4.png',
'amc_891_wle_retroimagecap_eac_na_na_2.png',
'amc_891_wle_retroimagecap_eac_na_na_8.png',
'amc_891_wle_retroimagecap_eac_na_na_9.png',
'amc_981_wle_imagecap_eac_na_na_1.png',
'gro_113_wle_image_hgd_na_na_1.png',
'gro_45_wle_retroimage_eac_na_na_2.png',
'gro_95_wle_retroimage_eac_na_na_1.png',
'isa_102_wle_imagecap_eac_na_na_1.png',
'isa_26_wle_image_eac_na_na_1.png',
'isa_26_wle_image_eac_na_na_3.png',
'isa_26_wle_image_eac_na_na_4.png',
'isa_27_wle_image_eac_na_na_1.png',
'isa_57_wle_retroimage_eac_na_na_1.png',
'isa_88_wle_image_eac_na_na_1.png',
'isa_88_wle_image_eac_na_na_2.png',
'isa_88_wle_image_eac_na_na_3.png',
'isa_88_wle_image_eac_na_na_4.png',
'isa_88_wle_image_eac_na_na_5.png',
'isa_97_wle_image_eac_na_na_1.png',
'par_145_wle_image_eac_na_na_3.png',
'par_91_wle_image_hgd_na_na_2.png',
'par_91_wle_image_hgd_na_na_4.png',
'umcu_113_wle_image_eac_na_na_3.png',
'umcu_120_wle_image_eac_na_na_1.png',
'umcu_132_wle_imagecap_eac_na_na_1.png',
'umcu_132_wle_imagecap_eac_na_na_2.png',
'umcu_132_wle_imagecap_eac_na_na_4.png',
'umcu_135_wle_focusimagecap_eac_na_na_2.png',
'zur_105_wle_image_eac_superclean_na_1.png',
'zur_106_wle_image_hgd_superclean_na_1.png',
'zur_22_wle_imagecap_hgd_superclean_na_2.png',
'zur_45_wle_image_eac_superclean_na_1.png',
'zur_54_wle_image_eac_superclean_na_2.png',
'zur_99_wle_image_hgd_superclean_na_1.png']

path = r'Z:\- BEELDMATERIAAL -\QADB data voor tim 110721\Neo\Train'
images = ['png', 'tiff', 'jpg', 'bmp']
for folderName, subfolders, filenames in os.walk(path):
    
    for file in filenames:
        
        if file in suspended:
            print(file)

            os.remove(os.path.join(folderName, file))
       
