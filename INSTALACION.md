# 🚀 INSTALACIÓN - Linux Challenge Lab

**Guía rápida de instalación y configuración**

---

## 📋 Tabla de Contenidos

1. [Instalación en GitHub Codespaces](#instalación-en-github-codespaces) ⭐ Recomendado
2. [Instalación Local](#instalación-local)
3. [Verificación de la Instalación](#verificación-de-la-instalación)
4. [Primeros Pasos](#primeros-pasos)
5. [Comandos Rápidos](#comandos-rápidos)
6. [GitHub Classroom](#integración-con-github-classroom)
7. [Solución de Problemas](#solución-de-problemas)

---

## 🌐 Instalación en GitHub Codespaces

### Método Automático (Recomendado) ⭐

Este es el método más sencillo y funciona automáticamente gracias al archivo `.devcontainer/devcontainer.json`.

#### Paso 1: Abrir en Codespaces

1. **Desde GitHub:**
   - Ve al repositorio en GitHub
   - Click en el botón verde `Code`
   - Selecciona la pestaña `Codespaces`
   - Click en `Create codespace on main`

   ![Crear Codespace](https://docs.github.com/assets/cb-77061/images/help/codespaces/new-codespace-button.png)

2. **Espera la configuración automática** (2-3 minutos)
   - Se instalará Python 3.11
   - Se instalarán las dependencias (Flask)
   - Se configurará el entorno automáticamente

#### Paso 2: Verificar la Instalación

Una vez que el Codespace esté listo:

```bash
# El entorno ya debería estar configurado
ls ~/linux_lab
```

Si el directorio no existe, ejecuta:

```bash
python3 linux_challenge.py setup
```

#### Paso 3: Iniciar el Sistema

```bash
# Opción 1: Usar el script interactivo
./start.sh

# Opción 2: Iniciar directamente el dashboard
python3 web_dashboard.py

# Opción 3: Usar CLI
python3 linux_challenge.py start
```

### Método Manual en Codespaces

Si la configuración automática falla:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Dar permisos de ejecución a los scripts
chmod +x start.sh
chmod +x verify_system.py

# 3. Configurar el entorno
python3 linux_challenge.py setup

# 4. Verificar
python3 verify_system.py
```

### Ventajas de Codespaces

✅ **Configuración automática**  
✅ **No requiere instalación local**  
✅ **Entorno consistente para todos**  
✅ **Accesible desde cualquier dispositivo**  
✅ **60-120 horas gratis al mes**

---

## 💻 Instalación Local

### Requisitos Previos

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Git**
- Sistema operativo: Linux, macOS o Windows con WSL

### Verificar Requisitos

```bash
# Verificar Python
python3 --version
# Debe mostrar: Python 3.8.x o superior

# Verificar pip
pip3 --version
# Debe mostrar: pip 20.x.x o superior

# Verificar Git
git --version
# Debe mostrar: git version 2.x.x o superior
```

### Instalación Paso a Paso

#### 1. Clonar el Repositorio

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/linux-challenge-lab.git

# Entrar al directorio
cd linux-challenge-lab
```

#### 2. Crear Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
# En Linux/macOS:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

#### 3. Instalar Dependencias

```bash
# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
pip list
# Debe mostrar Flask y Werkzeug
```

#### 4. Dar Permisos de Ejecución (Linux/macOS)

```bash
chmod +x start.sh
chmod +x verify_system.py
```

#### 5. Configurar el Entorno

```bash
# Configurar el laboratorio
python3 linux_challenge.py setup

# Verificar
python3 verify_system.py
```

### Instalación en Windows

Para Windows, recomendamos usar **WSL2** (Windows Subsystem for Linux):

#### Instalar WSL2

1. Abrir PowerShell como Administrador
2. Ejecutar:
   ```powershell
   wsl --install
   ```
3. Reiniciar el equipo
4. Abrir Ubuntu desde el menú de inicio
5. Seguir los pasos de instalación local

#### Alternativa: Git Bash

Si no quieres usar WSL:

```bash
# En Git Bash
python -m pip install -r requirements.txt
python linux_challenge.py setup
python web_dashboard.py
```

---

## ✅ Verificación de la Instalación

### Script de Verificación

Ejecuta el script de verificación para asegurarte de que todo funciona:

```bash
python3 verify_system.py
```

Deberías ver algo como:

```
======================================================================
  🔍 VERIFICACIÓN DEL SISTEMA - Linux Challenge Lab
======================================================================

🐍 Verificando Python...
   ✅ Python 3.11.4

📦 Verificando dependencias...
   ✅ Flask
   ✅ Werkzeug

📄 Verificando archivos del sistema...
   ✅ linux_challenge.py (25680 bytes) - Sistema principal de retos
   ✅ web_dashboard.py (4532 bytes) - Servidor web
   ✅ templates/index.html (15234 bytes) - Dashboard HTML
   ✅ requirements.txt (45 bytes) - Dependencias
   ✅ start.sh (3456 bytes) - Script de inicio

🔧 Verificando entorno del laboratorio...
   ✅ Directorio del laboratorio: /home/user/linux_lab
   ✅ secretos/
   ✅ logs/
   ✅ datos/
   ✅ config/
   ✅ archivos/
   ✅ sistema/

🔐 Verificando permisos...
   ✅ start.sh (ejecutable)
   ✅ verify_system.py (ejecutable)

🌐 Verificando disponibilidad de puertos...
   ✅ Puerto 5000 disponible

======================================================================
  📋 RESUMEN DE VERIFICACIÓN
======================================================================

   Verificaciones completadas: 6/6
   Estado: ✅ SISTEMA COMPLETAMENTE FUNCIONAL

   🚀 Todo está listo para usar Linux Challenge Lab
```

### Verificación Manual

```bash
# 1. Verificar Python
python3 --version

# 2. Verificar Flask
python3 -c "import flask; print(flask.__version__)"

# 3. Verificar estructura
ls -la ~/linux_lab

# 4. Probar CLI
python3 linux_challenge.py start

# 5. Probar servidor web (en otra terminal)
python3 web_dashboard.py
# Luego visita http://localhost:5000
```

---

## 🎯 Primeros Pasos

### 1. Explorar el Sistema

```bash
# Ver todos los retos
python3 linux_challenge.py start

# Ver tu progreso
python3 linux_challenge.py status

# Ver pista del primer reto
python3 linux_challenge.py hint 1
```

### 2. Iniciar el Dashboard Web

```bash
# Iniciar el servidor
python3 web_dashboard.py

# O usar el script interactivo
./start.sh
# Selecciona opción 1
```

Luego abre tu navegador en:
- http://localhost:5000
- http://127.0.0.1:5000

En Codespaces, se abrirá automáticamente en una nueva pestaña.

### 3. Resolver tu Primer Reto

```bash
# Navegar al directorio del primer reto
cd ~/linux_lab/secretos

# Listar archivos ocultos
ls -la

# Leer el archivo oculto
cat .archivo_oculto.txt

# Enviar la flag
python3 linux_challenge.py submit FLAG{encontre_el_oculto}
```

---

## ⚡ Comandos Rápidos

### Configuración

```bash
# Configurar entorno inicial
python3 linux_challenge.py setup

# Reconfigurar (elimina progreso)
rm -rf ~/linux_lab && python3 linux_challenge.py setup

# Verificar sistema
python3 verify_system.py
```

### Uso del CLI

```bash
# Ver retos
python3 linux_challenge.py start

# Ver progreso
python3 linux_challenge.py status

# Ver pista
python3 linux_challenge.py hint <numero>

# Enviar flag
python3 linux_challenge.py submit FLAG{...}
```

### Dashboard Web

```bash
# Iniciar servidor
python3 web_dashboard.py

# Con verbose (debug)
python3 web_dashboard.py --debug

# En segundo plano (Linux/macOS)
nohup python3 web_dashboard.py &

# Detener servidor
# Presiona CTRL+C en la terminal donde está corriendo
```

### Script Interactivo

```bash
# Iniciar menú interactivo
./start.sh

# Opciones disponibles:
# 1 - Iniciar Dashboard Web
# 2 - Usar Línea de Comandos
# 3 - Ver README
# 4 - Ver Estado del Sistema
# 5 - Reconfigurar Entorno
# 6 - Salir
```

---

## 🎓 Integración con GitHub Classroom

### Para Instructores

1. **Crear una organización en GitHub**
   ```
   https://github.com/organizations/new
   ```

2. **Acceder a GitHub Classroom**
   ```
   https://classroom.github.com
   ```

3. **Crear un nuevo Classroom**
   - Seleccionar tu organización
   - Nombrar el classroom

4. **Crear una asignación**
   - Tipo: Individual Assignment
   - Template repository: Tu fork del proyecto
   - Habilitar feedback pull requests
   - Habilitar Codespaces

5. **Compartir el enlace con estudiantes**
   ```
   https://classroom.github.com/a/ABC123XYZ
   ```

### Para Estudiantes

1. **Aceptar la asignación**
   - Click en el enlace proporcionado por el instructor
   - Autorizar GitHub Classroom
   - Se creará automáticamente tu repositorio personal

2. **Abrir en Codespaces**
   - Click en el botón `Code` en tu repositorio
   - Selecciona `Codespaces`
   - Click en `Create codespace on main`

3. **Comenzar a trabajar**
   - El entorno se configurará automáticamente
   - Sigue los pasos de "Primeros Pasos"

---

## 🔧 Solución de Problemas

### Problema: Flask no se instala

```bash
# Actualizar pip
python3 -m pip install --upgrade pip

# Instalar Flask nuevamente
pip install Flask==3.0.0

# Si persiste, usar --user
pip install --user Flask==3.0.0
```

### Problema: Puerto 5000 ocupado

```bash
# Ver qué proceso usa el puerto
lsof -i :5000

# Matar el proceso
kill -9 <PID>

# O cambiar el puerto en web_dashboard.py
# Edita la última línea:
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Problema: Permisos denegados en start.sh

```bash
# Dar permisos de ejecución
chmod +x start.sh
chmod +x verify_system.py

# Ejecutar
./start.sh
```

### Problema: El entorno no se configura

```bash
# Verificar que estás en el directorio correcto
pwd

# Debe mostrar algo como:
# /workspaces/linux-challenge-lab o
# /home/usuario/linux-challenge-lab

# Configurar manualmente
python3 linux_challenge.py setup

# Verificar
ls -la ~/linux_lab
```

### Problema: "Module not found" al ejecutar

```bash
# Verificar que Flask está instalado
pip list | grep Flask

# Si no está, instalar
pip install -r requirements.txt

# Verificar Python
which python3
python3 --version
```

### Problema: El dashboard no se ve bien

- Limpia la caché del navegador (CTRL+SHIFT+R)
- Prueba en modo incógnito
- Verifica que el servidor esté corriendo
- Revisa la consola del navegador (F12) para errores

### Problema: Progreso perdido

```bash
# El progreso se guarda en:
~/linux_lab/.progress.json

# Hacer backup
cp ~/linux_lab/.progress.json ~/backup_progress.json

# Restaurar backup
cp ~/backup_progress.json ~/linux_lab/.progress.json
```

### Problema: Codespace muy lento

- Codespaces gratuitos tienen recursos limitados
- Cierra pestañas/aplicaciones innecesarias
- Considera actualizar a GitHub Pro para mejores recursos
- O usa instalación local

---

## 📊 Estructura de Archivos

```
linux-challenge-lab/
├── .devcontainer/
│   └── devcontainer.json           # Configuración de Codespaces
├── templates/
│   └── index.html                  # Dashboard web
├── linux_challenge.py              # Sistema principal ⭐
├── web_dashboard.py                # Servidor Flask ⭐
├── start.sh                        # Script de inicio ⭐
├── verify_system.py                # Verificación del sistema
├── requirements.txt                # Dependencias Python
├── README.md                       # Documentación principal
├── GUIA_PROFESOR.md               # Guía para instructores
├── SOLUCIONES.md                  # Soluciones (confidencial)
├── INSTALACION.md                 # Este archivo
└── .gitignore                     # Archivos ignorados

Directorio de datos (creado automáticamente):
~/linux_lab/
├── .progress.json                 # Tu progreso
├── secretos/                      # Reto 1
│   └── .archivo_oculto.txt
├── logs/                          # Retos 2, 7, 8
│   ├── sistema.log
│   ├── conexiones.log
│   └── errores.log
├── datos/                         # Retos 3, 9
│   ├── archivo1.txt
│   ├── archivo2.txt
│   ├── archivo3.txt
│   └── reciente.txt
├── config/                        # Reto 4
│   └── sistema.conf
├── archivos/                      # Reto 6
│   └── secreto.tar.gz
└── sistema/                       # Reto 10
    └── var/
        └── cache/
            └── 2f4e803d0dcf99c0b9f58bcfa5be0b43
```

---

## 🆘 Obtener Ayuda

### Recursos Disponibles

1. **README.md**: Documentación completa del proyecto
2. **GUIA_PROFESOR.md**: Información adicional y pedagógica
3. **verify_system.py**: Diagnóstico automático

### Comunidad

- 🐛 Reportar bugs: GitHub Issues
- 💬 Discusiones: GitHub Discussions
- 📧 Contacto: [tu-email@ejemplo.com]

### Comandos de Ayuda

```bash
# Ayuda del CLI
python3 linux_challenge.py

# Estado del sistema
python3 verify_system.py

# Ver logs del servidor
python3 web_dashboard.py
# Los logs aparecerán en la terminal
```

---

## ✅ Checklist de Instalación

Usa esta lista para verificar que todo esté correcto:

- [ ] Python 3.8+ instalado
- [ ] Flask instalado
- [ ] Repositorio clonado
- [ ] Scripts con permisos de ejecución (Linux/macOS)
- [ ] Entorno configurado (`python3 linux_challenge.py setup`)
- [ ] Verificación pasada (`python3 verify_system.py`)
- [ ] CLI funciona (`python3 linux_challenge.py start`)
- [ ] Dashboard accesible (http://localhost:5000)
- [ ] Primer reto visible

---

## 🎉 ¡Listo para Comenzar!

Si llegaste hasta aquí y todo funciona correctamente, ¡estás listo para comenzar tu aventura en Linux!

**Próximos pasos:**

1. Lee el **README.md** para entender el sistema
2. Ejecuta `./start.sh` para iniciar
3. Intenta resolver el **Reto 1**
4. Diviértete aprendiendo Linux

---

**¿Preguntas?** Consulta el README.md o contacta a tu instructor.

**¡Buena suerte y happy hacking!** 🐧🚀