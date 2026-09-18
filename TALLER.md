# Taller de Linux: Challenge Lab

## Información general
**Nombre:** Linux Command Line Challenge Lab
**Modalidad:** práctica individual con flags personalizadas
**Duración estimada:** 4 a 6 horas
**Nivel:** principiante a avanzado
**Puntuación total:** 400 puntos

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

El laboratorio contiene 20 retos progresivos. Cada reto tiene una flag personalizada y una condición técnica. Encontrar o enviar una flag no es suficiente: el sistema también comprueba que se haya realizado la operación solicitada.

Para consultar una pista:

```bash
python3 linux_challenge.py hint <numero>
```

Para enviar una flag:

```bash
python3 linux_challenge.py submit "FLAG{tu_flag_aqui}"
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
| **Total** | **20** | **400** |

## Retos 1 a 5: fundamentos

### Reto 1: Explorador de archivos ocultos

**Objetivo:** encuentra el archivo oculto en `~/linux_lab/secretos`.

**Conceptos:** `cd`, `ls`, archivos ocultos y lectura de archivos.

```bash
cd ~/linux_lab/secretos
ls -la
cat .archivo_oculto.txt
```

### Reto 2: Lector de logs

**Objetivo:** lee `~/linux_lab/logs/sistema.log` y localiza la flag.

**Conceptos:** `cat`, `less`, `more` y `grep`.

### Reto 3: Cazador de palabras

**Objetivo:** busca la palabra `secreto` en `~/linux_lab/datos`.

**Conceptos:** búsqueda recursiva y patrones de texto.

```bash
grep -r "secreto" ~/linux_lab/datos
```

### Reto 4: Maestro de permisos

**Objetivo:** cambia `~/linux_lab/config/sistema.conf` a permisos `600`.

**Conceptos:** permisos numéricos, `chmod` y `ls -l`.

```bash
chmod 600 ~/linux_lab/config/sistema.conf
ls -l ~/linux_lab/config/sistema.conf
```

### Reto 5: Constructor de estructuras

**Objetivo:** crea `~/linux_lab/proyecto/src/main/java/com/app`.

**Conceptos:** directorios anidados y `mkdir -p`.

```bash
mkdir -p ~/linux_lab/proyecto/src/main/java/com/app
```

## Retos 6 a 10: búsqueda y análisis

### Reto 6: Descompresor experto

**Objetivo:** extrae `~/linux_lab/archivos/secreto.tar.gz` y encuentra la flag.

```bash
cd ~/linux_lab/archivos
tar -xzf secreto.tar.gz
find secreto -type f -print
```

### Reto 7: Filtro de patrones

**Objetivo:** encuentra todas las direcciones IP en `logs/conexiones.log`.

```bash
grep -E '[0-9]{1,3}(\.[0-9]{1,3}){3}' ~/linux_lab/logs/conexiones.log
```

### Reto 8: Contador de líneas

**Objetivo:** cuenta las líneas que contienen `ERROR` en `logs/errores.log`.

```bash
grep 'ERROR' ~/linux_lab/logs/errores.log | wc -l
```

### Reto 9: Detective de archivos

**Objetivo:** encuentra los archivos `.txt` modificados durante las últimas 24 horas.

```bash
find ~/linux_lab -type f -name '*.txt' -mtime -1 -print
```

### Reto 10: El hash perdido

**Objetivo:** calcula el MD5 de `<codigo>_linux_master` y localiza el archivo con ese nombre en `sistema/var/cache`.

```bash
echo -n "TU_CODIGO_linux_master" | md5sum
find ~/linux_lab/sistema/var/cache -type f
```

## Retos 11 a 15: operaciones del sistema

### Reto 11: Maestro de redirecciones

**Objetivo:** crea `output/resultado.txt` con únicamente las líneas `SUCCESS` de `logs/app.log`.

```bash
mkdir -p ~/linux_lab/output
grep 'SUCCESS' ~/linux_lab/logs/app.log > ~/linux_lab/output/resultado.txt
```

### Reto 12: Cazador de procesos

**Objetivo:** identifica el servicio asociado al puerto 8080 en `procesos/puertos.txt`.

```bash
grep '8080' ~/linux_lab/procesos/puertos.txt
```

### Reto 13: Escritor de scripts

**Objetivo:** crea un script ejecutable llamado `scripts/contador.sh` que cuente los archivos `.log`.

El script debe comenzar con `#!/bin/bash` y tener permiso de ejecución.

```bash
chmod +x ~/linux_lab/scripts/contador.sh
~/linux_lab/scripts/contador.sh
```

### Reto 14: Creador de enlaces

**Objetivo:** crea `~/linux_lab/acceso_rapido` como enlace simbólico hacia `~/linux_lab/datos`.

```bash
ln -s ~/linux_lab/datos ~/linux_lab/acceso_rapido
readlink ~/linux_lab/acceso_rapido
```

### Reto 15: Análisis de logs

**Objetivo:** encuentra las tres IP que más aparecen en `logs/accesos.log`.

```bash
awk '{print $4}' ~/linux_lab/logs/accesos.log | sort | uniq -c | sort -rn | head -3
```

## Retos 16 a 20: administración

Estos retos generan resultados verificables en `~/linux_lab/resultados`.

### Reto 16: Auditoría de entorno

Crea `resultados/entorno.txt` con los valores reales de `USER`, `SHELL` y `HOME`, una variable por línea.

```bash
printf 'USER=%s\nSHELL=%s\nHOME=%s\n' "$USER" "$SHELL" "$HOME" > ~/linux_lab/resultados/entorno.txt
```

### Reto 17: Inspector de disco

Guarda la salida real de `du` en `resultados/uso_disco.txt`.

```bash
du -sh ~/linux_lab > ~/linux_lab/resultados/uso_disco.txt
```

### Reto 18: Backup verificable

Crea `backup/lab_backup.tar.gz` con los logs y la configuración del laboratorio.

```bash
mkdir -p ~/linux_lab/backup
tar -czf ~/linux_lab/backup/lab_backup.tar.gz \
  -C ~/linux_lab logs config
tar -tzf ~/linux_lab/backup/lab_backup.tar.gz
```

### Reto 19: Informe con AWK

Agrupa las ventas de `datos/ventas.csv` por producto y guarda los totales en `resultados/ventas.txt`. Los totales esperados son `cafe=18` y `te=11`.

```bash
awk -F, 'NR > 1 { total[$1] += $4 } END { for (producto in total) print producto "=" total[producto] }' \
  ~/linux_lab/datos/ventas.csv > ~/linux_lab/resultados/ventas.txt
```

### Reto 20: Diagnóstico de resolución

Guarda la resolución del nombre `localhost` en `resultados/localhost.txt`.

```bash
getent hosts localhost > ~/linux_lab/resultados/localhost.txt
```

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

El dashboard web muestra el avance, los puntos, las pistas y el estado de los 20 retos.

## Preguntas frecuentes

**¿Puedo resolver los retos en cualquier orden?**
Sí, aunque se recomienda seguir el orden de dificultad.

**¿Qué ocurre si envío una flag incorrecta?**
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
- [ ] Resolví al menos 15 de 20 retos.
- [ ] Alcancé al menos 150 puntos.
- [ ] Verifiqué mi progreso con `status`.
- [ ] Envié las flags encontradas.
- [ ] Documenté los comandos aprendidos.

**Versión del taller:** 3.0
**Última actualización:** septiembre de 2026
