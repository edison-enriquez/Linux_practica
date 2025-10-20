#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificación del sistema Linux Challenge Lab
Verifica que todos los componentes estén correctamente instalados
"""

import os
import sys
from pathlib import Path

def print_header(text):
    """Imprime un encabezado formateado"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def check_python():
    """Verifica la versión de Python"""
    print("\n🐍 Verificando Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Se requiere Python 3.8 o superior (tienes {version.major}.{version.minor})")
        return False

def check_dependencies():
    """Verifica las dependencias instaladas"""
    print("\n📦 Verificando dependencias...")
    dependencies = {
        'flask': 'Flask',
        'werkzeug': 'Werkzeug'
    }
    
    all_installed = True
    for module, name in dependencies.items():
        try:
            __import__(module)
            print(f"   ✅ {name}")
        except ImportError:
            print(f"   ❌ {name} no está instalado")
            all_installed = False
    
    return all_installed

def check_files():
    """Verifica que existan los archivos necesarios"""
    print("\n📄 Verificando archivos del sistema...")
    required_files = {
        'linux_challenge.py': 'Sistema principal de retos',
        'web_dashboard.py': 'Servidor web',
        'templates/index.html': 'Dashboard HTML',
        'requirements.txt': 'Dependencias',
        'start.sh': 'Script de inicio'
    }
    
    all_exist = True
    for file, description in required_files.items():
        path = Path(file)
        if path.exists():
            size = path.stat().st_size
            print(f"   ✅ {file} ({size} bytes) - {description}")
        else:
            print(f"   ❌ {file} - {description}")
            all_exist = False
    
    return all_exist

def check_environment():
    """Verifica el entorno del laboratorio"""
    print("\n🔧 Verificando entorno del laboratorio...")
    lab_dir = Path.home() / "linux_lab"
    
    if not lab_dir.exists():
        print(f"   ❌ Directorio del laboratorio no existe: {lab_dir}")
        print(f"   💡 Ejecuta: python3 linux_challenge.py setup")
        return False
    
    print(f"   ✅ Directorio del laboratorio: {lab_dir}")
    
    # Verificar subdirectorios
    subdirs = ['secretos', 'logs', 'datos', 'config', 'archivos', 'sistema']
    missing = []
    
    for subdir in subdirs:
        path = lab_dir / subdir
        if path.exists():
            print(f"   ✅ {subdir}/")
        else:
            print(f"   ⚠️  {subdir}/ (falta)")
            missing.append(subdir)
    
    # Verificar archivo de progreso
    progress_file = lab_dir / ".progress.json"
    if progress_file.exists():
        import json
        try:
            with open(progress_file, 'r') as f:
                progress = json.load(f)
            completados = len(progress.get('completados', []))
            puntos = progress.get('puntos', 0)
            print(f"\n   📊 Progreso actual:")
            print(f"      • Retos completados: {completados}/10")
            print(f"      • Puntos: {puntos}/175")
        except:
            print(f"   ⚠️  Archivo de progreso corrupto")
    else:
        print(f"\n   ℹ️  No hay progreso guardado aún")
    
    if missing:
        print(f"\n   ⚠️  Algunos directorios faltan. Considera reconfigurar:")
        print(f"   💡 Ejecuta: python3 linux_challenge.py setup")
        return False
    
    return True

def check_permissions():
    """Verifica permisos de archivos ejecutables"""
    print("\n🔐 Verificando permisos...")
    executable_files = ['start.sh', 'verify_system.py']
    
    all_ok = True
    for file in executable_files:
        path = Path(file)
        if path.exists():
            is_executable = os.access(path, os.X_OK)
            if is_executable:
                print(f"   ✅ {file} (ejecutable)")
            else:
                print(f"   ⚠️  {file} (no ejecutable)")
                print(f"      Ejecuta: chmod +x {file}")
                all_ok = False
        else:
            print(f"   ❌ {file} (no existe)")
            all_ok = False
    
    return all_ok

def check_ports():
    """Verifica disponibilidad del puerto"""
    print("\n🌐 Verificando disponibilidad de puertos...")
    import socket
    
    port = 5000
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        
        if result == 0:
            print(f"   ⚠️  Puerto {port} está en uso")
            print(f"      El dashboard web podría tener problemas para iniciar")
            return False
        else:
            print(f"   ✅ Puerto {port} disponible")
            return True
    except:
        print(f"   ⚠️  No se pudo verificar el puerto {port}")
        return False

def print_summary(results):
    """Imprime un resumen de los resultados"""
    print_header("📋 RESUMEN DE VERIFICACIÓN")
    
    total = len(results)
    passed = sum(1 for r in results.values() if r)
    
    print(f"\n   Verificaciones completadas: {passed}/{total}")
    print(f"   Estado: ", end="")
    
    if passed == total:
        print("✅ SISTEMA COMPLETAMENTE FUNCIONAL")
        print("\n   🚀 Todo está listo para usar Linux Challenge Lab")
        print("\n   💡 Para comenzar:")
        print("      • Ejecuta: ./start.sh")
        print("      • O ejecuta: python3 web_dashboard.py")
    elif passed >= total * 0.7:
        print("⚠️  SISTEMA PARCIALMENTE FUNCIONAL")
        print("\n   ⚠️  Algunos componentes necesitan atención")
        print("   💡 Revisa los errores arriba y corrígelos")
    else:
        print("❌ SISTEMA NO FUNCIONAL")
        print("\n   ❌ Varios componentes faltan o tienen errores")
        print("   💡 Ejecuta: python3 linux_challenge.py setup")
    
    print("\n" + "=" * 70 + "\n")

def main():
    """Función principal"""
    print_header("🔍 VERIFICACIÓN DEL SISTEMA - Linux Challenge Lab")
    
    results = {
        'Python': check_python(),
        'Dependencias': check_dependencies(),
        'Archivos': check_files(),
        'Entorno': check_environment(),
        'Permisos': check_permissions(),
        'Puertos': check_ports()
    }
    
    print_summary(results)
    
    # Código de salida
    if all(results.values()):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
