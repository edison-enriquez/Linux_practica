#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux Challenge Lab - Dashboard Web
Servidor Flask que proporciona una interfaz web para el sistema de retos
"""

from flask import Flask, render_template, jsonify, request
from linux_challenge import LinuxChallenge
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'linux-challenge-lab-secret-key-2024'

# Instancia global del sistema de retos
challenge = LinuxChallenge()


@app.route('/')
def index():
    """Página principal del dashboard"""
    return render_template('index.html')


@app.route('/api/progress', methods=['GET'])
def get_progress():
    """
    Endpoint para obtener el progreso actual del usuario
    
    Returns:
        JSON con retos, progreso y estadísticas
    """
    completados = challenge.progress.get("completados", [])
    puntos = challenge.progress.get("puntos", 0)
    
    # Preparar datos de los retos
    retos_data = []
    for reto in challenge.retos:
        reto_info = {
            "id": reto["id"],
            "nombre": reto["nombre"],
            "descripcion": reto["descripcion"],
            "puntos": reto["puntos"],
            "dificultad": reto["dificultad"],
            "categoria": reto["categoria"],
            "completado": reto["id"] in completados,
            "fecha": challenge.progress.get(f"reto_{reto['id']}_fecha", None)
        }
        retos_data.append(reto_info)
    
    return jsonify({
        "retos": retos_data,
        "completados": completados,
        "puntos": puntos,
        "total_retos": len(challenge.retos),
        "puntos_maximos": sum(r["puntos"] for r in challenge.retos),
        "porcentaje": (len(completados) / len(challenge.retos)) * 100 if challenge.retos else 0
    })


@app.route('/api/submit', methods=['POST'])
def submit_flag():
    """
    Endpoint para enviar una flag
    
    Body JSON:
        {
            "flag": "FLAG{...}"
        }
    
    Returns:
        JSON con resultado de la validación
    """
    data = request.get_json()
    
    if not data or 'flag' not in data:
        return jsonify({
            "success": False,
            "message": "❌ Debes proporcionar una flag"
        }), 400
    
    flag = data['flag']
    exito, mensaje, reto_id = challenge.submit_flag(flag)
    
    response = {
        "success": exito,
        "message": mensaje,
        "reto_id": reto_id if exito else None,
        "puntos_totales": challenge.progress.get("puntos", 0),
        "completados": len(challenge.progress.get("completados", [])),
        "total_retos": len(challenge.retos)
    }
    
    # Verificar si completó todos los retos
    if exito and len(challenge.progress.get("completados", [])) == len(challenge.retos):
        response["all_completed"] = True
    
    return jsonify(response)


@app.route('/api/hint/<int:reto_id>', methods=['GET'])
def get_hint(reto_id):
    """
    Endpoint para obtener la pista de un reto
    
    Args:
        reto_id: ID del reto
    
    Returns:
        JSON con la pista del reto
    """
    reto = next((r for r in challenge.retos if r["id"] == reto_id), None)
    
    if not reto:
        return jsonify({
            "success": False,
            "message": f"❌ Reto {reto_id} no encontrado"
        }), 404
    
    return jsonify({
        "success": True,
        "reto_id": reto_id,
        "nombre": reto["nombre"],
        "pista": reto["pista"]
    })


@app.route('/api/reset', methods=['POST'])
def reset_progress():
    """
    Endpoint para reiniciar el progreso (solo desarrollo)
    
    Returns:
        JSON con confirmación
    """
    challenge.progress = {
        "completados": [],
        "puntos": 0
    }
    challenge.save_progress()
    
    return jsonify({
        "success": True,
        "message": "✅ Progreso reiniciado correctamente"
    })


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """
    Endpoint para obtener estadísticas detalladas
    
    Returns:
        JSON con estadísticas del progreso
    """
    completados = challenge.progress.get("completados", [])
    puntos = challenge.progress.get("puntos", 0)
    
    # Contar por dificultad
    stats_dificultad = {
        "Principiante": 0,
        "Intermedio": 0,
        "Avanzado": 0,
        "Experto": 0
    }
    
    # Contar por categoría
    stats_categoria = {}
    
    for reto in challenge.retos:
        if reto["id"] in completados:
            stats_dificultad[reto["dificultad"]] += 1
            
            if reto["categoria"] not in stats_categoria:
                stats_categoria[reto["categoria"]] = 0
            stats_categoria[reto["categoria"]] += 1
    
    return jsonify({
        "total_completados": len(completados),
        "total_retos": len(challenge.retos),
        "puntos": puntos,
        "puntos_maximos": sum(r["puntos"] for r in challenge.retos),
        "por_dificultad": stats_dificultad,
        "por_categoria": stats_categoria
    })


def main():
    """Inicia el servidor Flask"""
    print("=" * 70)
    print("🚀 Iniciando Linux Challenge Lab Dashboard")
    print("=" * 70)
    print("\n📊 Dashboard disponible en: http://localhost:5000")
    print("📊 Dashboard disponible en: http://127.0.0.1:5000")
    print("\n💡 Presiona CTRL+C para detener el servidor\n")
    print("=" * 70 + "\n")
    
    # Verificar si el entorno está configurado
    if not challenge.lab_dir.exists():
        print("⚠️  ADVERTENCIA: El entorno no está configurado")
        print("   Ejecuta: python3 linux_challenge.py setup\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    main()
