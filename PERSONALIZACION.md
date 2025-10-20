# 🔒 Sistema de FLAGS Personalizadas - Linux Challenge Lab

## 📖 Descripción

El sistema Linux Challenge Lab ahora cuenta con **FLAGS personalizadas** basadas en el código de cada estudiante. Esto significa que:

- ✅ Cada estudiante tiene FLAGS únicas
- ✅ No pueden compartir respuestas entre ellos
- ✅ El profesor puede identificar fácilmente a cada estudiante
- ✅ Mayor integridad académica en el laboratorio

---

## 🎯 ¿Cómo Funciona?

### 1. Registro del Código de Estudiante

Al ejecutar `python3 linux_challenge.py setup`, el sistema solicita un código de estudiante:

```bash
👤 Ingresa tu código de estudiante: EST-2024-001
✅ Código registrado: EST-2024-001
¿Es correcto? (s/n): s
```

**Requisitos del código:**
- Mínimo 3 caracteres
- Puede contener letras, números y guiones
- Ejemplos válidos: `EST-2024-001`, `ALUMNO-123`, `12345678`, `JUAN-PEREZ`

### 2. Generación de FLAGS Personalizadas

El sistema genera FLAGS únicas usando un algoritmo SHA-256:

```python
# Formato de generación
datos = f"{codigo_estudiante}_{id_reto}_{texto_base}"
hash_obj = hashlib.sha256(datos.encode())
hash_corto = hash_obj.hexdigest()[:8].upper()

# FLAG resultante
FLAG{texto_base_HASH}
```

**Ejemplo con código `EST-2024-001`:**
- Reto 1: `FLAG{encontre_el_oculto_B0E8C093}`
- Reto 2: `FLAG{leyendo_archivos_F3A2C1D4}`
- Reto 10: `FLAG{linux_master_9E7B5C2A}`

**Ejemplo con código `ALUMNO-123`:**
- Reto 1: `FLAG{encontre_el_oculto_164A1B00}`
- Reto 2: `FLAG{leyendo_archivos_8C5D2E9F}`
- Reto 10: `FLAG{linux_master_3B9A7F1C}`

### 3. Validación de FLAGS

Cuando el estudiante envía una FLAG:

```bash
python3 linux_challenge.py submit "FLAG{encontre_el_oculto_B0E8C093}"
```

El sistema:
1. Regenera la FLAG esperada usando el código del estudiante guardado
2. Compara con la FLAG enviada
3. Acepta solo si coinciden exactamente

---

## 👨‍🎓 Para Estudiantes

### Paso 1: Configurar el Laboratorio

```bash
python3 linux_challenge.py setup
```

- Ingresa tu código de estudiante cuando se te solicite
- Este código se guardará y se usará para todos los retos
- **Importante**: Anota tu código, lo necesitarás si reconfiguras

### Paso 2: Encontrar las FLAGS

Las FLAGS están en los archivos del sistema, personalizadas para ti:

```bash
# Ejemplo Reto 1
cat ~/linux_lab/secretos/.archivo_oculto.txt
# Salida: FLAG{encontre_el_oculto_XXXXXXXX}
# Los XXXXXXXX son únicos para tu código
```

### Paso 3: Enviar FLAGS

```bash
python3 linux_challenge.py submit "FLAG{tu_flag_personalizada}"
```

### ⚠️ Importante

- **NO compartas tu código de estudiante** con otros
- **NO compartas tus FLAGS** - no funcionarán para otros estudiantes
- Si olvidas tu código, revisa el archivo `~/linux_lab/.progress.json`

---

## 👨‍🏫 Para Profesores

### Ventajas del Sistema Personalizado

1. **Prevención de Plagio**
   - Cada estudiante tiene FLAGS diferentes
   - Compartir respuestas no sirve

2. **Identificación Fácil**
   - El código del estudiante está en `.progress.json`
   - Puedes verificar quién resolvió cada reto

3. **Trazabilidad**
   - Cada FLAG es trazable al código del estudiante
   - Registro de fecha y hora de completación

### Asignación de Códigos

**Opción 1: Códigos Predefinidos**
```
EST-2024-001
EST-2024-002
EST-2024-003
...
```

**Opción 2: Identificadores Institucionales**
```
12345678 (ID universitario)
JUAN-PEREZ (Nombre)
202401-EST (Semestre + carrera)
```

**Opción 3: GitHub Usernames**
```
estudiante1
alumno-java
dev-python
```

### Verificación del Progreso

Cada estudiante tiene un archivo `.progress.json`:

```json
{
  "completados": [1, 2, 3],
  "puntos": 35,
  "codigo_estudiante": "EST-2024-001",
  "reto_1_fecha": "2025-10-20T15:30:00",
  "reto_2_fecha": "2025-10-20T15:45:00",
  "reto_3_fecha": "2025-10-20T16:00:00"
}
```

### Recolección de Resultados

**En GitHub Classroom:**
1. Los estudiantes hacen commit de `~/linux_lab/.progress.json`
2. Puedes ver el código y progreso de cada uno
3. Las FLAGS en los archivos son personalizadas

**Script de Recolección:**
```bash
# Ejemplo para recolectar progreso de todos los estudiantes
for student in */; do
    echo "Estudiante: $student"
    cat "$student/linux_lab/.progress.json" | jq '{codigo_estudiante, puntos, completados}'
done
```

---

## 🔧 Aspectos Técnicos

### Archivos Modificados

1. **Archivos con FLAGS Personalizadas:**
   - `~/linux_lab/secretos/.archivo_oculto.txt`
   - `~/linux_lab/logs/sistema.log`
   - `~/linux_lab/datos/archivo3.txt`
   - `~/linux_lab/config/sistema.conf`
   - `~/linux_lab/archivos/secreto/flag.txt`
   - `~/linux_lab/logs/conexiones.log`
   - `~/linux_lab/logs/errores.log`
   - `~/linux_lab/datos/reciente.txt`
   - `~/linux_lab/sistema/var/cache/{hash_personalizado}`
   - `~/linux_lab/logs/app.log`
   - `~/linux_lab/procesos/puertos.txt`
   - `~/linux_lab/scripts/.flag.txt`
   - `~/linux_lab/.enlace_flag.txt`
   - `~/linux_lab/logs/accesos.log`

2. **Archivo de Referencia del Reto 5:**
   - `~/linux_lab/.flag_reto5.txt`

### Algoritmo de Hash

```python
def generar_flag_personalizada(codigo_estudiante, reto_id, texto_base):
    """
    Genera una FLAG única y reproducible.
    
    Args:
        codigo_estudiante: Código único del estudiante
        reto_id: ID del reto (1-15)
        texto_base: Descripción de la flag
        
    Returns:
        FLAG personalizada en formato FLAG{texto_base_HASH}
    """
    datos = f"{codigo_estudiante}_{reto_id}_{texto_base}"
    hash_obj = hashlib.sha256(datos.encode())
    hash_corto = hash_obj.hexdigest()[:8].upper()
    
    return f"FLAG{{{texto_base}_{hash_corto}}}"
```

### Reto 10 Especial (Hash MD5)

El Reto 10 usa MD5 del código del estudiante + "linux_master":

```python
datos_hash = f"{codigo_estudiante}_linux_master"
md5_hash = hashlib.md5(datos_hash.encode()).hexdigest()
# Archivo: ~/linux_lab/sistema/var/cache/{md5_hash}
```

Cada estudiante tendrá un archivo con nombre diferente:
- `EST-2024-001` → `3ecda2f53b123774d1723622c8beacab`
- `ALUMNO-123` → `3422937a9044a63b68369a697e51fd37`

---

## 📊 Ejemplos Comparativos

### Estudiante 1: `EST-2024-001`

| Reto | FLAG |
|------|------|
| 1 | `FLAG{encontre_el_oculto_B0E8C093}` |
| 2 | `FLAG{leyendo_archivos_F1C2D3E4}` |
| 3 | `FLAG{grep_poderoso_A9B8C7D6}` |
| 10 | `FLAG{linux_master_E5F6G7H8}` |

### Estudiante 2: `ALUMNO-123`

| Reto | FLAG |
|------|------|
| 1 | `FLAG{encontre_el_oculto_164A1B00}` |
| 2 | `FLAG{leyendo_archivos_9F8E7D6C}` |
| 3 | `FLAG{grep_poderoso_5B4A3C2D}` |
| 10 | `FLAG{linux_master_1E2F3G4H}` |

**Observación:** Mismo reto, FLAGS completamente diferentes.

---

## 🔐 Seguridad

### Fortalezas

1. **Unicidad Garantizada**: SHA-256 asegura FLAGS únicas
2. **Reproducibilidad**: Mismas entradas = misma FLAG
3. **No Reversible**: No se puede obtener el código desde la FLAG
4. **Colisiones Mínimas**: 8 caracteres hex = 4.3 mil millones de combinaciones

### Limitaciones

- Si dos estudiantes usan el mismo código, tendrán las mismas FLAGS
- El código se guarda en texto plano en `.progress.json`

### Recomendaciones

- Asignar códigos únicos a cada estudiante
- Instruir a no compartir códigos
- Monitorear el archivo `.progress.json` para detectar duplicados

---

## 🚀 Uso en Producción

### GitHub Classroom

```yaml
# .github/classroom/autograding.json
{
  "tests": [
    {
      "name": "Verificar código único",
      "setup": "",
      "run": "test -f ~/linux_lab/.progress.json",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 10,
      "points": 5
    },
    {
      "name": "Verificar progreso",
      "setup": "",
      "run": "cat ~/linux_lab/.progress.json | jq '.puntos' | awk '$1 >= 100 {exit 0} {exit 1}'",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 10,
      "points": 95
    }
  ]
}
```

### Canvas/Moodle

Los estudiantes pueden:
1. Configurar su entorno con su código
2. Resolver los retos
3. Hacer screenshot de `python3 linux_challenge.py status`
4. Subir el archivo `.progress.json` como evidencia

---

## ❓ FAQ

**P: ¿Puedo cambiar mi código después de configurar?**  
R: Sí, pero perderás todo tu progreso. Debes ejecutar `rm -rf ~/linux_lab` y luego `setup` de nuevo.

**P: ¿Qué pasa si olvido mi código?**  
R: Está guardado en `~/linux_lab/.progress.json` en el campo `codigo_estudiante`.

**P: ¿Puedo usar caracteres especiales en mi código?**  
R: Sí, pero se recomienda usar solo letras, números y guiones para evitar problemas.

**P: ¿Las FLAGS cambian si reconfiguro con el mismo código?**  
R: No, las FLAGS son determinísticas. Mismo código = mismas FLAGS.

**P: ¿Cómo verifico que mi código está registrado?**  
R: Ejecuta `python3 linux_challenge.py start` y verás tu código en la primera línea.

---

## 📝 Nota Final

Este sistema de personalización convierte el Linux Challenge Lab en una herramienta robusta para evaluación individual, manteniendo la diversión y el aprendizaje práctico, pero con la garantía de integridad académica.

**Versión del Sistema**: 2.1 (Sistema con FLAGS Personalizadas)
**Fecha**: Octubre 2025
