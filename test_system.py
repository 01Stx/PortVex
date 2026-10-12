import unittest
from unittest.mock import patch
from system import diagnostico_sistema


class TestDiagnosticoSistema(unittest.TestCase):

    @patch("builtins.print")
    @patch("system.os.getcwd", return_value="D:\\projetos")
    @patch("system.platform.architecture", return_value=("64bit", "WindowsPE"))
    @patch("system.platform.version", return_value="10.0")
    @patch("system.platform.system", return_value="Windows")
    @patch("system.platform.node", return_value="PC-TESTE")
    @patch("system.getpass.getuser", return_value="usuario_teste")
    def test_diagnostico_exibe_informacoes(
        self,
        mock_usuario,
        mock_computador,
        mock_sistema,
        mock_versao,
        mock_arquitetura,
        mock_diretorio,
        mock_print
    ):
        diagnostico_sistema()

        
        saida = "\n".join(
            str(chamada.args[0])
            for chamada in mock_print.call_args_list
        )

        self.assertIn("DIAGNÓSTICO DO SISTEMA", saida)
        self.assertIn("PC-TESTE", saida)
        self.assertIn("Windows", saida)
        self.assertIn("64bit", saida)
        self.assertIn(r"D:\projetos", saida)



if __name__ == "__main__":
    unittest.main()