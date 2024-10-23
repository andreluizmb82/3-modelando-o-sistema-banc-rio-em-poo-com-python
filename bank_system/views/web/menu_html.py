import http.server
import socketserver
from typing import Callable
from urllib.parse import urlparse, parse_qs

from .routing.employee_routng import *
from .routing.cliet_routng import *

#from models.account import Account
#from models.client import Individual, Client

import os
ROOT_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(ROOT_PATH, "assets")
TEMPLATES_PATH = os.path.join(ROOT_PATH, "templates")
#TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')

PORT = 8005

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    obj_selected = None
    def _build(
        self, 
        func: Callable[[str, dict[str, list[str]]], tuple[str, str, str, str, str, str, str]]
    ) -> None:
        
        #if(self.headers['Content-Length']):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        page_title, main_title, main_content, script_js, header_path, nav_path, main_path = func(TEMPLATES_PATH, query_params)
        
        html_header = ""
        html_main = ""
        html_nav = ""
        html_content = ""
        
        try:
            with open(header_path, "r", encoding="utf-8") as file:
                html_header = file.read()
                
            
            with open(main_path, "r", encoding="utf-8") as file:
                html_main = file.read()
                
                
            with open(nav_path, "r", encoding="utf-8") as file:
                html_nav = file.read()
                

                
            html_content = html_header.replace("{{script_js}}", script_js)
            html_content = html_content.replace("{{page_title}}", page_title)
            html_content = html_content.replace("{{nav}}", html_nav)
            
            html_main = html_main.replace("{{main_title}}", main_title)
            html_main = html_main.replace("{{main_content}}", main_content)
            
            html_content = html_content.replace("{{main}}", html_main)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Connection", "close")
            self.flush_headers()
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
                
        except FileNotFoundError as exp:
            self._handle_error(404, f"File not found: {exp}")
        except Exception as exp:
            self._handle_error(500, f"Server error: {str(exp)}")
            
            
    def _handle_error(self, status_code: int, message: str):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.send_header("Connection", "close")
        self.flush_headers()
        self.end_headers()
        self.wfile.write(f"<html><body><h1>{status_code} - {message}</h1></body></html>".encode('utf-8'))


    def do_GET(self):

        if self.path == '/':
            
            html_content = ""
            try:
                with open(f"{TEMPLATES_PATH}/index.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                    
                    html_content = html_content.replace("*{{message}}*", "My First Hello World - Message!")
                    
            except FileNotFoundError as exp:
                html_content = f"<html><body><h1>File not found</h1><p>{exp}</p></body></html>"
            except Exception as e:
                html_content = f"<html><body><h1>Error: {str(e)}</h1></body></html>"
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Connection", "close")
            self.flush_headers()
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
            
            
        elif self.path.endswith(".css"):
            try:
                css_path = os.path.join(ASSETS_PATH + "/css/")
                file_path = os.path.join(css_path, self.path.split("/")[-1])
                with open(file_path, "r", encoding="utf-8") as file:
                    css_content = file.read()

                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.send_header("Connection", "close")
                self.flush_headers()
                self.end_headers()
                self.wfile.write(css_content.encode('utf-8')) 
                
            except FileNotFoundError as exp:
                self._handle_error(404, f"File not found: {exp}")
            except Exception as exp:
                self._handle_error(500, f"Server error: {str(exp)}")
                
        elif self.path.endswith(".js"):
            try:
                js_path = os.path.join(ASSETS_PATH + "/js/")
                file_path = os.path.join(js_path, self.path.split("/")[-1])
                with open(file_path, "r", encoding="utf-8") as file:
                    css_content = file.read()

                self.send_response(200)
                self.send_header("Content-type", "text/script")
                self.send_header("Connection", "close")
                self.flush_headers()
                self.end_headers()
                self.wfile.write(css_content.encode('utf-8')) 
                
            except FileNotFoundError as exp:
                self._handle_error(404, f"File not found: {exp}")
            except Exception as exp:
                self._handle_error(500, f"Server error: {str(exp)}")

        
        elif self.path == "/employee":
            self._build(employee_root)
            
        elif self.path.startswith("/employee/new_client"):
            self._build(employee_new_client)
        
        elif self.path.startswith("/employee/new_account?cpf="):
            self._build(employee_new_account)
            
        elif self.path.startswith("/employee/client?cpf="):
            self._build(employee_client_select)
            
        elif self.path == "/employee/clients_list":
            self._build(employee_clients_list)
            
        elif self.path == "/employee/account_list":
            self._build(employee_account_list)
            
            
        elif self.path =="/client":
            self._build(client)
            
        elif self.path.startswith("/client/account"):
            self._build(client_select_account)
            
        elif self.path.startswith("/client/deposit"):
            self._build(client_deposit)
            
        elif self.path.startswith("/client/withdraw"):
            self._build(client_withdraw)
            
        elif self.path.startswith("/client/statement"):
            self._build(client_statement)
        
        elif self.path.startswith("/employee/new_client"):
            print(self.headers['Content-Length'])
            
            # Análise da URL para extrair os parâmetros de consulta
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)

            # Extração dos valores dos parâmetros
            new_cpf = query_params.get('new_cpf', [""])[0]
            name = query_params.get('name', [""])[0].strip('"')
            date_of_birth = query_params.get('date_of_birth', [""])[0].strip('"')
            address = query_params.get('address', [""])[0].strip('"')
            create_new_account = query_params.get('create_new_account', [""])[0]

            # Monta uma mensagem de resposta com os parâmetros recebidos
            response_message = f"""
            <html>
            <body>
                <h1>Detalhes do Funcionário</h1>
                <p>CPF: {new_cpf}</p>
                <p>Nome: {name}</p>
                <p>Data de Nascimento: {date_of_birth}</p>
                <p>Endereço: {address}</p>
                <p>Conta Nova: {create_new_account}</p>
            </body>
            </html>
            """
            # Envia a resposta
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Connection", "close")
            self.flush_headers()
            self.end_headers()
            self.wfile.write(response_message.encode('utf-8'))

        
        else:
            # Se a rota não for encontrada, retornar um erro 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.send_header("Connection", "close")
            self.flush_headers()
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 - Not Found</h1></body></html>")

            
    def do_POST(self):
        # Responder a uma requisição POST
        if self.path == '/':
            # Obter o comprimento do conteúdo enviado no corpo do POST
            content_length = int(self.headers['Content-Length'])
            # Ler o corpo da requisição
            post_data = self.rfile.read(content_length)
            

            # Responder com uma mensagem de confirmação
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Connection", "close")
            self.flush_headers()
            self.end_headers()
            response_message = "{\"Dados\": " + post_data.decode('utf-8') + "}"
            self.wfile.write(response_message.encode('utf-8'))

        elif self.path.startswith("/employee/new_client"):
            self._build(employee_new_client)
            
        else:
            # Se a rota não for encontrada, retornar um erro 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.send_header("Connection", "close")
            self.flush_headers()
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 - Not Found</h1></body></html>")


def start_menu_web():
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Acesse a pagina em localhost:{PORT} no seu navegador.")
        # Manter o servidor rodando
        httpd.serve_forever()

if __name__ == "__main__":
    # Criar o servidor
    start_menu_web()
