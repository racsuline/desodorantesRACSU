# Configura tu clave de Gemini API
GENAI_API_KEY = "TU_API_GEMINI_KEY"
if not GENAI_API_KEY:
    print("Error: GENAI_API_KEY no encontrada")
    exit()

# Importa la librería genai en lugar de google.generativeai
import genai
from colorama import init, Fore, Style
import questionary

# Inicializa colorama
init(autoreset=True)

# Configura la API key
genai.configure(api_key=GENAI_API_KEY)

# Función para obtener recomendaciones de desodorantes
def get_deodorant_recommendations(intensity, odor_type, ph_level, age, activity_level, fragrance_pref, skin_sensitivity, format_pref, brand_pref):
    # Selecciona el modelo Gemini adecuado
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    prompt = f"""
Eres un experto en formulación de desodorantes y ciencia olfativa, especializado en el mercado Chileno.
Basándote en el perfil corporal y preferencias del usuario, recomienda entre 3 a 5 desodorantes que se vendan actualmente en farmacias y supermercados en Chile.
Destaca el mejor desodorante para cada perfil y justifica tu elección.
Solo puedes considerar marcas como: Nivea, Rexona, Dove, Adidas, Old Spice, Axe. Si hay otras que esten en el mercado Chileno pero que no sean mencionadas aqui, incluyelas en tus recomendaciones.
Datos del usuario:
- Intensidad del olor corporal: {intensity}
- Tipo de olor corporal: {odor_type}
- Valor de pH: {ph_level}
- Edad: {age} años
- Nivel de actividad física: {activity_level}
- Preferencia de fragancia: {fragrance_pref}
- Sensibilidad de piel: {skin_sensitivity}
- Formato preferido: {format_pref}
- Preferencia de marca: {brand_pref}
Entrega las recomendaciones en este formato para la terminal:
==========================================
Desodorante: <Nombre del producto>
Descripción: <Justificación clara y resumida de por qué lo recomiendas para ese perfil>
==========================================
Sin listas, sin JSON, solo texto plano.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al obtener recomendaciones: {e}"

# Encabezado divertido
def print_header():
    print(Fore.CYAN + Style.BRIGHT + "\n==============================================")
    print(Fore.CYAN + Style.BRIGHT + "RECOMENDADOR DE DESODORANTES PARA INFORMÁTICOS")
    print(Fore.CYAN + Style.BRIGHT + "==============================================\n")
    print(Fore.LIGHTBLACK_EX + "Porque incluso los bugs huyen de un buen desodorante. 🐞➡️💨")
    print(Fore.LIGHTBLACK_EX + "¡No dejes que tu código huela peor que tu lógica! 😅")

# Lógica principal
def main():
    print_header()
    intensity = questionary.select(
        "👉 Intensidad de tu olor corporal:",
        choices=["Leve", "Moderado", "Fuerte"],
        instruction="Usa las flechas ↑ ↓ y Enter"
    ).ask().lower()
    odor_type = questionary.select(
        "👉 Tipo de olor corporal:",
        choices=["Especiado", "Almizclado", "Floral"],
        instruction="Usa las flechas ↑ ↓ y Enter"
    ).ask().lower()

    while True:
        try:
            ph_level = float(input("👉 Valor de pH (0 a 14): "))
            if 0 <= ph_level <= 14:
                break
            else:
                print(Fore.RED + "⚠️  Debe estar entre 0 y 14.")
        except ValueError:
            print(Fore.RED + "⚠️  Ingresa un número válido.")

    while True:
        try:
            age = int(input("👉 Edad: "))
            if 0 < age < 120:
                break
            else:
                print(Fore.RED + "⚠️  Ingresa una edad válida.")
        except ValueError:
            print(Fore.RED + "⚠️  Solo se aceptan números enteros.")

    activity_level = questionary.select(
        "👉 Nivel de actividad física:",
        choices=["Bajo", "Medio", "Alto"],
        instruction="Usa las flechas ↑ ↓ y Enter"
    ).ask().lower()
    fragrance_pref = questionary.select(
        "👉 Preferencia de fragancia:",
        choices=["Cítrico", "Fresco", "Floral", "Sin fragancia"],
        instruction="Usa las flechas ↑ ↓ y Enter"
    ).ask().lower()
    skin_sensitivity = questionary.select(
        "👉 Sensibilidad de tu piel:",
        choices=["Normal", "Sensible", "Muy sensible"],
        instruction="Usa las flechas ↑ ↓ y Enter"
    ).ask().lower()
    format_pref = questionary.select(
        "👉 Formato preferido de desodorante:",
        choices=["Spray", "Barra", "Roll-on", "Sin preferencia"],
        instruction="Usa las flechas ↑ ↓ y Enter"
    ).ask().lower()
    brand_pref = questionary.select(
        "👉 Preferencia de marca:",
        choices=["Nivea", "Rexona", "Dove", "Adidas", "Old Spice", "Axe", "Sin preferencia"],
        instruction="Usa las flechas ↑ ↓ y Enter"
    ).ask().lower()

    print(Fore.YELLOW + "\nProcesando tus datos... 🖥️\n")
    recommendations = get_deodorant_recommendations(
        intensity, odor_type, ph_level, age, activity_level,
        fragrance_pref, skin_sensitivity, format_pref, brand_pref
    )

    print(Fore.GREEN + "===== TUS RECOMENDACIONES =====\n")
    print(recommendations)
    print(Fore.CYAN + "\nGracias por usar el recomendador. ¡Que tu código y tú siempre huelan bien! 🧼")

if __name__ == "__main__":
    main()
