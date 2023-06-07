# APIrestful_chuck
Prueba técnica de DDB


La API tiene 3 rutas:
/ La raíz sólo indica un texto de bienbenida
/objetos Muestra en formato json 25 diccionarios previamente extraídos de la API: https://api.chucknorris.io/jokes/random
/jokes Muestra un arreglo de 25 datos satíricos sobre Chuck Norris.

Para mejorar el rendimiento modifiqué un poco el código y agregué almacenamiento en caché, por lo que la primera carga puede demorar, 
pero las siguientes por un tiempo determinado serán más rápidas.
