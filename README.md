# Group_raster_clip EN
Instruction with pictures (https://github.com/GAGvozdik/Group_raster_clip/blob/main/README.md)

Arcmap project with imported group clipping module. 
For Arcgis version 10.8. Possible problems when running on older versions. Module is written in python 2.7.

Installation:
1. Terminal GIT must be installed to work correctly (https://git-scm.com/downloads). 
2. Open in any new folder, right-click in the folder -> Git Bash Here.
3. In the terminal that opens, type git clone https://github.com/GAGvozdik/Group_raster_clip.git.

![Illustration 0](https://github.com/GAGvozdik/Group_raster_clip/blob/main/img/instruction0.png)

4. Close the terminal.

Instructions:
1. Open CUT_TIFF_BY_SHAPE.mxd project.
2. In the directory, select the GroupRasterClip tool in GROUP_TIFF_CUT.tbx.

![Illustration 1](https://github.com/GAGvozdik/Group_raster_clip/blob/main/img/instruction1.PNG)

3. In the window that opens select the folder where the TIFF files are located.
4. Choose a contour of the .shp type.
5. Select the folder where you want to save the cropped images.

![Illustration 1](https://github.com/GAGvozdik/Group_raster_clip/blob/main/img/instruction2.PNG)

*When you run the module again with the same input files and the same output folder, the files in the output folder will be overwritten

The documentation help for the arcpy methods used is https://desktop.arcgis.com/en/arcmap/latest/tools/data-management-toolbox/clip.htm.
You can also contact support
email: nagel20@yandex.ru
telegram: 8 925 735 32 87


# Group_raster_clip RU

Инструкция с картинками (https://github.com/GAGvozdik/Group_raster_clip/blob/main/README.md)
Проект Arcmap с импортированным модулем для обрезки группы растров. 
Для версии Arcgis 10.8. Возможны проблемы при запуске на старых версиях. Модуль написан на python 2.7.

Установка:
1. Для корректной работы требуется установить терминал GIT (https://git-scm.com/downloads). 
2. Открыть в любую новую папку, в папке щелкнуть правой кнопкой мыши -> Git Bash Here.
3. В открывшемся терминале ввести git clone https://github.com/GAGvozdik/Group_raster_clip.git

![Illustration 0](https://github.com/GAGvozdik/Group_raster_clip/blob/main/img/instruction0.png)

4. Закрыть терминал.
  
Инструкция:
1. Открыть проект CUT_TIFF_BY_SHAPE.mxd.
2. В каталоге выбрать инструмент GroupRasterClip в GROUP_TIFF_CUT.tbx.

![Illustration 1](https://github.com/GAGvozdik/Group_raster_clip/blob/main/img/instruction1.PNG)

3. В открывшемся окне выбрать папку, в которой лежат файлы TIFF.
4. Выбрать контур типа .shp.
5. Выбрать папку, куда сохранятся обрезанные растры.

![Illustration 1](https://github.com/GAGvozdik/Group_raster_clip/blob/main/img/instruction2.PNG)

*При повторном запуске модуля с теми же входными файлами и той же выходной папкой, файлы в выходной папке перезапишутся

Cправка по документации используемых методов arcpy - https://desktop.arcgis.com/en/arcmap/latest/tools/data-management-toolbox/clip.htm
Также можно обратиться в поддержку
почта: nagel20@yandex.ru
telegram: 8 925 735 32 87