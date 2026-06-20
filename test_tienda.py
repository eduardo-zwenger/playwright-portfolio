from playwright.sync_api import Page, expect

def test_cargar_pagina(page: Page):
    # 1. Entramos a una página de prácticas libre de bloqueos
    print("\nAbriendo la página de pruebas...")
    page.goto("https://the-internet.herokuapp.com")
    
    # 2. Validamos que el título de la pestaña sea el correcto
    print("Validando el título...")
    expect(page).to_have_title("The Internet")
    print("¡Prueba completada con éxito! 🎉")


def test_formulario_login(page: Page):
    # 1. Ir directo a la página del formulario de login
        print("\nNavegando al formulario de Login...")
        page.goto("https://the-internet.herokuapp.com/login")
    
    # 2. Interactuar con los campos de texto (.fill)
    # Buscamos el input por su atributo id (#username) y escribimos el usuario correcto
        print("Escribiendo las credenciales...")
        page.locator("#username").fill("tomsmith")
    
    # Buscamos el input de la contraseña (#password) y escribimos la clave correcta
        page.locator("#password").fill("SuperSecretPassword!")
    
    # 3. Hacer clic en el botón de enviar (.click)
    # Buscamos el botón que sea de tipo 'submit' dentro del formulario
        print("Haciendo clic en el botón de Login...")
        page.click("button[type='submit']")
    
    # 4. Aserciones: Validar que el login fue exitoso
    # Buscamos el cartel verde de alerta que confirma que entramos
        alerta_exito = page.locator("#flash")
    
    # Verificamos que el cartel sea visible en la pantalla
        expect(alerta_exito).to_be_visible()
    
    # Verificamos que el cartel contenga el texto de bienvenida esperado
        expect(alerta_exito).to_contain_text("You logged into a secure area!")
        print("¡Login exitoso y validado correctamente! 🔐🎉")