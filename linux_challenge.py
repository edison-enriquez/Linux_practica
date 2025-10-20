#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux Challenge Lab - Sistema de Retos CTF
Sistema principal de gestión de retos para aprendizaje de comandos Linux
"""

import os
import sys
import json
import stat
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class LinuxChallenge:
    """
    Clase principal que gestiona el sistema de retos de Linux.
    Maneja la configuración, verificación de retos y progreso del usuario.
    """

    def __init__(self):
        """Inicializa la configuración del sistema de retos"""
        self.home_dir = Path.home()
        self.lab_dir = self.home_dir / "linux_lab"
        self.progress_file = self.lab_dir / ".progress.json"
        self.codigo_estudiante = None
        
        # Cargar código de estudiante si existe
        if self.progress_file.exists():
            progress = self._cargar_progreso()
            self.codigo_estudiante = progress.get("codigo_estudiante")
        
        # Definición de todos los retos del sistema
        self.retos = [
            {
                "id": 1,
                "nombre": "🔍 Explorador de Archivos Ocultos",
                "descripcion": "Encuentra el archivo oculto en el directorio ~/linux_lab/secretos",
                "pista": "Los archivos ocultos en Linux comienzan con un punto (.). Usa 'ls -la' para verlos.",
                "flag": "FLAG{encontre_el_oculto}",
                "puntos": 10,
                "dificultad": "Principiante",
                "categoria": "Navegación"
            },
            {
                "id": 2,
                "nombre": "📖 Lector de Logs",
                "descripcion": "Lee el contenido del archivo ~/linux_lab/logs/sistema.log y encuentra la flag",
                "pista": "Usa 'cat', 'less' o 'more' para leer archivos de texto.",
                "flag": "FLAG{leyendo_archivos_como_pro}",
                "puntos": 10,
                "dificultad": "Principiante",
                "categoria": "Lectura de archivos"
            },
            {
                "id": 3,
                "nombre": "🔎 Cazador de Palabras",
                "descripcion": "Busca la palabra 'secreto' en todos los archivos del directorio ~/linux_lab/datos",
                "pista": "El comando 'grep' es perfecto para buscar texto. Usa 'grep -r' para búsqueda recursiva.",
                "flag": "FLAG{grep_es_poderoso}",
                "puntos": 15,
                "dificultad": "Principiante",
                "categoria": "Búsqueda de texto"
            },
            {
                "id": 4,
                "nombre": "🔐 Maestro de Permisos",
                "descripcion": "Cambia los permisos del archivo ~/linux_lab/config/sistema.conf a 600 (rw-------)",
                "pista": "Usa 'chmod 600 archivo' para dar permisos de lectura/escritura solo al propietario.",
                "flag": "FLAG{permisos_configurados}",
                "puntos": 15,
                "dificultad": "Intermedio",
                "categoria": "Permisos"
            },
            {
                "id": 5,
                "nombre": "🏗️ Constructor de Estructuras",
                "descripcion": "Crea la estructura de directorios: ~/linux_lab/proyecto/src/main/java/com/app",
                "pista": "Usa 'mkdir -p' para crear directorios anidados en un solo comando.",
                "flag": "FLAG{estructura_creada}",
                "puntos": 15,
                "dificultad": "Intermedio",
                "categoria": "Creación de directorios"
            },
            {
                "id": 6,
                "nombre": "📦 Descompresor Experto",
                "descripcion": "Descomprime el archivo ~/linux_lab/archivos/secreto.tar.gz y encuentra la flag",
                "pista": "Usa 'tar -xzf archivo.tar.gz' para descomprimir archivos .tar.gz",
                "flag": "FLAG{descompresion_exitosa}",
                "puntos": 20,
                "dificultad": "Intermedio",
                "categoria": "Compresión"
            },
            {
                "id": 7,
                "nombre": "🎯 Filtro de Patrones",
                "descripcion": "Encuentra todas las direcciones IP en el archivo ~/linux_lab/logs/conexiones.log",
                "pista": "Usa grep con expresiones regulares: grep -E '[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}'",
                "flag": "FLAG{regex_master}",
                "puntos": 20,
                "dificultad": "Avanzado",
                "categoria": "Expresiones regulares"
            },
            {
                "id": 8,
                "nombre": "🔢 Contador de Líneas",
                "descripcion": "Cuenta cuántas líneas contienen la palabra 'ERROR' en ~/linux_lab/logs/errores.log",
                "pista": "Combina 'grep' con 'wc -l' usando pipes: grep 'palabra' archivo | wc -l",
                "flag": "FLAG{contador_experto}",
                "puntos": 20,
                "dificultad": "Avanzado",
                "categoria": "Pipes y filtros"
            },
            {
                "id": 9,
                "nombre": "🕵️ Detective de Archivos",
                "descripcion": "Encuentra todos los archivos .txt modificados en las últimas 24 horas en ~/linux_lab",
                "pista": "Usa 'find' con -name y -mtime: find . -name '*.txt' -mtime -1",
                "flag": "FLAG{find_es_increible}",
                "puntos": 25,
                "dificultad": "Avanzado",
                "categoria": "Búsqueda avanzada"
            },
            {
                "id": 10,
                "nombre": "🏆 Challenge Final: El Hash Perdido",
                "descripcion": "Encuentra la flag final oculta en un archivo cuyo nombre es el MD5 de 'linux_master'",
                "pista": "El hash MD5 de 'linux_master' es un nombre de archivo. Usa 'find' y 'md5sum' para descubrirlo.",
                "flag": "FLAG{linux_master_2024}",
                "puntos": 30,
                "dificultad": "Experto",
                "categoria": "Challenge Final"
            },
            {
                "id": 11,
                "nombre": "📝 Maestro de Redirecciones",
                "descripcion": "Crea un archivo llamado ~/linux_lab/output/resultado.txt que contenga solo las líneas con 'SUCCESS' del archivo ~/linux_lab/logs/app.log",
                "pista": "Usa redirecciones: grep 'SUCCESS' archivo.log > resultado.txt",
                "flag": "FLAG{redireccion_exitosa}",
                "puntos": 15,
                "dificultad": "Intermedio",
                "categoria": "Redirecciones"
            },
            {
                "id": 12,
                "nombre": "⚙️ Cazador de Procesos",
                "descripcion": "Encuentra el proceso que está usando el puerto 8080 (simulado en un archivo)",
                "pista": "Lee el archivo ~/linux_lab/procesos/puertos.txt y busca el proceso del puerto 8080",
                "flag": "FLAG{proceso_encontrado}",
                "puntos": 20,
                "dificultad": "Intermedio",
                "categoria": "Procesos"
            },
            {
                "id": 13,
                "nombre": "📜 Escritor de Scripts",
                "descripcion": "Crea un script ~/linux_lab/scripts/contador.sh que cuente archivos .log en ~/linux_lab/logs",
                "pista": "#!/bin/bash seguido de: ls ~/linux_lab/logs/*.log | wc -l. No olvides chmod +x",
                "flag": "FLAG{script_funcional}",
                "puntos": 25,
                "dificultad": "Avanzado",
                "categoria": "Scripting"
            },
            {
                "id": 14,
                "nombre": "🔗 Creador de Enlaces",
                "descripcion": "Crea un enlace simbólico llamado ~/linux_lab/acceso_rapido que apunte a ~/linux_lab/datos",
                "pista": "Usa 'ln -s origen destino' para crear enlaces simbólicos",
                "flag": "FLAG{enlace_simbolico}",
                "puntos": 15,
                "dificultad": "Intermedio",
                "categoria": "Enlaces"
            },
            {
                "id": 15,
                "nombre": "🔍 Analizador de Logs Avanzado",
                "descripcion": "Encuentra las 3 IPs que más aparecen en ~/linux_lab/logs/accesos.log",
                "pista": "Combina grep, sort, uniq -c y head: grep -oE 'IP_PATTERN' | sort | uniq -c | sort -rn | head -3",
                "flag": "FLAG{analisis_avanzado}",
                "puntos": 30,
                "dificultad": "Experto",
                "categoria": "Análisis de datos"
            }
        ]
        
        self.progress = self.load_progress()

    def setup_environment(self) -> bool:
        """
        Configura todo el entorno del laboratorio de retos.
        Crea directorios, archivos y estructura necesaria para todos los retos.
        """
        try:
            print("🚀 Configurando el entorno de Linux Challenge Lab...")
            print("=" * 60)
            
            # Solicitar código de estudiante si no existe
            if not self.codigo_estudiante:
                self.codigo_estudiante = self.solicitar_codigo_estudiante()
                # Guardar el código inmediatamente
                self.progress["codigo_estudiante"] = self.codigo_estudiante
                self.save_progress()
                print(f"\n✅ Tu código '{self.codigo_estudiante}' ha sido guardado.")
                print("   Tus FLAGS serán únicas y personalizadas.\n")
            else:
                print(f"\n👤 Código de estudiante registrado: {self.codigo_estudiante}")
                print("   Tus FLAGS están personalizadas para tu código.\n")
            
            # Crear directorio principal
            self.lab_dir.mkdir(exist_ok=True)
            print(f"✅ Directorio principal creado: {self.lab_dir}")
            
            # Generar flags personalizadas
            flag1 = self.generar_flag_personalizada(1, "encontre_el_oculto")
            flag2 = self.generar_flag_personalizada(2, "leyendo_archivos")
            flag6 = self.generar_flag_personalizada(6, "descomprimir_experto")
            flag10 = self.generar_flag_personalizada(10, "linux_master")
            
            # ===== RETO 1: Archivo oculto =====
            secretos_dir = self.lab_dir / "secretos"
            secretos_dir.mkdir(exist_ok=True)
            archivo_oculto = secretos_dir / ".archivo_oculto.txt"
            archivo_oculto.write_text(f"{flag1}\n¡Felicidades! Has encontrado el archivo oculto.\nTu flag personalizada: {flag1}")
            print("✅ Reto 1: Archivo oculto creado")
            
            # ===== RETO 2: Archivo de logs =====
            logs_dir = self.lab_dir / "logs"
            # ===== RETO 2: Archivo de log con flag =====
            logs_dir = self.lab_dir / "logs"
            logs_dir.mkdir(exist_ok=True)
            
            sistema_log = logs_dir / "sistema.log"
            contenido_log = ("2024-01-15 10:00:00 Sistema iniciado\n"
                           "2024-01-15 10:01:23 Usuario login: admin\n"
                           "2024-01-15 10:02:45 Proceso completado exitosamente\n"
                           f"2024-01-15 10:03:12 {flag2}\n"
                           "2024-01-15 10:04:00 Sistema funcionando correctamente\n")
            sistema_log.write_text(contenido_log)
            print("✅ Reto 2: Archivo de logs creado")
            
            # Generar más flags personalizadas
            flag3 = self.generar_flag_personalizada(3, "grep_poderoso")
            flag4 = self.generar_flag_personalizada(4, "permisos_configurados")
            flag5 = self.generar_flag_personalizada(5, "estructura_creada")
            
            # ===== RETO 3: Archivos con texto para grep =====
            datos_dir = self.lab_dir / "datos"
            datos_dir.mkdir(exist_ok=True)
            
            (datos_dir / "archivo1.txt").write_text("Este es un archivo normal\nCon varias líneas\n")
            (datos_dir / "archivo2.txt").write_text("Aquí hay información importante\nPero no es lo que buscas\n")
            (datos_dir / "archivo3.txt").write_text(f"La palabra secreto está aquí\n{flag3}\n")
            print("✅ Reto 3: Archivos de datos creados")
            
            # ===== RETO 4: Archivo de configuración con permisos =====
            config_dir = self.lab_dir / "config"
            config_dir.mkdir(exist_ok=True)
            sistema_conf = config_dir / "sistema.conf"
            sistema_conf.write_text(f"# Configuración del sistema\n{flag4}\n")
            os.chmod(sistema_conf, 0o644)  # Permisos iniciales: rw-r--r--
            print("✅ Reto 4: Archivo de configuración creado con permisos 644")
            
            # ===== RETO 5: Se verificará cuando el usuario cree la estructura =====
            # Guardar flag5 en un archivo de referencia
            (self.lab_dir / ".flag_reto5.txt").write_text(flag5)
            print("✅ Reto 5: Preparado para verificación de estructura")
            
            # ===== RETO 6: Archivo comprimido =====
            archivos_dir = self.lab_dir / "archivos"
            archivos_dir.mkdir(exist_ok=True)
            
            # Crear archivo temporal con la flag
            temp_dir = archivos_dir / "temp_secreto"
            temp_dir.mkdir(exist_ok=True)
            (temp_dir / "flag.txt").write_text(f"{flag6}\n¡Excelente! Has descomprimido el archivo correctamente.")
            
            # Comprimir el archivo
            import tarfile
            tar_file = archivos_dir / "secreto.tar.gz"
            with tarfile.open(tar_file, "w:gz") as tar:
                tar.add(temp_dir, arcname="secreto")
            
            # Eliminar el directorio temporal
            import shutil
            shutil.rmtree(temp_dir)
            print("✅ Reto 6: Archivo comprimido creado")
            
            # Generar más flags personalizadas
            flag7 = self.generar_flag_personalizada(7, "regex_master")
            flag8 = self.generar_flag_personalizada(8, "contador_experto")
            flag9 = self.generar_flag_personalizada(9, "find_increible")
            
            # ===== RETO 7: Archivo con IPs =====
            conexiones_log = logs_dir / "conexiones.log"
            contenido_conexiones = ("2024-01-15 10:00:00 Conexión desde 192.168.1.100\n"
                                   "2024-01-15 10:05:00 Conexión desde 10.0.0.50\n"
                                   f"2024-01-15 10:10:00 {flag7}\n"
                                   "2024-01-15 10:15:00 Conexión desde 172.16.0.1\n"
                                   "2024-01-15 10:20:00 Conexión desde 8.8.8.8\n")
            conexiones_log.write_text(contenido_conexiones)
            print("✅ Reto 7: Archivo de conexiones creado")
            
            # ===== RETO 8: Archivo con errores =====
            errores_log = logs_dir / "errores.log"
            contenido_errores = (f"INFO: Sistema iniciado\n"
                               "ERROR: Fallo en módulo A\n"
                               "WARNING: Advertencia general\n"
                               "ERROR: Fallo en módulo B\n"
                               "INFO: Proceso completado\n"
                               "ERROR: Fallo en módulo C\n"
                               f"{flag8}\n")
            errores_log.write_text(contenido_errores)
            print("✅ Reto 8: Archivo de errores creado")
            
            # ===== RETO 9: Crear archivo .txt reciente =====
            (datos_dir / "reciente.txt").write_text(f"{flag9}\nArchivo reciente para el reto de find.")
            # Actualizar tiempo de modificación a ahora
            os.utime(datos_dir / "reciente.txt", None)
            print("✅ Reto 9: Archivo reciente creado")
            
            # ===== RETO 10: Hash MD5 =====
            # Calcular MD5 del código del estudiante + "linux_master"
            datos_hash = f"{self.codigo_estudiante}_linux_master"
            md5_hash = hashlib.md5(datos_hash.encode()).hexdigest()
            sistema_dir = self.lab_dir / "sistema" / "var" / "cache"
            sistema_dir.mkdir(parents=True, exist_ok=True)
            
            hash_file = sistema_dir / md5_hash
            hash_file.write_text(f"{flag10}\n¡FELICIDADES! Has completado el reto final.\n¡Eres un maestro de Linux!")
            print(f"✅ Reto 10: Archivo hash creado ({md5_hash})")
            
            # Generar flags para retos 11-15
            flag11 = self.generar_flag_personalizada(11, "redireccion_exitosa")
            flag12 = self.generar_flag_personalizada(12, "proceso_encontrado")
            flag13 = self.generar_flag_personalizada(13, "script_maestro")
            flag14 = self.generar_flag_personalizada(14, "enlace_creado")
            flag15 = self.generar_flag_personalizada(15, "analista_experto")
            
            # ===== RETO 11: Redirecciones =====
            output_dir = self.lab_dir / "output"
            output_dir.mkdir(exist_ok=True)
            
            app_log = logs_dir / "app.log"
            contenido_app = ("2024-01-15 10:00:00 SUCCESS Usuario autenticado\n"
                           "2024-01-15 10:01:00 ERROR Fallo en conexión\n"
                           "2024-01-15 10:02:00 SUCCESS Operación completada\n"
                           "2024-01-15 10:03:00 WARNING Memoria baja\n"
                           "2024-01-15 10:04:00 SUCCESS Datos guardados\n"
                           f"{flag11}\n")
            app_log.write_text(contenido_app)
            print("✅ Reto 11: Archivo de aplicación creado")
            
            # ===== RETO 12: Procesos =====
            procesos_dir = self.lab_dir / "procesos"
            procesos_dir.mkdir(exist_ok=True)
            
            puertos_file = procesos_dir / "puertos.txt"
            contenido_puertos = (f"Puerto 80: nginx (PID 1234)\n"
                               "Puerto 443: nginx (PID 1234)\n"
                               "Puerto 3000: node (PID 5678)\n"
                               "Puerto 5432: postgres (PID 2345)\n"
                               "Puerto 8080: java_app (PID 9876)\n"
                               f"{flag12}\n")
            puertos_file.write_text(contenido_puertos)
            print("✅ Reto 12: Archivo de procesos creado")
            
            # ===== RETO 13: Scripting =====
            scripts_dir = self.lab_dir / "scripts"
            scripts_dir.mkdir(exist_ok=True)
            
            # Crear un archivo de referencia para validación
            # ===== RETO 13: Bash scripting =====
            scripts_dir = self.lab_dir / "scripts"
            scripts_dir.mkdir(exist_ok=True)
            (scripts_dir / ".flag.txt").write_text(flag13)
            print("✅ Reto 13: Directorio de scripts preparado")
            
            # ===== RETO 14: Enlaces simbólicos =====
            # La flag se revelará cuando se cree el enlace correctamente
            (self.lab_dir / ".enlace_flag.txt").write_text(f"{flag14}\n¡Excelente! Dominas los enlaces simbólicos.")
            print("✅ Reto 14: Preparado para verificación de enlace")
            
            # ===== RETO 15: Análisis avanzado de logs =====
            accesos_log = logs_dir / "accesos.log"
            contenido_accesos = ("2024-01-15 10:00:00 GET /api/users 192.168.1.100 200\n"
                               "2024-01-15 10:01:00 POST /api/login 10.0.0.50 200\n"
                               "2024-01-15 10:02:00 GET /api/data 192.168.1.100 200\n"
                               "2024-01-15 10:03:00 GET /api/users 172.16.0.1 200\n"
                               "2024-01-15 10:04:00 POST /api/update 192.168.1.100 201\n"
                               "2024-01-15 10:05:00 GET /api/status 10.0.0.50 200\n"
                               "2024-01-15 10:06:00 GET /api/users 192.168.1.100 200\n"
                               "2024-01-15 10:07:00 POST /api/login 172.16.0.1 200\n"
                               "2024-01-15 10:08:00 GET /api/data 10.0.0.50 200\n"
                               "2024-01-15 10:09:00 GET /api/users 172.16.0.1 200\n"
                               "2024-01-15 10:10:00 POST /api/create 192.168.1.100 201\n"
                               f"{flag15}\n"
                               "Las IPs que más aparecen son:\n"
                               "1. 192.168.1.100 (5 veces)\n"
                               "2. 172.16.0.1 (3 veces)\n"
                               "3. 10.0.0.50 (3 veces)\n")
            accesos_log.write_text(contenido_accesos)
            print("✅ Reto 15: Archivo de accesos creado")
            
            print("=" * 60)
            print("✅ ¡Entorno configurado exitosamente!")
            print(f"📁 Directorio del laboratorio: {self.lab_dir}")
            print(f"👤 Código de estudiante: {self.codigo_estudiante}")
            print(f"🎯 Total de retos: {len(self.retos)}")
            print(f"\n🔒 Tus FLAGS son personalizadas y únicas para tu código.")
            print("\n💡 Usa 'python3 linux_challenge.py start' para ver los retos")
            print("💡 Usa 'python3 web_dashboard.py' para abrir el dashboard web")
            
            return True
            
        except Exception as e:
            print(f"❌ Error configurando el entorno: {e}")
            return False

    def load_progress(self) -> Dict:
        """Carga el progreso del usuario desde el archivo JSON"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        return {
            "completados": [],
            "puntos": 0,
            "codigo_estudiante": None
        }
    
    def _cargar_progreso(self) -> Dict:
        """Carga el progreso sin inicializar self.progress (usado en __init__)"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {"codigo_estudiante": None}
    
    def generar_flag_personalizada(self, reto_id: int, texto_base: str) -> str:
        """
        Genera una flag personalizada basada en el código del estudiante.
        
        Args:
            reto_id: ID del reto
            texto_base: Texto descriptivo de la flag
            
        Returns:
            Flag personalizada en formato FLAG{texto_base_HASH}
        """
        if not self.codigo_estudiante:
            return f"FLAG{{{texto_base}}}"
        
        # Crear un hash único combinando código de estudiante + reto_id + texto_base
        datos = f"{self.codigo_estudiante}_{reto_id}_{texto_base}"
        hash_obj = hashlib.sha256(datos.encode())
        hash_corto = hash_obj.hexdigest()[:8].upper()
        
        return f"FLAG{{{texto_base}_{hash_corto}}}"
    
    def solicitar_codigo_estudiante(self) -> str:
        """
        Solicita el código de estudiante al usuario.
        
        Returns:
            Código de estudiante ingresado
        """
        print("\n" + "=" * 70)
        print("🎓 CONFIGURACIÓN PERSONALIZADA".center(70))
        print("=" * 70)
        print("\n📝 Para personalizar tus retos, necesitamos tu código de estudiante.")
        print("   Este código se usará para generar FLAGS únicas para ti.")
        print("   Ejemplo: EST-2024-001, 12345678, TU-CODIGO, etc.\n")
        
        while True:
            codigo = input("👤 Ingresa tu código de estudiante: ").strip()
            
            if len(codigo) < 3:
                print("❌ El código debe tener al menos 3 caracteres. Intenta de nuevo.\n")
                continue
            
            print(f"\n✅ Código registrado: {codigo}")
            confirmacion = input("¿Es correcto? (s/n): ").strip().lower()
            
            if confirmacion in ['s', 'si', 'yes', 'y']:
                return codigo
            else:
                print("\n🔄 Intenta de nuevo...\n")

    def save_progress(self) -> None:
        """Guarda el progreso del usuario en el archivo JSON"""
        self.lab_dir.mkdir(exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)

    def submit_flag(self, flag: str) -> Tuple[bool, str, int]:
        """
        Verifica y registra una flag enviada por el usuario.
        
        Args:
            flag: La flag a verificar
            
        Returns:
            Tupla (éxito, mensaje, id_reto)
        """
        flag = flag.strip()
        
        # Verificar que el estudiante esté registrado
        if not self.codigo_estudiante:
            return False, "❌ Error: No hay código de estudiante registrado. Ejecuta 'setup' primero.", 0
        
        # Mapeo de retos a sus textos base de flags
        flag_bases = {
            1: "encontre_el_oculto",
            2: "leyendo_archivos",
            3: "grep_poderoso",
            4: "permisos_configurados",
            5: "estructura_creada",
            6: "descomprimir_experto",
            7: "regex_master",
            8: "contador_experto",
            9: "find_increible",
            10: "linux_master",
            11: "redireccion_exitosa",
            12: "proceso_encontrado",
            13: "script_maestro",
            14: "enlace_creado",
            15: "analista_experto"
        }
        
        # Buscar qué reto corresponde a la flag
        for reto in self.retos:
            flag_esperada = self.generar_flag_personalizada(reto["id"], flag_bases[reto["id"]])
            
            if flag_esperada == flag:
                reto_id = reto["id"]
                
                # Verificar si ya fue completado
                if reto_id in self.progress["completados"]:
                    return False, f"❌ Este reto ya fue completado anteriormente", reto_id
                
                # Verificación adicional según el reto
                verificacion_exitosa = self._verificar_reto_especifico(reto_id)
                
                if not verificacion_exitosa:
                    return False, f"⚠️ Flag correcta, pero no cumples los requisitos del reto", reto_id
                
                # Registrar completado
                self.progress["completados"].append(reto_id)
                self.progress["puntos"] += reto["puntos"]
                self.progress[f"reto_{reto_id}_fecha"] = datetime.now().isoformat()
                self.save_progress()
                
                mensaje = (
                    "\n🎉 ¡CORRECTO! 🎉\n"
                    f"Reto {reto_id}: {reto['nombre']}\n"
                    f"+{reto['puntos']} puntos\n"
                    f"Total: {self.progress['puntos']} puntos\n"
                    f"Completados: {len(self.progress['completados'])}/{len(self.retos)}\n"
                )
                return True, mensaje, reto_id
        
        return False, "❌ Flag incorrecta. Intenta de nuevo.", 0

    def _verificar_reto_especifico(self, reto_id: int) -> bool:
        """Verificaciones adicionales específicas para cada reto"""
        
        if reto_id == 1:
            return self.verificar_reto1()
        elif reto_id == 2:
            return self.verificar_reto2()
        elif reto_id == 3:
            return self.verificar_reto3()
        elif reto_id == 4:
            return self.verificar_reto4()
        elif reto_id == 5:
            return self.verificar_reto5()
        elif reto_id == 6:
            return self.verificar_reto6()
        elif reto_id == 7:
            return self.verificar_reto7()
        elif reto_id == 8:
            return self.verificar_reto8()
        elif reto_id == 9:
            return self.verificar_reto9()
        elif reto_id == 10:
            return self.verificar_reto10()
        elif reto_id == 11:
            return self.verificar_reto11()
        elif reto_id == 12:
            return self.verificar_reto12()
        elif reto_id == 13:
            return self.verificar_reto13()
        elif reto_id == 14:
            return self.verificar_reto14()
        elif reto_id == 15:
            return self.verificar_reto15()
        
        return True

    def verificar_reto1(self) -> bool:
        """Verifica que el archivo oculto existe"""
        archivo = self.lab_dir / "secretos" / ".archivo_oculto.txt"
        return archivo.exists()

    def verificar_reto2(self) -> bool:
        """Verifica que el archivo de logs existe"""
        archivo = self.lab_dir / "logs" / "sistema.log"
        return archivo.exists()

    def verificar_reto3(self) -> bool:
        """Verifica que los archivos de datos existen"""
        archivo = self.lab_dir / "datos" / "archivo3.txt"
        return archivo.exists()

    def verificar_reto4(self) -> bool:
        """Verifica que los permisos del archivo son 600"""
        archivo = self.lab_dir / "config" / "sistema.conf"
        if not archivo.exists():
            return False
        
        permisos = oct(os.stat(archivo).st_mode)[-3:]
        return permisos == "600"

    def verificar_reto5(self) -> bool:
        """Verifica que la estructura de directorios fue creada"""
        ruta = self.lab_dir / "proyecto" / "src" / "main" / "java" / "com" / "app"
        return ruta.exists() and ruta.is_dir()

    def verificar_reto6(self) -> bool:
        """Verifica que el archivo fue descomprimido"""
        archivo = self.lab_dir / "archivos" / "secreto" / "flag.txt"
        return archivo.exists()

    def verificar_reto7(self) -> bool:
        """Verifica que el archivo de conexiones existe"""
        archivo = self.lab_dir / "logs" / "conexiones.log"
        return archivo.exists()

    def verificar_reto8(self) -> bool:
        """Verifica que el archivo de errores existe"""
        archivo = self.lab_dir / "logs" / "errores.log"
        return archivo.exists()

    def verificar_reto9(self) -> bool:
        """Verifica que el archivo reciente existe"""
        archivo = self.lab_dir / "datos" / "reciente.txt"
        return archivo.exists()

    def verificar_reto10(self) -> bool:
        """Verifica que el archivo hash existe"""
        datos_hash = f"{self.codigo_estudiante}_linux_master"
        md5_hash = hashlib.md5(datos_hash.encode()).hexdigest()
        archivo = self.lab_dir / "sistema" / "var" / "cache" / md5_hash
        return archivo.exists()

    def verificar_reto11(self) -> bool:
        """Verifica que se creó el archivo con redirección"""
        archivo = self.lab_dir / "output" / "resultado.txt"
        if not archivo.exists():
            return False
        # Verificar que contiene líneas con SUCCESS
        contenido = archivo.read_text()
        return "SUCCESS" in contenido and "ERROR" not in contenido

    def verificar_reto12(self) -> bool:
        """Verifica que se leyó el archivo de procesos"""
        archivo = self.lab_dir / "procesos" / "puertos.txt"
        return archivo.exists()

    def verificar_reto13(self) -> bool:
        """Verifica que se creó el script"""
        script = self.lab_dir / "scripts" / "contador.sh"
        if not script.exists():
            return False
        # Verificar que sea ejecutable
        return os.access(script, os.X_OK)

    def verificar_reto14(self) -> bool:
        """Verifica que se creó el enlace simbólico"""
        enlace = self.lab_dir / "acceso_rapido"
        if not enlace.exists():
            return False
        # Verificar que es un enlace simbólico
        return enlace.is_symlink()

    def verificar_reto15(self) -> bool:
        """Verifica que el archivo de accesos existe"""
        archivo = self.lab_dir / "logs" / "accesos.log"
        return archivo.exists()

    def mostrar_retos(self) -> None:
        """Muestra todos los retos disponibles en la CLI"""
        print("\n" + "=" * 70)
        print("🎯 LINUX CHALLENGE LAB - RETOS CTF".center(70))
        print("=" * 70)
        
        completados = self.progress["completados"]
        puntos_totales = self.progress["puntos"]
        total_puntos_posibles = sum(r["puntos"] for r in self.retos)
        
        if self.codigo_estudiante:
            print(f"\n👤 Estudiante: {self.codigo_estudiante}")
            print(f"🔒 Tus FLAGS son personalizadas y únicas")
        
        print(f"\n📊 Progreso: {len(completados)}/{len(self.retos)} retos completados")
        print(f"⭐ Puntos: {puntos_totales}/{total_puntos_posibles}")
        print(f"📈 Porcentaje: {(len(completados)/len(self.retos))*100:.0f}%")
        print("\n" + "-" * 70)
        
        for reto in self.retos:
            estado = "✅" if reto["id"] in completados else "⬜"
            print(f"\n{estado} RETO {reto['id']}: {reto['nombre']}")
            print(f"   📝 {reto['descripcion']}")
            print(f"   🏆 Puntos: {reto['puntos']} | 📊 Dificultad: {reto['dificultad']} | 📁 Categoría: {reto['categoria']}")
            
            if reto["id"] in completados:
                fecha = self.progress.get(f"reto_{reto['id']}_fecha", "")
                if fecha:
                    print(f"   ✅ Completado: {fecha}")
        
        print("\n" + "=" * 70)
        print("\n💡 Comandos disponibles:")
        print("   python3 linux_challenge.py hint <numero>  - Ver pista de un reto")
        print("   python3 linux_challenge.py submit <flag>  - Enviar una flag")
        print("   python3 linux_challenge.py status         - Ver tu progreso")
        print("   python3 web_dashboard.py                   - Abrir dashboard web")
        print("=" * 70 + "\n")

    def mostrar_hint(self, reto_id: int) -> None:
        """Muestra la pista de un reto específico"""
        reto = next((r for r in self.retos if r["id"] == reto_id), None)
        
        if not reto:
            print(f"❌ Reto {reto_id} no encontrado")
            return
        
        print("\n" + "=" * 70)
        print(f"💡 PISTA - RETO {reto_id}: {reto['nombre']}")
        print("=" * 70)
        print(f"\n{reto['pista']}\n")
        print("=" * 70 + "\n")

    def mostrar_status(self) -> None:
        """Muestra el estado actual del progreso"""
        completados = self.progress["completados"]
        puntos = self.progress["puntos"]
        total_puntos_posibles = sum(r["puntos"] for r in self.retos)
        
        print("\n" + "=" * 70)
        print("📊 TU PROGRESO".center(70))
        print("=" * 70)
        print(f"\n✅ Retos completados: {len(completados)}/{len(self.retos)}")
        print(f"⭐ Puntos totales: {puntos}/{total_puntos_posibles}")
        print(f"📈 Porcentaje: {(len(completados)/len(self.retos))*100:.0f}%")
        
        if completados:
            print(f"\n🎯 Retos completados: {', '.join(map(str, sorted(completados)))}")
            
            # Calcular estadísticas
            retos_completados = [r for r in self.retos if r["id"] in completados]
            if retos_completados:
                print("\n📅 Últimas completaciones:")
                for reto in sorted(retos_completados, key=lambda x: self.progress.get(f"reto_{x['id']}_fecha", ""), reverse=True)[:3]:
                    fecha = self.progress.get(f"reto_{reto['id']}_fecha", "")
                    if fecha:
                        print(f"   • Reto {reto['id']}: {reto['nombre']} - {fecha}")
        
        pendientes = [r for r in self.retos if r["id"] not in completados]
        if pendientes:
            print(f"\n⏳ Retos pendientes: {len(pendientes)}")
            print(f"   Próximo reto sugerido: Reto {pendientes[0]['id']} - {pendientes[0]['nombre']}")
        else:
            print("\n🏆 ¡FELICIDADES! Has completado todos los retos")
            print("   Eres un verdadero maestro de Linux 🎉")
        
        print("\n" + "=" * 70 + "\n")


def main():
    """Función principal del CLI"""
    challenge = LinuxChallenge()
    
    if len(sys.argv) < 2:
        mensaje_ayuda = (
            "\n🎯 Linux Challenge Lab - Sistema de Retos CTF\n\n"
            "Uso:\n"
            "    python3 linux_challenge.py setup              - Configurar entorno\n"
            "    python3 linux_challenge.py start              - Ver todos los retos\n"
            "    python3 linux_challenge.py submit <flag>      - Enviar una flag\n"
            "    python3 linux_challenge.py status             - Ver tu progreso\n"
            "    python3 linux_challenge.py hint <numero>      - Ver pista de un reto\n\n"
            "Ejemplos:\n"
            "    python3 linux_challenge.py submit FLAG{ejemplo}\n"
            "    python3 linux_challenge.py hint 1\n"
        )
        print(mensaje_ayuda)
        sys.exit(1)
    
    comando = sys.argv[1].lower()
    
    if comando == "setup":
        challenge.setup_environment()
    
    elif comando == "start":
        challenge.mostrar_retos()
    
    elif comando == "submit":
        if len(sys.argv) < 3:
            print("❌ Debes proporcionar una flag")
            print("Uso: python3 linux_challenge.py submit FLAG{...}")
            sys.exit(1)
        
        flag = sys.argv[2]
        exito, mensaje, reto_id = challenge.submit_flag(flag)
        print(mensaje)
        
        if exito and len(challenge.progress["completados"]) == 10:
            print("\n" + "=" * 70)
            print("🏆 ¡FELICIDADES! 🏆".center(70))
            print("=" * 70)
            print("\n   Has completado todos los retos del Linux Challenge Lab")
            print(f"   Puntuación final: {challenge.progress['puntos']}/175 puntos")
            print("\n   ¡Eres un verdadero maestro de Linux! 🎉\n")
            print("=" * 70 + "\n")
    
    elif comando == "status":
        challenge.mostrar_status()
    
    elif comando == "hint":
        if len(sys.argv) < 3:
            print("❌ Debes proporcionar el número del reto")
            print("Uso: python3 linux_challenge.py hint <numero>")
            sys.exit(1)
        
        try:
            reto_id = int(sys.argv[2])
            challenge.mostrar_hint(reto_id)
        except ValueError:
            print("❌ El número de reto debe ser un entero")
            sys.exit(1)
    
    else:
        print(f"❌ Comando desconocido: {comando}")
        print("Usa 'python3 linux_challenge.py' sin argumentos para ver la ayuda")
        sys.exit(1)


if __name__ == "__main__":
    main()
