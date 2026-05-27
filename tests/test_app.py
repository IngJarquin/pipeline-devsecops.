import unittest
from src.app import validate_email

class TestSecurityValidations(unittest.TestCase):

    def test_valid_emails(self):
        """Prueba que los formatos de correo legítimos sean aceptados correctamente."""
        self.assertTrue(validate_email("usuario@dominio.com"))
        self.assertTrue(validate_email("seguridad.devsecops@empresa.org"))
        self.assertTrue(validate_email("datos-sensibles123@sub.dominio.net"))

    def test_invalid_emails(self):
        """Prueba que los formatos de correo malformados o corruptos sean rechazados."""
        self.assertFalse(validate_email("usuario_sin_arroba.com"))
        self.assertFalse(validate_email("usuario@dominio_sin_punto"))
        self.assertFalse(validate_email(" @dominio.com"))
        self.assertFalse(validate_email(""))

    def test_sql_injection_payload_in_email(self):
        """
        Prueba de Seguridad (Abuse Case): Asegura que si un atacante intenta 
        inyectar código SQL en el campo de email, el validador lo intercepte y lo rechace.
        """
        sql_payload_1 = "admin@empresa.com' OR '1'='1"
        sql_payload_2 = "test@correo.com'; DROP TABLE records;--"
        
        self.assertFalse(validate_email(sql_payload_1))
        self.assertFalse(validate_email(sql_payload_2))

if __name__ == "__main__":
    unittest.main()
