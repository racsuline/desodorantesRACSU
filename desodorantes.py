    # Set your Gemini API key
GOOGLE_GENAI_API_KEY = "TU_API"

if not GOOGLE_GENAI_API_KEY:
    print("Error: GOOGLE_GENAI_API_KEY no encontrada")
    exit()

import google.generativeai as genai
from colorama import init, Fore, Style

init(autoreset=True)

genai.configure(api_key=GOOGLE_GENAI_API_KEY)

def get_deodorant_recommendations(intensity, odor_type, ph_level, age, activity_level, fragrance_pref):
    """
    Recommends deodorant brands based on the user's odor profile using the Gemini API.
    """
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    prompt = f"""
Eres un experto en formulación de desodorantes y ciencia olfativa, especializado en el mercado Chileno.
Basándote en el perfil corporal del usuario, recomienda 3 a 5 desodorantes que se vendan actualmente en farmacias y supermercados en Chile.

Solo puedes considerar marcas como: Nivea, Rexona, Dove, Adidas, Old Spice, Axe.

Datos del usuario:
- Intensidad del Olor: {intensity}
- Tipo de Olor: {odor_type}
- Valor de pH: {ph_level}
- Edad: {age} años
- Nivel de actividad física: {activity_level}
- Preferencia de fragancia: {fragrance_pref}

Entrega las recomendaciones en este formato para la terminal:

Desodorante: <Nombre del producto>

Descripción: <Breve justificación de por qué lo recomiendas para ese perfil>

Separado por líneas divisorias como "------------------------------"

Sin JSON, sin listas, solo texto plano formateado.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al obtener recomendaciones: {e}"

def print_header():
    print(Fore.CYAN + Style.BRIGHT + "\n=============================================")
    print(Fore.CYAN + Style.BRIGHT + "  RECOMENDADOR DE DESODORANTES CHILE v2.0")
    print(Fore.CYAN + Style.BRIGHT + "=============================================\n")

def main():
    """
    Main function to gather user input and display deodorant recommendations.
    """
    print_header()

    intensity = input("👉 Intensidad de tu olor corporal (leve, moderado, fuerte): ").lower()
    odor_type = input("👉 Tipo de olor corporal (especiado, almizclado, floral): ").lower()

    while True:
        try:
            ph_level = float(input("👉 Valor de pH (0 a 14): "))
            if 0 <= ph_level <= 14:
                break
            else:
                print(Fore.RED + "⚠️  El valor de pH debe estar entre 0 y 14.")
        except ValueError:
            print(Fore.RED + "⚠️  Por favor, ingresa un número válido para el pH.")

    while True:
        try:
            age = int(input("👉 Edad: "))
            if 0 < age < 120:
                break
            else:
                print(Fore.RED + "⚠️  Ingresa una edad válida.")
        except ValueError:
            print(Fore.RED + "⚠️  Por favor, ingresa un número entero para la edad.")

    activity_level = input("👉 Nivel de actividad física (bajo, medio, alto): ").lower()
    fragrance_pref = input("👉 Preferencia de fragancia (cítrico, fresco, floral, sin fragancia): ").lower()

    print(Fore.YELLOW + "\nObteniendo recomendaciones...\n")

    recommendations = get_deodorant_recommendations(
        intensity, odor_type, ph_level, age, activity_level, fragrance_pref
    )

    print(Fore.GREEN + "===== TUS RECOMENDACIONES =====\n")
    print(recommendations)
    print(Fore.CYAN + "\nGracias por usar el recomendador 👃✨")

if __name__ == "__main__":
    main()