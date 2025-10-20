# 🎯 Linux Challenge Lab - Sistema de Retos CTF

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

**Sistema interactivo de aprendizaje de comandos Linux estilo HackTheBox/CTF**

Aprende comandos de Linux de forma práctica e interactiva, resolviendo retos progresivos y ganando puntos. Perfecto para estudiantes, desarrolladores y entusiastas de la línea de comandos.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Inicio Rápido](#-inicio-rápido)
- [Los 15 Retos](#-los-15-retos)
- [Cómo Usar](#-cómo-usar)
- [Comandos Útiles](#-comandos-útiles-de-linux)
- [Sistema de Puntos](#-sistema-de-puntos)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Solución de Problemas](#-solución-de-problemas)

---

## ✨ Características

- 🎮 **15 Retos Progresivos**: Desde principiante hasta experto
- 🌐 **Dashboard Web Interactivo**: Interfaz moderna estilo terminal/hacker
- ⌨️ **Interfaz CLI**: Uso completo desde la línea de comandos
- 📊 **Sistema de Puntos**: Gana puntos por cada reto completado (285 pts totales)
- 💾 **Progreso Persistente**: Tu avance se guarda automáticamente
- 💡 **Sistema de Pistas**: Obtén ayuda cuando la necesites
- 🔄 **Actualización en Tiempo Real**: El dashboard se actualiza automáticamente
- 📱 **Responsive**: Funciona en escritorio y móvil
- 🎨 **Tema Oscuro**: Diseño estilo hacker con verde neón

---

## 🚀 Inicio Rápido

### En GitHub Codespaces (Recomendado)

1. **Abre este repositorio en Codespaces**
   - Click en `Code` → `Codespaces` → `Create codespace on main`
   - El entorno se configurará automáticamente

2. **Ejecuta el script de inicio**
   ```bash
   ./start.sh
   ```

3. **Selecciona una opción del menú**
   - Opción 1: Iniciar Dashboard Web (Recomendado)
   - Opción 2: Usar Línea de Comandos

### Instalación Manual

```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar el entorno
python3 linux_challenge.py setup

# Iniciar el dashboard web
python3 web_dashboard.py

# O usar la interfaz CLI
python3 linux_challenge.py start
```

---

## 🎮 Los 15 Retos

### 🟢 Nivel Principiante (10 pts c/u)

#### **Reto 1: 🔍 Explorador de Archivos Ocultos**
- **Objetivo**: Encuentra el archivo oculto en `~/linux_lab/secretos`
- **Puntos**: 10
- **Conceptos**: Archivos ocultos, comando `ls -la`

#### **Reto 2: 📖 Lector de Logs**
- **Objetivo**: Lee el contenido del archivo `~/linux_lab/logs/sistema.log`
- **Puntos**: 10
- **Conceptos**: Lectura de archivos con `cat`, `less`, `more`

### 🟡 Nivel Intermedio (15-20 pts)

#### **Reto 3: 🔎 Cazador de Palabras**
- **Objetivo**: Busca la palabra 'secreto' en `~/linux_lab/datos`
- **Puntos**: 15
- **Conceptos**: Búsqueda con `grep`, búsqueda recursiva

#### **Reto 4: 🔐 Maestro de Permisos**
- **Objetivo**: Cambia permisos del archivo a 600 (rw-------)
- **Puntos**: 15
- **Conceptos**: Permisos de archivos con `chmod`

#### **Reto 5: 🏗️ Constructor de Estructuras**
- **Objetivo**: Crea la estructura de directorios especificada
- **Puntos**: 15
- **Conceptos**: Creación de directorios anidados con `mkdir -p`

#### **Reto 6: 📦 Descompresor Experto**
- **Objetivo**: Descomprime el archivo `secreto.tar.gz`
- **Puntos**: 20
- **Conceptos**: Compresión y descompresión con `tar`

### 🔴 Nivel Avanzado (20-25 pts)

#### **Reto 7: 🎯 Filtro de Patrones**
- **Objetivo**: Encuentra todas las direcciones IP en el log
- **Puntos**: 20
- **Conceptos**: Expresiones regulares con `grep -E`

#### **Reto 8: 🔢 Contador de Líneas**
- **Objetivo**: Cuenta líneas con la palabra 'ERROR'
- **Puntos**: 20
- **Conceptos**: Pipes y filtros (`grep | wc -l`)

#### **Reto 9: 🕵️ Detective de Archivos**
- **Objetivo**: Encuentra archivos .txt modificados recientemente
- **Puntos**: 25
- **Conceptos**: Búsqueda avanzada con `find`

### 🏆 Nivel Experto (30 pts)

#### **Reto 10: 🏆 Challenge Final: El Hash Perdido**
- **Objetivo**: Encuentra la flag en un archivo con nombre hash MD5
- **Puntos**: 30
- **Conceptos**: Integración de todos los conocimientos

### 🎯 Nivel Especializado (15-30 pts)

#### **Reto 11: 📤 Maestro de Redirecciones**
- **Objetivo**: Domina redirecciones de entrada/salida y stderr
- **Puntos**: 15
- **Conceptos**: Redirecciones (`>`, `>>`, `2>`, `&>`, `<`)

#### **Reto 12: ⚙️ Controlador de Procesos**
- **Objetivo**: Gestiona procesos en segundo plano
- **Puntos**: 20
- **Conceptos**: Gestión de procesos (`ps`, `jobs`, `bg`, `fg`, `kill`)

#### **Reto 13: 📜 Maestro del Scripting**
- **Objetivo**: Crea y ejecuta un script bash avanzado
- **Puntos**: 25
- **Conceptos**: Scripting bash, variables, condicionales, loops

#### **Reto 14: 🔗 Experto en Enlaces**
- **Objetivo**: Crea y gestiona enlaces simbólicos y duros
- **Puntos**: 15
- **Conceptos**: Enlaces simbólicos (`ln -s`) y enlaces duros

#### **Reto 15: 🔬 Análisis Forense de Logs**
- **Objetivo**: Análisis complejo de archivos de log
- **Puntos**: 30
- **Conceptos**: Análisis avanzado con `awk`, `sed`, `sort`, `uniq`

**PUNTUACIÓN TOTAL: 285 puntos**

---

## 💻 Cómo Usar

### Dashboard Web (Recomendado)

1. **Inicia el servidor web**
   ```bash
   python3 web_dashboard.py
   ```

2. **Abre tu navegador**
   - URL: `http://localhost:5000`

3. **Explora el dashboard**
   - Ver estadísticas en tiempo real
   - Leer descripciones de retos
   - Ver pistas cuando las necesites
   - Enviar flags cuando resuelvas retos

4. **Resuelve los retos en la terminal**
   - Usa comandos de Linux para resolver cada reto
   - Encuentra las flags en formato `FLAG{...}`
   - Envía las flags en el dashboard web

### Interfaz de Línea de Comandos (CLI)

```bash
# Ver todos los retos disponibles
python3 linux_challenge.py start

# Ver tu progreso actual
python3 linux_challenge.py status

# Ver pista de un reto específico
python3 linux_challenge.py hint 1

# Enviar una flag
python3 linux_challenge.py submit FLAG{encontre_el_oculto}

# Configurar/reconfigurar el entorno
python3 linux_challenge.py setup
```

### Script de Inicio Interactivo

```bash
./start.sh
```

Este script te presentará un menú con opciones para:
- Iniciar el dashboard web
- Usar la línea de comandos
- Ver el README
- Verificar el sistema
- Reconfigurar el entorno

---

## 🔧 Comandos Útiles de Linux

### Navegación y Exploración
```bash
ls              # Listar archivos
ls -la          # Listar todos (incluidos ocultos) con detalles
cd directorio   # Cambiar de directorio
pwd             # Mostrar directorio actual
tree            # Ver estructura de árbol
```

### Lectura de Archivos
```bash
cat archivo.txt         # Mostrar contenido completo
less archivo.txt        # Ver archivo (paginado)
head -n 10 archivo.txt  # Primeras 10 líneas
tail -n 10 archivo.txt  # Últimas 10 líneas
```

### Búsqueda de Archivos
```bash
find . -name "*.txt"              # Buscar por nombre
find . -type f -mtime -1          # Modificados hace menos de 1 día
find . -type d -name "config"     # Buscar directorios
locate archivo                    # Búsqueda rápida (requiere updatedb)
```

### Búsqueda en Contenido
```bash
grep "palabra" archivo.txt               # Buscar palabra
grep -r "palabra" directorio/            # Búsqueda recursiva
grep -i "palabra" archivo.txt            # Ignorar mayúsculas
grep -E "patrón|otro" archivo.txt        # Expresiones regulares
grep -c "ERROR" archivo.log              # Contar ocurrencias
```

### Permisos
```bash
chmod 600 archivo        # rw-------
chmod 644 archivo        # rw-r--r--
chmod 755 archivo        # rwxr-xr-x
ls -l archivo            # Ver permisos
stat archivo             # Información detallada
```

### Directorios
```bash
mkdir directorio                  # Crear directorio
mkdir -p a/b/c/d                 # Crear directorios anidados
rmdir directorio                  # Eliminar directorio vacío
rm -r directorio                  # Eliminar directorio y contenido
```

### Compresión
```bash
tar -czf archivo.tar.gz directorio/    # Comprimir
tar -xzf archivo.tar.gz                # Descomprimir
gzip archivo                           # Comprimir con gzip
gunzip archivo.gz                      # Descomprimir gzip
```

### Pipes y Filtros
```bash
cat archivo | grep "ERROR"              # Buscar errores
grep "ERROR" archivo | wc -l            # Contar errores
find . -name "*.log" | xargs grep "IP" # Buscar en múltiples archivos
```

### Información del Sistema
```bash
whoami              # Usuario actual
hostname            # Nombre del host
uname -a            # Información del sistema
df -h               # Espacio en disco
du -sh directorio/  # Tamaño de directorio
```

---

## ⭐ Sistema de Puntos

| Nivel | Puntos por Reto | Número de Retos | Total |
|-------|-----------------|-----------------|-------|
| 🟢 Principiante | 10 pts | 2 | 20 pts |
| 🟡 Intermedio | 15-20 pts | 4 | 65 pts |
| 🔴 Avanzado | 20-25 pts | 3 | 65 pts |
| 🏆 Experto | 30 pts | 1 | 30 pts |
| 🎯 Especializado | 15-30 pts | 5 | 105 pts |
| **TOTAL** | | **15** | **285 pts** |

### Niveles de Logro

- 🥉 **Bronce** (0-70 pts): Principiante
- 🥈 **Plata** (71-140 pts): Intermedio
- 🥇 **Oro** (141-215 pts): Avanzado
- 🏆 **Maestro** (216-285 pts): Experto en Linux

---

## 📁 Estructura del Proyecto

```
linux-challenge-lab/
├── .devcontainer/
│   └── devcontainer.json       # Configuración de Codespaces
├── templates/
│   └── index.html              # Dashboard web
├── linux_challenge.py          # Sistema principal de retos
├── web_dashboard.py            # Servidor Flask
├── start.sh                    # Script de inicio interactivo
├── verify_system.py            # Script de verificación
├── requirements.txt            # Dependencias Python
├── README.md                   # Este archivo
├── GUIA_PROFESOR.md           # Guía para instructores
├── SOLUCIONES.md              # Soluciones de los retos
├── INSTALACION.md             # Guía de instalación
└── .gitignore                 # Archivos ignorados

Directorio de datos (creado automáticamente):
~/linux_lab/
├── .progress.json             # Progreso del usuario
├── secretos/                  # Reto 1
├── logs/                      # Retos 2, 7, 8
├── datos/                     # Retos 3, 9
├── config/                    # Reto 4
├── archivos/                  # Reto 6
└── sistema/                   # Reto 10
```

---

## 🔧 Solución de Problemas

### El dashboard no inicia

```bash
# Verifica que Flask esté instalado
pip install flask

# Verifica que el puerto 5000 esté libre
lsof -i :5000

# Si está ocupado, mata el proceso o usa otro puerto
python3 web_dashboard.py  # Edita el archivo para cambiar el puerto
```

### El entorno no está configurado

```bash
# Reconfigura el entorno
python3 linux_challenge.py setup

# O usa el script interactivo
./start.sh
# Selecciona opción 5: Reconfigurar Entorno
```

### Los archivos no tienen permisos de ejecución

```bash
chmod +x start.sh
chmod +x verify_system.py
```

### No puedo encontrar un archivo para un reto

```bash
# Verifica que el entorno esté configurado
ls -la ~/linux_lab

# Si falta, reconfigura
python3 linux_challenge.py setup
```

### Mi progreso se perdió

El progreso se guarda en `~/linux_lab/.progress.json`. Si este archivo se elimina, perderás tu progreso. Para hacer un backup:

```bash
cp ~/linux_lab/.progress.json ~/backup_progress.json
```

### El dashboard no se actualiza

- Refresca la página (F5)
- Espera 10 segundos (actualización automática)
- Verifica la consola del navegador para errores

---

## 🎓 Aprendizaje

Este sistema está diseñado para enseñarte:

1. **Navegación en Linux**: Moverte por el sistema de archivos
2. **Manipulación de archivos**: Crear, leer, modificar archivos
3. **Búsqueda**: Encontrar archivos y contenido
4. **Permisos**: Entender y modificar permisos
5. **Expresiones regulares**: Patrones de búsqueda avanzados
6. **Pipes**: Combinar comandos para tareas complejas
7. **Compresión**: Trabajar con archivos comprimidos
8. **Pensamiento lógico**: Resolver problemas paso a paso

---

## 🤝 Contribuir

¿Tienes ideas para nuevos retos? ¿Encontraste un bug? 

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nuevo-reto`)
3. Commit tus cambios (`git commit -am 'Agregar nuevo reto'`)
4. Push a la rama (`git push origin feature/nuevo-reto`)
5. Crea un Pull Request

---

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👨‍🏫 Para Instructores

Si eres profesor/instructor, consulta:
- **GUIA_PROFESOR.md**: Guía completa para instructores
- **SOLUCIONES.md**: Soluciones detalladas (mantener confidencial)
- **INSTALACION.md**: Guía de despliegue para estudiantes

---

## 📞 Soporte

¿Necesitas ayuda? 
- 📖 Lee la documentación completa
- 🔍 Revisa la sección de solución de problemas
- 💡 Usa las pistas de los retos
- 🐛 Reporta bugs en GitHub Issues

---

## 🎉 ¡Buena Suerte!

**¡Diviértete aprendiendo Linux!** 🐧🚀

Recuerda: El objetivo no es solo completar los retos, sino **entender** los comandos y conceptos. Tómate tu tiempo para experimentar.

---

**Desarrollado con ❤️ para la comunidad de aprendizaje de Linux**