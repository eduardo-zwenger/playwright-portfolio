from playwright.sync_api import Page, expect

def test_cargar_pagina(page):
    # 1. Entramos a la página de prácticas
    print("\nAbriendo la página de pruebas...")
    page.goto("https://automationexercise.com")
    
    # 2. Validamos que el título de la pestaña sea el correcto
    print("Validando el título...")
    expect(page).to_have_title("Automation Exercise")
    print("¡Prueba completada con éxito! 🎉")