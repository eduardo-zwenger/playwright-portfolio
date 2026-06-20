from playwright.sync_api import Page, expect

def test_cargar_pagina(page: Page):
    # 1. Entramos a una página de prácticas libre de bloqueos
    print("\nAbriendo la página de pruebas...")
    page.goto("https://the-internet.herokuapp.com")
    
    # 2. Validamos que el título de la pestaña sea el correcto
    print("Validando el título...")
    expect(page).to_have_title("The Internet")
    print("¡Prueba completada con éxito! 🎉")