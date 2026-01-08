#Importar las librerías necesarias
from newspaper import Article
from gtts import gTTS
import os

def limpiar_pantalla() -> None:
    os.system("clear" if os.name != "nt" else "cls")

def mostrar_banner() -> None:
    print("=" * 60)
    print("          CONVERSOR DE ARTÍCULOS WEB A AUDIO (MP3)")
    print("=" * 60)
    print("   Ingresa la URL de una noticia o artículo en la web.")
    print('   Escribe "S" y presiona Enter para salir.')
    print("-" * 60)

def obtener_texto_articulo(url: str) -> tuple[str | None, str | None]:
    """Según URL, descarga y devuelve el título y el texto del artículo."""
    try:
        article = Article(url)
        article.download()
        article.parse()

        texto = article.text.strip()
        titulo = (article.title or "").strip()

        if not texto or len(texto) < 50:
            print("\n[!] No se pudo obtener un texto suficiente del artículo.\n")
            return None, None

        return titulo, texto
    except Exception as e:
        print(f"\n[!] Error al procesar la URL: {e}\n")
        return None, None

def texto_a_mp3(texto: str, nombre_archivo: str, idioma: str = "es") -> None:
    """Convierte texto a voz y guarda un archivo mp3."""
    tts = gTTS(text=texto, lang=idioma)
    tts.save(nombre_archivo)

def construir_nombre_archivo(titulo: str | None = None) -> str:
    """ Construye un nombre de archivo mp3 sencillo a partir del título, limitado a 10 caracteres, o usa un nombre por defecto. """
    if titulo:
        nombre = "".join(c for c in titulo if c.isalnum() or c in (" ", "_", "-"))
        nombre = nombre.strip().replace(" ", "_")
        if not nombre:
            nombre = "articulo"
    else:
        nombre = "articulo"

    # limitar a 10 caracteres
    nombre = nombre[:10]
    return f"{nombre}.mp3"

def main() -> None:
    while True:
        limpiar_pantalla()
        mostrar_banner()

        url = input("URL del artículo (o 'S' para salir): ").strip()

        if not url:
            print("\n[!] La URL no puede estar vacía. Intenta nuevamente.\n")
            input("Presiona Enter para continuar...")
            continue

        if url.upper() == "S":
            print("\nGracias por usar el conversor. ¡Hasta luego!\n")
            break

        print("\nDescargando artículo, por favor espera...\n")
        titulo, texto = obtener_texto_articulo(url)

        if not texto:
            print("Intenta con otra URL o escribe 'S' para salir.\n")
            input("Presiona Enter para continuar...")
            continue

        nombre_archivo = construir_nombre_archivo(titulo)
        ruta_salida = os.path.join(os.getcwd(), nombre_archivo)

        print("Convirtiendo texto a audio...\n")
        try:
            texto_a_mp3(texto, ruta_salida, idioma="es")
            print("=" * 60)
            print(" Conversión completada con éxito.")
            if titulo:
                print(f" Título: {titulo}")
            print(f" Archivo generado: {ruta_salida}")
            print("=" * 60)
        except Exception as e:
            print(f"\n[!] Ocurrió un error al generar el audio: {e}\n")

        print()
        opcion = input("¿Quieres convertir otro artículo? (S/N): ").strip().upper()
        if opcion != "S":
            print("\nGracias por usar el conversor. ¡Hasta luego!\n")
            break

# Ejecución del script
if __name__ == "__main__":
    main()
