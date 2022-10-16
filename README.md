# Group_raster_clip
Проект Arcmap с импортированным модулем для обрезки группы растров. 

Для версии Arcgis 10.8. Возможны проблемы при запуске на сильно старых версиях. Модуль написан на python 2.7.


	
При первом запуске проекта, выполните следующие действия:
	Откройте свой проект. 
	В каталоге Arcmap откройте скачанную папку Group_raster_clip с проектом, где содержится модуль
	Затем в GROUP_TIFF_CUT зайдите в properties файла GroupRasterClip
	Заходите в source
	В графе script file указываете путь к файлу 0_1.py, который лежит в папке с проектом


справка по документации используемых методов arcpy - https://desktop.arcgis.com/en/arcmap/latest/tools/data-management-toolbox/clip.htm

при повторном запуске модуля с теми же входными файлами и той же выходной папкой, файлы в выходной папке перезапишутся


При возникновении ошибок возможно помогут следующие действия:
 	перейдите с помощью проводника к папке python27\Lib\site-packages 
	и добавьте или отредактируйте файл Desktop10.8.pth. 
	Файл должен содержать три строки, как показано ниже (исправьте системные пути, если они отличаются):

	c:\Program Files\ArcGIS\Desktop10.8\arcpy
	c:\Program Files\ArcGIS\Desktop10.8\bin
	c:\Program Files\ArcGIS\Desktop10.8\ArcToolbox\Scripts

	затем используйте сочетание клавишь Win + R
	введите в открывшемся окне cmd (должен открыться терминал с черным фоном)
	в терминале введите python --version. терминал должен вывести python версии 2.7.
	введите pip install numpy
	дождитесь завершения установки, закройте терминал

Также можно обратиться в поддержку
почта nagel20@yandex.ru
telegram 8 925 735 32 87