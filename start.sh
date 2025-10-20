#!/bin/bash
# Script de inicio interactivo para Linux Challenge Lab

# Colores
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Banner
clear
echo -e "${GREEN}"
echo "======================================================================"
echo "   🎯 LINUX CHALLENGE LAB - Sistema de Retos CTF"
echo "======================================================================"
echo -e "${NC}"

# Verificar Python
echo -e "${CYAN}[1/3] Verificando Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 no está instalado${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python $(python3 --version) encontrado${NC}"

# Verificar dependencias
echo -e "\n${CYAN}[2/3] Verificando dependencias...${NC}"
if ! python3 -c "import flask" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  Flask no está instalado. Instalando...${NC}"
    pip install -q flask
    echo -e "${GREEN}✅ Flask instalado correctamente${NC}"
else
    echo -e "${GREEN}✅ Flask ya está instalado${NC}"
fi

# Verificar si el entorno está configurado
echo -e "\n${CYAN}[3/3] Verificando entorno...${NC}"
if [ ! -d "$HOME/linux_lab" ]; then
    echo -e "${YELLOW}⚠️  El entorno no está configurado${NC}"
    echo -e "${YELLOW}Configurando entorno...${NC}"
    python3 linux_challenge.py setup
else
    echo -e "${GREEN}✅ Entorno ya configurado${NC}"
fi

# Menú principal
while true; do
    echo -e "\n${GREEN}======================================================================"
    echo "   📋 MENÚ PRINCIPAL"
    echo "======================================================================${NC}"
    echo ""
    echo "  1) 🌐 Iniciar Dashboard Web (Recomendado)"
    echo "  2) ⌨️  Usar Línea de Comandos (CLI)"
    echo "  3) 📖 Ver README"
    echo "  4) 📊 Ver Estado del Sistema"
    echo "  5) 🔄 Reconfigurar Entorno"
    echo "  6) ❌ Salir"
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    read -p "$(echo -e ${YELLOW}Selecciona una opción [1-6]: ${NC})" opcion

    case $opcion in
        1)
            echo -e "\n${GREEN}🚀 Iniciando Dashboard Web...${NC}"
            echo -e "${CYAN}El dashboard estará disponible en:${NC}"
            echo -e "   ${YELLOW}→ http://localhost:5000${NC}"
            echo -e "   ${YELLOW}→ http://127.0.0.1:5000${NC}"
            echo -e "\n${CYAN}Presiona CTRL+C para detener el servidor${NC}\n"
            sleep 2
            python3 web_dashboard.py
            ;;
        2)
            echo -e "\n${GREEN}⌨️  Modo Línea de Comandos${NC}"
            echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo -e "\n${YELLOW}Comandos disponibles:${NC}"
            echo "  • python3 linux_challenge.py start              - Ver todos los retos"
            echo "  • python3 linux_challenge.py submit FLAG{...}   - Enviar una flag"
            echo "  • python3 linux_challenge.py status             - Ver tu progreso"
            echo "  • python3 linux_challenge.py hint <numero>      - Ver pista de un reto"
            echo -e "\n${CYAN}Presiona Enter para continuar...${NC}"
            read
            python3 linux_challenge.py start
            echo -e "\n${CYAN}Presiona Enter para volver al menú...${NC}"
            read
            ;;
        3)
            echo -e "\n${GREEN}📖 Abriendo README...${NC}"
            if [ -f "README.md" ]; then
                less README.md
            else
                echo -e "${RED}❌ README.md no encontrado${NC}"
            fi
            ;;
        4)
            echo -e "\n${GREEN}📊 Estado del Sistema${NC}"
            echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            python3 verify_system.py
            echo -e "\n${CYAN}Presiona Enter para continuar...${NC}"
            read
            ;;
        5)
            echo -e "\n${YELLOW}🔄 Reconfigurando entorno...${NC}"
            read -p "$(echo -e ${RED}¿Estás seguro? Esto eliminará el progreso actual [s/N]: ${NC})" confirmar
            if [[ $confirmar == "s" || $confirmar == "S" ]]; then
                rm -rf "$HOME/linux_lab"
                python3 linux_challenge.py setup
                echo -e "${GREEN}✅ Entorno reconfigurado${NC}"
            else
                echo -e "${YELLOW}❌ Operación cancelada${NC}"
            fi
            echo -e "\n${CYAN}Presiona Enter para continuar...${NC}"
            read
            ;;
        6)
            echo -e "\n${GREEN}👋 ¡Hasta luego!${NC}"
            echo -e "${YELLOW}Sigue practicando comandos de Linux 🚀${NC}\n"
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Opción inválida. Por favor selecciona 1-6${NC}"
            sleep 2
            ;;
    esac
done
