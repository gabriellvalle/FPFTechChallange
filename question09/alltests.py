import time, pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup():
    """Configuração inicial: executada uma vez para todos os testes"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://www.vanilton.net/triangulo/")
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "v1, v2, v3", 
    [(5, 5, 5), (7, 7, 7), (10, 10, 10)]  # Exemplos de triângulos equiláteros
)
def test_valida_triangulos_equilateros(setup, v1, v2, v3):
    """Teste para triângulo equilátero"""
    driver = setup
    driver.find_element(By.XPATH, "//input[@name='V1']").send_keys(str(v1))
    driver.find_element(By.XPATH, "//input[@name='V2']").send_keys(str(v2))
    driver.find_element(By.XPATH, "//input[@name='V3']").send_keys(str(v3))
    driver.find_element(By.XPATH, "//input[@value='Identificar']").click()
    time.sleep(2)
    resultado = driver.find_element(By.XPATH, "//div[contains(text(), 'Equilátero')]").text
    assert "Equilátero" in resultado, f"Esperado 'Equilátero', mas obteve '{resultado}'"

@pytest.mark.parametrize(
    "v1, v2, v3", 
    [(5, 5, 8), (6, 6, 9), (7, 7, 10)]  # Exemplos de triângulos isósceles
)
def test_valida_triangulos_isosceles(setup, v1, v2, v3):
    """Teste para triângulo isósceles"""
    driver = setup
    driver.find_element(By.XPATH, "//input[@name='V1']").send_keys(str(v1))
    driver.find_element(By.XPATH, "//input[@name='V2']").send_keys(str(v2))
    driver.find_element(By.XPATH, "//input[@name='V3']").send_keys(str(v3))
    driver.find_element(By.XPATH, "//input[@value='Identificar']").click()
    time.sleep(2)
    resultado = driver.find_element(By.XPATH, "//div[contains(text(), 'Isósceles')]").text
    assert "Isósceles" in resultado, f"Esperado 'Isósceles', mas obteve '{resultado}'"

@pytest.mark.parametrize(
    "v1, v2, v3", 
    [(4, 5, 6), (7, 8, 9), (10, 11, 12)]  # Exemplos de triângulos escalenos
)
def test_valida_triangulos_escalenos(setup, v1, v2, v3):
    """Teste para triângulo escaleno"""
    driver = setup
    driver.find_element(By.XPATH, "//input[@name='V1']").send_keys(str(v1))
    driver.find_element(By.XPATH, "//input[@name='V2']").send_keys(str(v2))
    driver.find_element(By.XPATH, "//input[@name='V3']").send_keys(str(v3))
    driver.find_element(By.XPATH, "//input[@value='Identificar']").click()
    time.sleep(2)
    resultado = driver.find_element(By.XPATH, "//div[contains(text(), 'Escaleno')]").text
    assert "Escaleno" in resultado, f"Esperado 'Escaleno', mas obteve '{resultado}'"

@pytest.mark.parametrize(
    "v1, v2, v3", 
    [
        (4, 5, 6),         # Triângulo escaleno válido
        (6, 6, 9),         # Triângulo isósceles válido
        (2, 2, 2),         # Triângulo equilátero válido
        (1, 2, 3),         # Triângulo inválido (não forma um triângulo)
        (8, 1, 9),         # Triângulo inválido (não forma um triângulo)
        (10, 5, 2),        # Triângulo inválido (não forma um triângulo)
        (0, 5, 5),         # Triângulo inválido (lado zero)
        (1, 1, 3),         # Triângulo inválido (não forma um triângulo)
        (5, 5, 12),        # Triângulo inválido (não forma um triângulo)
        (100, 200, 300),   # Triângulo inválido (não forma um triângulo)
        (0, 0, 0),         # Triângulo inválido (todos os lados são zero)
        (6, 2, 15),        # Triângulo inválido (não forma um triângulo)
        (4, 4, 9),         # Triângulo inválido (não forma um triângulo)
        (3, 8, 15)         # Triângulo inválido (não forma um triângulo)
    ]  # Exemplos de lados para verificar validade
)
def test_triangulo_validade(setup, v1, v2, v3):
    """Teste para verificar se os lados fornecidos formam um triângulo válido"""
    driver = setup

    driver.find_element(By.XPATH, "//input[@name='V1']").clear()
    driver.find_element(By.XPATH, "//input[@name='V2']").clear()
    driver.find_element(By.XPATH, "//input[@name='V3']").clear()
    
    driver.find_element(By.XPATH, "//input[@name='V1']").send_keys(str(v1))
    driver.find_element(By.XPATH, "//input[@name='V2']").send_keys(str(v2))
    driver.find_element(By.XPATH, "//input[@name='V3']").send_keys(str(v3))
    driver.find_element(By.XPATH, "//input[@value='Identificar']").click()
    time.sleep(2)

    triangulo_valido = v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1
    resultado_site = driver.find_element(By.XPATH, "//div[last()]/img").get_attribute("alt")
    
    if not triangulo_valido:
        assert resultado_site not in ('triângulo equilátero', 'triângulo isósceles', 'triângulo escaleno'), \
            f'Erro encontrado para {v1, v2, v3}: Lados inválidos para triângulo mas obteve "{resultado_site}" pela ferramenta.'
    else:
        if v1 == v2 == v3:
            assert "equilátero" in resultado_site, f'Erro para {v1, v2, v3}: Esperado "Equilátero" mas obteve "{resultado_site}"'
        elif v1 == v2 or v1 == v3 or v2 == v3:
            assert "isósceles" in resultado_site, f'Erro para {v1, v2, v3}: Esperado "Isósceles" mas obteve "{resultado_site}"'
        else:
            assert "escaleno" in resultado_site, f'Erro para {v1, v2, v3}: Esperado "Escaleno" mas obteve "{resultado_site}"'
