# Linux Challenge Lab

Laboratorio interactivo para aprender administración de sistemas Linux y línea de comandos mediante retos progresivos. Cada estudiante obtiene flags personalizadas y el progreso se guarda en `~/linux_lab/.progress.json`.

## Contenido

- 21 retos progresivos, desde navegación básica hasta criptografía de terminal.
- Dashboard web para consultar el progreso, pedir pistas y enviar flags.
- Interfaz CLI para trabajar completamente desde la terminal.
- Verificaciones basadas en el estado real del sistema y en los archivos producidos.
- 430 puntos disponibles.

## Inicio rápido

```bash
pip install -r requirements.txt
python3 linux_challenge.py setup
python3 web_dashboard.py
```

Después abre `http://localhost:5000`. También puedes consultar los retos desde la terminal:

```bash
python3 linux_challenge.py start
python3 linux_challenge.py status
```

El script `./start.sh` ofrece un menú para iniciar el dashboard, consultar el estado o usar la CLI.

## Flujo de trabajo

1. Ejecuta `setup` y registra tu código de estudiante.
2. Lee un reto con `python3 linux_challenge.py start`.
3. Trabaja en `~/linux_lab` usando comandos Linux reales.
4. Consulta una pista con `python3 linux_challenge.py hint NUMERO` cuando sea necesario.
5. Envía el token encontrado con `python3 linux_challenge.py submit "HASH"` o desde el dashboard.

Una flag correcta solo registra el reto si también se cumple su condición técnica.

## Retos

| Rango | Área | Puntos aproximados |
| --- | --- | ---: |
| 1-2 | Archivos ocultos y lectura de logs | 20 |
| 3-6 | Búsqueda, permisos, directorios y compresión | 65 |
| 7-9 | Expresiones regulares, pipes y `find` | 65 |
| 10 | Hash y descubrimiento de archivos | 30 |
| 11-15 | Redirecciones, procesos, scripts, enlaces y análisis de logs | 105 |
| 16-20 | Entorno, disco, backups, `awk` y redes | 115 |
| 21 | Criptografía ROT13 | 30 |
| **Total** | | **430** |

### Retos de administración

Los retos de administración producen artefactos que se comprueban de forma concreta:

- El informe de entorno debe contener `USER`, `SHELL` y `HOME`.
- El informe de disco debe conservar la salida de `du -sh`.
- El backup debe ser un `tar.gz` legible con logs y configuración.
- El informe de ventas debe sumar los productos mediante `awk`.
- La resolución de `localhost` debe proceder de una herramienta del sistema como `getent`.
- El mensaje de criptografía debe descifrarse y guardarse en `cripto/mensaje_descifrado.txt`.

## Comandos útiles

```bash
ls -la                         # Listar archivos, incluidos los ocultos
cat archivo.txt                # Leer un archivo
grep -r "texto" directorio/    # Buscar contenido recursivamente
find . -type f -mtime -1       # Buscar archivos recientes
chmod 600 archivo              # Cambiar permisos
mkdir -p a/b/c                 # Crear una estructura anidada
tar -xzf archivo.tar.gz        # Extraer un archivo comprimido
grep "ERROR" archivo | wc -l  # Contar líneas filtradas
du -sh ~/linux_lab             # Consultar uso de disco
getent hosts localhost          # Resolver localhost
```

## Dashboard web

El dashboard muestra el total de retos, puntos, porcentaje de avance y estado de cada ejercicio. Se actualiza automáticamente y permite solicitar pistas o enviar flags sin abandonar la terminal.

Para iniciarlo:

```bash
python3 web_dashboard.py
```

La API principal está disponible en:

- `GET /api/progress`: progreso y retos.
- `GET /api/hint/<id>`: pista de un reto.
- `POST /api/submit`: envío de una flag.
- `GET /api/stats`: estadísticas por dificultad y categoría.

## Estructura

```text
linux_challenge.py       Sistema de retos, flags y verificaciones
web_dashboard.py         Servidor Flask y API
templates/index.html     Dashboard web
verify_system.py         Comprobación de instalación
start.sh                 Menú de inicio
requirements.txt         Dependencias Python
TALLER.md                Guía extendida del taller
```

El entorno de trabajo se crea en `~/linux_lab` con directorios para logs, datos, configuración, scripts, backups y resultados.

## Verificación

```bash
python3 verify_system.py
python3 -m py_compile linux_challenge.py verify_system.py web_dashboard.py
```

Si el dashboard no inicia, comprueba que Flask esté instalado y que el puerto 5000 esté disponible:

```bash
pip install -r requirements.txt
ss -ltn | grep ':5000'
```

## Licencia

Proyecto de código abierto distribuido bajo la licencia MIT.
