# 🐧 Taller de Linux - Challenge Lab

## 📋 Información General

**Nombre del Taller**: Linux Command Line Challenge Lab  
**Modalidad**: Práctica individual con FLAGS personalizadas  
**Duración Estimada**: 4-6 horas  
**Nivel**: Principiante a Avanzado  
**Puntuación Total**: 285 puntos  

---

## 🎯 Objetivos de Aprendizaje

Al completar este taller, serás capaz de:

- ✅ Navegar eficientemente en el sistema de archivos de Linux
- ✅ Manipular archivos y directorios usando comandos básicos
- ✅ Utilizar herramientas de búsqueda y filtrado de texto
- ✅ Gestionar permisos y propiedades de archivos
- ✅ Trabajar con compresión y archivado de archivos
- ✅ Utilizar pipes, redirecciones y filtros avanzados
- ✅ Analizar logs y extraer información relevante
- ✅ Crear y ejecutar scripts bash básicos
- ✅ Gestionar procesos del sistema
- ✅ Trabajar con enlaces simbólicos y duros

---

## 🚀 Configuración Inicial

### Paso 1: Acceder al Laboratorio

**En GitHub Codespaces:**
1. Abre el repositorio en GitHub
2. Haz clic en `Code` → `Codespaces` → `Create codespace on main`
3. Espera a que el entorno se configure automáticamente

**En tu máquina local:**
```bash
git clone <url-del-repositorio>
cd Linux_practica
pip install -r requirements.txt
```

### Paso 2: Configurar tu Entorno Personalizado

**⚠️ IMPORTANTE:** Este laboratorio usa FLAGS personalizadas. Cada estudiante tendrá FLAGS únicas basadas en su código.

```bash
python3 linux_challenge.py setup
```

Cuando se te solicite:
1. **Ingresa tu código de estudiante** (puede ser tu ID institucional, nombre, o código asignado)
2. **Confirma tu código** - asegúrate de que esté correcto
3. El sistema generará FLAGS únicas para ti

**Ejemplo:**
```
👤 Ingresa tu código de estudiante: EST-2024-001
✅ Código registrado: EST-2024-001
¿Es correcto? (s/n): s
```

⚠️ **Anota tu código** - lo necesitarás si reconfiguras el sistema.

### Paso 3: Verificar la Configuración

```bash
# Ver todos los retos disponibles
python3 linux_challenge.py start

# O iniciar el dashboard web
python3 web_dashboard.py
# Luego abre http://localhost:5000 en tu navegador
```

---

## 📖 Cómo Funciona el Taller

### Sistema de Retos

- **15 retos progresivos** organizados por dificultad
- Cada reto tiene una **FLAG** que debes encontrar
- Las FLAGS tienen el formato: `FLAG{descripcion_HASH}`
- El HASH es único para tu código de estudiante

### Sistema de Puntos

| Nivel | Puntos | Cantidad |
|-------|--------|----------|
| 🟢 Principiante | 10 pts | 2 retos |
| 🟡 Intermedio | 15-20 pts | 4 retos |
| 🔴 Avanzado | 20-25 pts | 3 retos |
| 🏆 Experto | 30 pts | 1 reto |
| 🎯 Especializado | 15-30 pts | 5 retos |

### Envío de FLAGS

Cuando encuentres una FLAG, envíala con:

```bash
python3 linux_challenge.py submit "FLAG{tu_flag_aqui}"
```

### Sistema de Pistas

Si te atascas, puedes pedir una pista:

```bash
python3 linux_challenge.py hint <numero_de_reto>
```

**Ejemplo:**
```bash
python3 linux_challenge.py hint 1
```

---

## 🎮 Los 15 Retos

### 🟢 Nivel Principiante

#### **Reto 1: 🔍 Explorador de Archivos Ocultos** (10 pts)

**Objetivo:** Encuentra el archivo oculto en el directorio `~/linux_lab/secretos`

**Conceptos a aplicar:**
- Navegación de directorios (`cd`)
- Listado de archivos (`ls`)
- Archivos ocultos en Linux

**Pista para empezar:**
Los archivos ocultos en Linux comienzan con un punto (`.`). El comando `ls` tiene opciones especiales para verlos.

**¿Qué debes hacer?**
1. Navega al directorio indicado
2. Lista todos los archivos, incluyendo los ocultos
3. Lee el contenido del archivo oculto
4. Encuentra la FLAG y envíala

---

#### **Reto 2: 📖 Lector de Logs** (10 pts)

**Objetivo:** Lee el archivo `~/linux_lab/logs/sistema.log` y encuentra la FLAG

**Conceptos a aplicar:**
- Lectura de archivos de texto
- Comandos: `cat`, `less`, `more`, `grep`

**Pista para empezar:**
Puedes leer archivos de texto completos o buscar patrones específicos dentro de ellos.

**¿Qué debes hacer?**
1. Localiza el archivo de log
2. Lee su contenido completo o busca la palabra "FLAG"
3. Identifica la FLAG y envíala

---

### 🟡 Nivel Intermedio

#### **Reto 3: 🔎 Cazador de Palabras** (15 pts)

**Objetivo:** Busca la palabra 'secreto' en todos los archivos del directorio `~/linux_lab/datos`

**Conceptos a aplicar:**
- Búsqueda de texto con `grep`
- Búsqueda recursiva
- Patrones de búsqueda

**Pista para empezar:**
El comando `grep` puede buscar texto dentro de archivos. Puede buscar en múltiples archivos a la vez.

**¿Qué debes hacer?**
1. Navega al directorio de datos
2. Busca la palabra "secreto" en todos los archivos
3. Encuentra cuál archivo contiene la FLAG
4. Envía la FLAG encontrada

---

#### **Reto 4: 🔐 Maestro de Permisos** (15 pts)

**Objetivo:** Cambia los permisos del archivo `~/linux_lab/config/sistema.conf` a 600 (rw-------)

**Conceptos a aplicar:**
- Sistema de permisos de Linux
- Comando `chmod`
- Permisos numéricos y simbólicos

**Pista para empezar:**
Los permisos 600 significan: lectura y escritura para el propietario, ningún permiso para grupo y otros.

**¿Qué debes hacer?**
1. Verifica los permisos actuales del archivo (`ls -l`)
2. Cambia los permisos a 600 usando `chmod`
3. Lee el archivo para encontrar la FLAG
4. Envía la FLAG

---

#### **Reto 5: 🏗️ Constructor de Estructuras** (15 pts)

**Objetivo:** Crea la estructura de directorios: `~/linux_lab/proyecto/src/main/java/com/app`

**Conceptos a aplicar:**
- Creación de directorios con `mkdir`
- Opción `-p` para crear directorios anidados
- Estructuras de proyectos

**Pista para empezar:**
El comando `mkdir` con la opción `-p` puede crear toda una jerarquía de directorios en un solo comando.

**¿Qué debes hacer?**
1. Crea la estructura de directorios completa
2. Verifica que se creó correctamente
3. Envía la FLAG (el sistema la mostrará al verificar)

---

#### **Reto 6: 📦 Descompresor Experto** (20 pts)

**Objetivo:** Descomprime el archivo `~/linux_lab/archivos/secreto.tar.gz` y encuentra la FLAG

**Conceptos a aplicar:**
- Archivos comprimidos (tar.gz)
- Comando `tar`
- Opciones de descompresión

**Pista para empezar:**
Los archivos `.tar.gz` son archivos tar comprimidos con gzip. El comando `tar` tiene opciones para descomprimir.

**¿Qué debes hacer?**
1. Localiza el archivo comprimido
2. Descomprímelo usando `tar -xzf`
3. Explora los archivos descomprimidos
4. Encuentra y envía la FLAG

---

### 🔴 Nivel Avanzado

#### **Reto 7: 🎯 Filtro de Patrones** (20 pts)

**Objetivo:** Encuentra todas las direcciones IP en el archivo `~/linux_lab/logs/conexiones.log`

**Conceptos a aplicar:**
- Expresiones regulares
- Comando `grep` con patrones
- Opción `-E` para expresiones regulares extendidas

**Pista para empezar:**
Las direcciones IP tienen el formato: número.número.número.número. Puedes usar expresiones regulares para buscarlas.

**¿Qué debes hacer?**
1. Abre el archivo de conexiones
2. Identifica el patrón de las IPs
3. Encuentra todas las IPs en el log
4. La FLAG está entre las líneas del archivo

---

#### **Reto 8: 🔢 Contador de Líneas** (20 pts)

**Objetivo:** Cuenta cuántas líneas contienen la palabra 'ERROR' en `~/linux_lab/logs/errores.log`

**Conceptos a aplicar:**
- Pipes (`|`)
- Comando `grep`
- Comando `wc` (word count)
- Filtrado de líneas

**Pista para empezar:**
Puedes combinar `grep` para filtrar y `wc -l` para contar líneas usando un pipe.

**¿Qué debes hacer?**
1. Usa `grep` para filtrar líneas con "ERROR"
2. Usa `wc -l` para contar las líneas
3. Encuentra la FLAG en el archivo
4. Envía la FLAG

---

#### **Reto 9: 🕵️ Detective de Archivos** (25 pts)

**Objetivo:** Encuentra todos los archivos `.txt` modificados en las últimas 24 horas en `~/linux_lab`

**Conceptos a aplicar:**
- Comando `find`
- Búsqueda por tipo de archivo
- Búsqueda por tiempo de modificación
- Múltiples criterios de búsqueda

**Pista para empezar:**
El comando `find` puede buscar archivos por nombre, tipo, tamaño, fecha de modificación, etc.

**¿Qué debes hacer?**
1. Usa `find` con criterios de nombre (`-name "*.txt"`)
2. Añade criterio de tiempo (`-mtime`)
3. Encuentra el archivo reciente
4. Lee su contenido y envía la FLAG

---

### 🏆 Nivel Experto

#### **Reto 10: 🏆 Challenge Final: El Hash Perdido** (30 pts)

**Objetivo:** Encuentra la FLAG final oculta en un archivo cuyo nombre es el MD5 de tu código + 'linux_master'

**Conceptos a aplicar:**
- Hashing MD5
- Búsqueda de archivos
- Integración de conocimientos
- Comando `md5sum` o `echo -n | md5sum`

**Pista para empezar:**
El nombre del archivo es el hash MD5 de: `{tu_codigo}_linux_master`. Busca en `~/linux_lab/sistema/var/cache/`

**¿Qué debes hacer?**
1. Calcula el MD5 de `{tu_codigo}_linux_master`
2. Busca el archivo con ese nombre en la ruta indicada
3. Lee el contenido del archivo
4. Envía la FLAG final

**Ejemplo de cálculo MD5:**
```bash
echo -n "TU_CODIGO_linux_master" | md5sum
```

---

### 🎯 Nivel Especializado

#### **Reto 11: 📝 Maestro de Redirecciones** (15 pts)

**Objetivo:** Crea un archivo `~/linux_lab/output/resultado.txt` que contenga solo las líneas con 'SUCCESS' de `~/linux_lab/logs/app.log`

**Conceptos a aplicar:**
- Redirección de salida (`>`, `>>`)
- Comando `grep`
- Filtrado de contenido

**Pista para empezar:**
Puedes usar `grep` para filtrar y `>` para redirigir la salida a un archivo.

**¿Qué debes hacer?**
1. Crea el directorio `output` si no existe
2. Filtra las líneas con "SUCCESS" del archivo de log
3. Redirige el resultado a `resultado.txt`
4. Envía la FLAG que aparece en el log

---

#### **Reto 12: ⚙️ Cazador de Procesos** (20 pts)

**Objetivo:** Encuentra el proceso que está usando el puerto 8080 (simulado en un archivo)

**Conceptos a aplicar:**
- Lectura de información de procesos
- Archivo `~/linux_lab/procesos/puertos.txt`
- Comando `grep` para buscar

**Pista para empezar:**
La información del proceso está en un archivo de texto que simula la salida de comandos de procesos.

**¿Qué debes hacer?**
1. Lee el archivo de puertos
2. Encuentra qué proceso usa el puerto 8080
3. Localiza la FLAG en el archivo
4. Envía la FLAG

---

#### **Reto 13: 📜 Escritor de Scripts** (25 pts)

**Objetivo:** Crea un script bash ejecutable llamado `backup.sh` en `~/linux_lab/scripts`

**Conceptos a aplicar:**
- Creación de scripts bash
- Permisos de ejecución (`chmod +x`)
- Shebang (`#!/bin/bash`)
- Variables y comandos básicos

**Pista para empezar:**
Un script bash debe comenzar con `#!/bin/bash` y tener permisos de ejecución.

**¿Qué debes hacer?**
1. Crea el archivo `backup.sh` en el directorio scripts
2. Añade el shebang y contenido básico
3. Dale permisos de ejecución
4. El sistema verificará y mostrará la FLAG

**Script mínimo de ejemplo:**
```bash
#!/bin/bash
echo "Backup iniciado"
# Tu código aquí
```

---

#### **Reto 14: 🔗 Creador de Enlaces** (15 pts)

**Objetivo:** Crea un enlace simbólico llamado `flag_link` que apunte a `~/linux_lab/.enlace_flag.txt`

**Conceptos a aplicar:**
- Enlaces simbólicos
- Comando `ln -s`
- Diferencia entre enlaces simbólicos y duros

**Pista para empezar:**
Los enlaces simbólicos son como accesos directos. Se crean con `ln -s origen destino`.

**¿Qué debes hacer?**
1. Crea el enlace simbólico en el directorio adecuado
2. Verifica que el enlace funciona
3. Lee el contenido a través del enlace
4. Envía la FLAG

---

#### **Reto 15: 🔬 Análisis Forense de Logs** (30 pts)

**Objetivo:** Encuentra las 3 IPs que más aparecen en `~/linux_lab/logs/accesos.log`

**Conceptos a aplicar:**
- Análisis de logs
- Comandos `awk`, `sort`, `uniq`, `head`
- Pipes complejos
- Extracción de columnas

**Pista para empezar:**
Necesitas extraer las IPs, ordenarlas, contarlas y mostrar las más frecuentes. Combina varios comandos con pipes.

**¿Qué debes hacer?**
1. Extrae las direcciones IP del log (columna 4)
2. Ordénalas alfabéticamente
3. Cuenta cuántas veces aparece cada una
4. Ordena por frecuencia y muestra las top 3
5. La FLAG está en el archivo

**Comando de ejemplo:**
```bash
awk '{print $4}' archivo.log | sort | uniq -c | sort -rn | head -3
```

---

## 📊 Sistema de Comandos por Reto

### Comandos Básicos de Navegación

```bash
pwd                 # Mostrar directorio actual
cd <directorio>     # Cambiar de directorio
cd ..               # Subir un nivel
cd ~                # Ir al home
ls                  # Listar archivos
ls -l               # Listar con detalles
ls -la              # Listar todo (incluidos ocultos)
ls -lh              # Listar con tamaños legibles
```

### Lectura de Archivos

```bash
cat archivo.txt         # Mostrar contenido completo
less archivo.txt        # Ver archivo (paginado)
more archivo.txt        # Ver archivo (simple)
head -n 10 archivo.txt  # Primeras 10 líneas
tail -n 10 archivo.txt  # Últimas 10 líneas
tail -f archivo.log     # Seguir un archivo en tiempo real
```

### Búsqueda y Filtrado

```bash
grep "palabra" archivo.txt          # Buscar palabra en archivo
grep -r "palabra" directorio/       # Buscar recursivamente
grep -i "palabra" archivo.txt       # Búsqueda case-insensitive
grep -v "palabra" archivo.txt       # Invertir búsqueda (excluir)
grep -E "patrón" archivo.txt        # Expresiones regulares
find . -name "*.txt"                # Buscar archivos por nombre
find . -type f -mtime -1            # Archivos modificados hace menos de 1 día
```

### Permisos

```bash
chmod 600 archivo              # Cambiar permisos (numérico)
chmod u+x script.sh            # Dar permisos de ejecución al usuario
chmod -R 755 directorio/       # Cambiar permisos recursivamente
ls -l archivo                  # Ver permisos de archivo
```

### Directorios

```bash
mkdir directorio               # Crear directorio
mkdir -p a/b/c/d              # Crear directorios anidados
rmdir directorio              # Eliminar directorio vacío
rm -r directorio              # Eliminar directorio y contenido
```

### Compresión

```bash
tar -czf archivo.tar.gz directorio/    # Comprimir
tar -xzf archivo.tar.gz                # Descomprimir
tar -tzf archivo.tar.gz                # Ver contenido sin descomprimir
gzip archivo                           # Comprimir con gzip
gunzip archivo.gz                      # Descomprimir gzip
```

### Redirecciones y Pipes

```bash
comando > archivo.txt          # Redirigir salida (sobrescribe)
comando >> archivo.txt         # Redirigir salida (añade)
comando < archivo.txt          # Redirigir entrada
comando 2> errores.txt         # Redirigir errores
comando &> todo.txt            # Redirigir salida y errores
comando1 | comando2            # Pipe: salida de cmd1 a entrada de cmd2
```

### Análisis de Texto

```bash
wc -l archivo.txt              # Contar líneas
wc -w archivo.txt              # Contar palabras
sort archivo.txt               # Ordenar líneas
uniq archivo.txt               # Eliminar duplicados consecutivos
uniq -c archivo.txt            # Contar ocurrencias
cut -d':' -f1 archivo.txt      # Cortar por delimitador
awk '{print $1}' archivo.txt   # Imprimir primera columna
sed 's/viejo/nuevo/g' archivo  # Reemplazar texto
```

### Enlaces

```bash
ln -s origen enlace_simbolico  # Crear enlace simbólico
ln origen enlace_duro          # Crear enlace duro
ls -l                          # Ver enlaces (símbolo ->)
readlink enlace                # Ver destino del enlace
```

### Utilidades

```bash
echo "texto"                   # Imprimir texto
echo -n "texto" | md5sum       # Calcular MD5
date                           # Fecha y hora actual
whoami                         # Usuario actual
which comando                  # Ubicación de un comando
man comando                    # Manual de un comando
```

---

## 💡 Consejos y Buenas Prácticas

### 1. Explora Antes de Actuar
```bash
# Siempre verifica dónde estás
pwd

# Lista el contenido antes de moverte
ls -la
```

### 2. Usa Tab para Autocompletar
- Presiona `Tab` para autocompletar nombres de archivos y directorios
- Presiona `Tab` dos veces para ver todas las opciones

### 3. Historial de Comandos
```bash
# Flecha arriba/abajo para ver comandos anteriores
# Ctrl+R para buscar en el historial
history | grep "comando"
```

### 4. Lee los Mensajes de Error
- Los errores te dicen exactamente qué está mal
- "No such file or directory" → el archivo/directorio no existe
- "Permission denied" → no tienes permisos

### 5. Usa el Manual
```bash
man ls          # Manual del comando ls
ls --help       # Ayuda rápida
```

### 6. Testa Comandos Destructivos
```bash
# Antes de borrar, lista qué se va a borrar
rm archivo.txt           # ¡Cuidado!
ls archivo.txt          # Verifica primero que existe
```

### 7. Guarda tus Comandos Útiles
- Crea un archivo `notas.txt` con comandos que te funcionen
- Documenta qué hace cada uno

---

## 📈 Seguimiento de Progreso

### Ver Tu Estado Actual

```bash
python3 linux_challenge.py status
```

Verás:
- Retos completados
- Puntos totales
- Porcentaje de completación
- Últimos retos resueltos
- Próximo reto sugerido

### Ver Todos los Retos

```bash
python3 linux_challenge.py start
```

### Dashboard Web

```bash
python3 web_dashboard.py
```

Luego abre `http://localhost:5000` para ver:
- Estadísticas en tiempo real
- Lista de todos los retos
- Formulario para enviar FLAGS
- Sistema de pistas interactivo

---

## 🎓 Niveles de Logro

| Nivel | Puntos | Insignia |
|-------|--------|----------|
| 🥉 **Bronce** | 0-70 pts | Principiante |
| 🥈 **Plata** | 71-140 pts | Intermedio |
| 🥇 **Oro** | 141-215 pts | Avanzado |
| 🏆 **Maestro** | 216-285 pts | Experto en Linux |

**Meta:** ¡Alcanza el nivel de Maestro completando los 15 retos!

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo resolver los retos en cualquier orden?**  
R: Se recomienda seguir el orden, ya que aumentan en dificultad. Pero técnicamente puedes intentar cualquiera.

**P: ¿Qué pasa si envío una FLAG incorrecta?**  
R: El sistema te dirá que es incorrecta y podrás intentar de nuevo sin penalización.

**P: ¿Puedo usar Google para buscar comandos?**  
R: ¡Sí! En el mundo real, buscar documentación es parte del trabajo. Solo no compartas FLAGS con otros.

**P: ¿Cuántas veces puedo pedir pistas?**  
R: Ilimitadas. Las pistas están para ayudarte a aprender.

**P: ¿Qué pasa si borro accidentalmente archivos del laboratorio?**  
R: Puedes reconfigurar todo con `python3 linux_challenge.py setup` (perderás tu progreso).

**P: ¿Las FLAGS son las mismas para todos?**  
R: No, cada estudiante tiene FLAGS personalizadas basadas en su código.

**P: ¿Puedo trabajar en equipo?**  
R: Puedes discutir conceptos y comandos, pero cada uno debe resolver y enviar sus propias FLAGS.

---

## 🚨 Solución de Problemas

### El comando no funciona
```bash
# Verifica que estás escribiendo correctamente
ls -la    # ✓ Correcto
ls - la   # ✗ Incorrecto (espacio extra)
```

### No encuentro el archivo
```bash
# Verifica que estás en el directorio correcto
pwd

# Busca el archivo
find ~ -name "nombre_archivo"
```

### Permission denied
```bash
# Verifica los permisos
ls -l archivo

# Cambia permisos si es necesario
chmod +r archivo    # Añadir lectura
chmod +x script     # Añadir ejecución
```

### No puedo salir de un comando
- `Ctrl+C` para cancelar comando actual
- `Ctrl+D` para salir de sesión interactiva
- `q` para salir de `less` o `man`

---

## 📚 Recursos Adicionales

### Documentación de Comandos
```bash
man <comando>        # Manual completo
<comando> --help     # Ayuda rápida
info <comando>       # Información detallada
```

### Tutoriales Recomendados
- [Linux Journey](https://linuxjourney.com/) - Tutorial interactivo
- [The Linux Command Line](http://linuxcommand.org/) - Libro gratuito
- [ExplainShell](https://explainshell.com/) - Explica comandos complejos

### Cheat Sheets
- [Linux Command Cheat Sheet](https://www.loggly.com/wp-content/uploads/2015/05/Linux-Cheat-Sheet-Sponsored-By-Loggly.pdf)
- [Bash Scripting Cheat Sheet](https://devhints.io/bash)

---

## ✅ Lista de Verificación Final

Antes de finalizar, asegúrate de:

- [ ] Haber configurado tu código de estudiante
- [ ] Haber resuelto al menos 10 de 15 retos
- [ ] Haber alcanzado mínimo 150 puntos
- [ ] Haber documentado comandos útiles que aprendiste
- [ ] Haber verificado tu progreso con `status`
- [ ] Haber enviado todas las FLAGS encontradas

---

## 🎉 ¡Buena Suerte!

Recuerda:
- **Aprende haciendo** - la práctica es la mejor maestra
- **No tengas miedo de equivocarte** - los errores son oportunidades de aprendizaje
- **Experimenta** - prueba variaciones de comandos
- **Documenta** - anota lo que aprendes
- **Diviértete** - ¡Linux es poderoso y emocionante!

---

**Versión del Taller**: 2.1  
**Última Actualización**: Octubre 2025  
**Autor**: Sistema Linux Challenge Lab  

💻 Happy Hacking! 🐧
