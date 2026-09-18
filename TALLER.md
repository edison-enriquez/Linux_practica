# Taller de Linux: Challenge Lab

## Información general
**Nombre:** Linux Command Line Challenge Lab
**Modalidad:** práctica individual con flags personalizadas
**Duración estimada:** 4 a 6 horas
**Nivel:** principiante a avanzado
**Puntuación total:** 430 puntos

## Objetivos de aprendizaje

Al completar el taller podrás:

- Navegar por el sistema de archivos de Linux.
- Crear, leer, modificar y buscar archivos y directorios.
- Gestionar permisos y propiedades de archivos.
- Trabajar con compresión, archivado y backups.
- Utilizar pipes, redirecciones y filtros de texto.
- Analizar logs y extraer información relevante.
- Crear y ejecutar scripts Bash.
- Consultar procesos y datos del sistema.
- Trabajar con enlaces simbólicos.
- Diagnosticar información de disco y resolución de nombres.
- Aplicar un cifrado ROT13 desde la terminal.

## Configuración inicial

### Entorno local

```bash
git clone <url-del-repositorio>
cd Linux_practica
pip install -r requirements.txt
```

### Entorno personalizado

Cada estudiante debe ejecutar:

```bash
python3 linux_challenge.py setup
```

El sistema solicitará un código de estudiante. Este código se utiliza para generar flags únicas. Puede ser un identificador institucional, un nombre o cualquier código asignado por el instructor.

### Comprobación inicial

```bash
python3 linux_challenge.py start
python3 verify_system.py
```

Para abrir la interfaz web:

```bash
python3 web_dashboard.py
```

Después visita `http://localhost:5000`.

## Cómo funciona el taller

El laboratorio contiene 21 retos progresivos. Cada reto tiene un token hexadecimal personalizado y una condición técnica. Encontrar o enviar un token no es suficiente: el sistema también comprueba que se haya realizado la operación solicitada.

Para consultar una pista:

```bash
python3 linux_challenge.py hint <numero>
```

Para enviar un token encontrado:

```bash
python3 linux_challenge.py submit "HASH_HEXADECIMAL"
```

Para consultar el estado:

```bash
python3 linux_challenge.py status
```

## Distribución de puntos

| Nivel | Número de retos | Puntos disponibles |
| --- | ---: | ---: |
| Principiante | 2 | 20 |
| Intermedio | 4 | 65 |
| Avanzado | 3 | 65 |
| Experto | 1 | 30 |
| Especializado | 5 | 105 |
| Administración | 5 | 115 |
| Criptografía | 1 | 30 |
| **Total** | **21** | **430** |

## Retos 1 a 5: fundamentos

### Reto 1: Explorador de archivos ocultos

**Objetivo:** encuentra el archivo oculto en `~/linux_lab/secretos`.

**Conceptos:** `cd`, `ls`, archivos ocultos y lectura de archivos.


### Reto 2: Lector de logs

**Objetivo:** lee `~/linux_lab/logs/sistema.log` y localiza la flag.

**Conceptos:** `cat`, `less`, `more` y `grep`.

### Reto 3: Cazador de palabras

**Objetivo:** busca la palabra `secreto` en `~/linux_lab/datos`.

**Conceptos:** búsqueda recursiva y patrones de texto.


### Reto 4: Maestro de permisos

**Objetivo:** cambia `~/linux_lab/config/sistema.conf` a permisos `600`.

**Conceptos:** permisos numéricos, `chmod` y `ls -l`.


### Reto 5: Constructor de estructuras

**Objetivo:** crea `~/linux_lab/proyecto/src/main/java/com/app`.

**Conceptos:** directorios anidados y `mkdir -p`.


## Retos 6 a 10: búsqueda y análisis

### Reto 6: Descompresor experto

**Objetivo:** extrae `~/linux_lab/archivos/secreto.tar.gz` y encuentra la flag.


### Reto 7: Filtro de patrones

**Objetivo:** encuentra todas las direcciones IP en `logs/conexiones.log`.


### Reto 8: Contador de líneas

**Objetivo:** cuenta las líneas que contienen `ERROR`, guarda el resultado y encuentra el token en `logs/errores.log`.


### Reto 9: Detective de archivos

**Objetivo:** encuentra los archivos `.txt` modificados durante las últimas 24 horas.


### Reto 10: El hash perdido

**Objetivo:** calcula el MD5 de `<codigo>_linux_master` y localiza el archivo con ese nombre en `sistema/var/cache`.


## Retos 11 a 15: operaciones del sistema

### Reto 11: Maestro de redirecciones

**Objetivo:** crea `output/resultado.txt` con únicamente las líneas `SUCCESS` de `logs/app.log`.


### Reto 12: Cazador de procesos

**Objetivo:** identifica el servicio asociado al puerto 8080 en `procesos/puertos.txt`.


### Reto 13: Escritor de scripts

**Objetivo:** crea un script ejecutable llamado `scripts/contador.sh` que cuente los archivos `.log`.

El script debe comenzar con `#!/bin/bash` y tener permiso de ejecución.


### Reto 14: Creador de enlaces

**Objetivo:** crea `~/linux_lab/acceso_rapido` como enlace simbólico hacia `~/linux_lab/datos`.


### Reto 15: Análisis de logs

**Objetivo:** encuentra las tres IP que más aparecen en `logs/accesos.log`.


## Retos 16 a 20: administración

Estos retos generan resultados verificables en `~/linux_lab/resultados`.

### Reto 16: Auditoría de entorno

Crea `resultados/entorno.txt` con los valores reales de `USER`, `SHELL` y `HOME`, una variable por línea.


### Reto 17: Inspector de disco

Guarda la salida real de `du` en `resultados/uso_disco.txt`.


### Reto 18: Backup verificable

Crea `backup/lab_backup.tar.gz` con los logs y la configuración del laboratorio.


### Reto 19: Informe con AWK

Encuentra el token en los metadatos de `datos/ventas.csv`, agrupa las ventas por producto y guarda los totales en `resultados/ventas.txt`. Los totales esperados son `cafe=18` y `te=11`.


### Reto 20: Diagnóstico de resolución

Guarda la resolución del nombre `localhost` en `resultados/localhost.txt`.


### Reto 21: Criptógrafo de terminal

Descifra el archivo ROT13 `~/linux_lab/cripto/mensaje_rot13.txt` y guarda el resultado en `~/linux_lab/cripto/mensaje_descifrado.txt`. El token se encuentra dentro del mensaje descifrado.


## Comandos de referencia

### Navegación y archivos

```bash
pwd
cd <directorio>
ls -la
cp origen destino
mv origen destino
rm archivo
```

### Búsqueda y filtrado

```bash
find . -name '*.log'
grep -r 'texto' directorio/
cut -d':' -f1 archivo
sort archivo
uniq -c archivo
```

### Permisos y enlaces

```bash
chmod 600 archivo
chmod u+x script.sh
ln -s origen destino
readlink destino
stat archivo
```

### Compresión y sistema

```bash
tar -czf archivo.tar.gz directorio/
tar -xzf archivo.tar.gz
df -h
du -sh directorio/
ps aux
```

## Recomendaciones de trabajo

1. Comprueba la ruta actual con `pwd` antes de ejecutar cambios.
2. Lista el contenido con `ls -la` antes de modificar archivos.
3. Usa el autocompletado con la tecla Tab.
4. Lee los mensajes de error antes de repetir un comando.
5. Consulta `man <comando>` o `<comando> --help`.
6. Prueba los comandos destructivos con cuidado.
7. Documenta los comandos que te resulten útiles.

## Seguimiento del progreso

```bash
python3 linux_challenge.py status
python3 linux_challenge.py start
python3 verify_system.py
```

El dashboard web muestra el avance, los puntos, las pistas y el estado de los 21 retos.

## Preguntas frecuentes

**¿Puedo resolver los retos en cualquier orden?**
Sí, aunque se recomienda seguir el orden de dificultad.

**¿Qué ocurre si envío un token incorrecto?**
El sistema permite volver a intentarlo sin penalización.

**¿Puedo consultar documentación externa?**
Sí. Buscar documentación forma parte del trabajo habitual en Linux.

**¿Qué ocurre si elimino archivos del laboratorio?**
Puedes ejecutar `python3 linux_challenge.py setup` para preparar de nuevo el entorno. La reconfiguración puede eliminar el progreso actual.

**¿Las flags son iguales para todos los estudiantes?**
No. Se generan a partir del código de cada estudiante.

## Solución de problemas

### Flask no está instalado

```bash
pip install -r requirements.txt
```

### El puerto 5000 está ocupado

```bash
ss -ltn | grep ':5000'
```

### Un script no tiene permisos

```bash
chmod +x script.sh
```

### No encuentro un archivo

```bash
pwd
find ~ -name 'nombre_del_archivo'
```

### Necesito salir de un comando

Usa `Ctrl+C` para cancelar el comando actual, `Ctrl+D` para cerrar una sesión y `q` para salir de `less` o `man`.

## Lista de verificación final

- [ ] Configuré mi código de estudiante.
- [ ] Resolví al menos 16 de 21 retos.
- [ ] Alcancé al menos 150 puntos.
- [ ] Verifiqué mi progreso con `status`.
- [ ] Envié las flags encontradas.
- [ ] Documenté los comandos aprendidos.

**Versión del taller:** 3.0
**Última actualización:** septiembre de 2026
